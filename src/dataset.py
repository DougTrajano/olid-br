import logging
import uuid
from typing import Any, Dict, List, Union

from src.data_classes import (
    Annotation,
    Annotator,
    LabelStrategy,
    Metadata,
    ProcessedText,
    RawText
)

_logger = logging.getLogger(__name__)

class Dataset(object):
    def __init__(self, annotators: List[Annotator], toxicity_threshold: float = 0.5):
        """Initialize the BuildDataset class."""
        self.annotators = annotators
        self.toxicity_threshold = toxicity_threshold

        _logger.debug("Initializing the BuildDataset class.")

    def _clean_text(self, text: str):
        """Clean the text of any unwanted characters.

        Args:
        - text: The text to clean.

        Returns:
        - The cleaned text.
        """
        _logger.debug(f"Cleaning the text: {text}")

        # Remove newlines, tabs, etc.
        for char in ["\n", "\t", "\r"]:
            text = text.replace(char, " ")

        # Remove multiple spaces
        text = " ".join(text.split())
        text = text.strip()

        _logger.debug(f"Cleaned the text: {text}")
        return text

    def _get_annotation_by_id(self, annotations: List[Any], annotator_id: int) -> Dict[Any, Any]:
        """Get an annotation by annotator id.

        Args:
        - annotations: The list of annotations.
        - annotator_id: The annotator id.

        Returns:
        - The annotation.
        """
        for annotation in annotations:
            if annotation["completed_by"] == annotator_id:
                return annotation

    def _get_is_offensive(self, annotations: List[Any], annotator_id: int) -> str:
        """Get the is_toxic attribute from a given annotation.

        Args:
        - annotations: List of annotations.
        - annotator_id: The annotator id.

        Returns:
        - "OFF" if text is offensive, "NOT" otherwise.
        """
        annotation = self._get_annotation_by_id(annotations, annotator_id)
        if annotation:
            for each in annotation["result"]:
                if each["from_name"] == "is_toxic":
                    if each["value"]["choices"][0] == "Yes":
                        return "OFF"
                    else:
                        return "NOT"

    def _get_is_targeted(self, annotations: List[Any], annotator_id: int) -> str:
        """Get the is_targeted attribute from a given annotation.

        Args:
        - annotations: List of annotations.
        - annotator_id: The annotator id.

        Returns:
        - "TIN" if text is targeted, "UNT" otherwise.
        """
        targeted_type = self._get_targeted_type(annotations, annotator_id)
        if isinstance(targeted_type, str):
            return "TIN"
        else:
            return "UNT"

    def _get_targeted_type(self, annotations: List[Any], annotator_id: int) -> str:
        """Get the targeted_type attribute from a given annotation.

        Args:
        - annotations: List of annotations.
        - annotator_id: The annotator id.

        Returns:
        - "IND" if text is targeted to an individual, "GRP" if it is targeted to a group, "OTH" otherwise.
        """
        annotation = self._get_annotation_by_id(annotations, annotator_id)
        if annotation:
            for each in annotation["result"]:
                if each["from_name"] in ["target", "target_type"]:
                    if each["value"]["choices"][0] == "Individual":
                        return "IND"
                    elif each["value"]["choices"][0] == "Group":
                        return "GRP"
                    elif each["value"]["choices"][0] == "Other":
                        return "OTH"
                    else:
                        raise ValueError("Invalid targeted type.")

    def _get_offensive_type(self, annotations: List[Any], annotator_id: int, label: Union[str, List[str]]) -> bool:
        """Get the offensive type for a given annotation.

        Args:
        - annotations: List of annotations.
        - annotator_id: The annotator id.
        - label: The label of the offensive type.
        
        Returns:
        - True if the offensive text is related to label, False otherwise.
        """
        annotation = self._get_annotation_by_id(annotations, annotator_id)
        if annotation:        
            for each in annotation["result"]:
                if each["from_name"] in ["Sentiment", "toxic_labels"]:
                    if isinstance(label, str):
                        if label in each["value"]["choices"]:
                            return True
                    elif isinstance(label, list):
                        for l in label:
                            if l in each["value"]["choices"]:
                                return True
        return False
        
    def _get_toxic_spans(self, annotations: List[Any], annotator_id: int) -> List[int]:
        """Get the toxic spans for a given annotation.

        Args:
        - annotations: List of annotations.
        - annotator_id: The annotator id.

        Returns:
        - List of spans.
        """
        spans = []

        annotation = self._get_annotation_by_id(annotations, annotator_id)
        if annotation:    
            for each in annotation["result"]:
                if each["from_name"] in ["BadWords", "toxic_spans"]:
                    tmp_spans = list(range(each["value"]["start"], each["value"]["end"]))
                    spans.extend(tmp_spans)

        if len(spans) > 0:
            spans = list(set(spans))
            spans.sort()            
        return spans
            
    def _get(self, item: Dict[Any, Any]):

        text = RawText(
            id=uuid.uuid4().hex,
            text=self._clean_text(item["data"]["text"]),
            source=item["data"]["meta_info"]["source"],
            created_at=item["data"]["meta_info"]["created_at"],
            collected_at=item["data"]["meta_info"]["collected_at"],
            is_toxic=item["data"]["meta_info"]["toxicity_score"] > self.toxicity_threshold,
            toxicity_score=item["data"]["meta_info"]["toxicity_score"],
            publisher_category=item["data"]["meta_info"].get("category")
        )

        # Get the annotations
        for item_annotation in item["annotations"]:
            if item_annotation["completed_by"] in [a.annotator_id for a in self.annotators]:
                annotation_id = item_annotation["completed_by"]
                annotation = Annotation(
                    annotator_id=annotation_id,
                    is_offensive=self._get_is_offensive(item["annotations"], annotation_id),
                    is_targeted=self._get_is_targeted(item["annotations"], annotation_id),
                    targeted_type=self._get_targeted_type(item["annotations"], annotation_id),
                    toxic_spans=self._get_toxic_spans(item["annotations"], annotation_id),
                    health=self._get_offensive_type(item["annotations"], annotation_id, "Health"),
                    ideology=self._get_offensive_type(item["annotations"], annotation_id, "Ideology"),
                    insult=self._get_offensive_type(item["annotations"], annotation_id, "Insult"),
                    lgbtqphobia=self._get_offensive_type(item["annotations"], annotation_id, ["Identity Attack", "LGBTQphobia"]),
                    other_lifestyle=self._get_offensive_type(item["annotations"], annotation_id, "Other-Lifestyle"),
                    physical_aspects=self._get_offensive_type(item["annotations"], annotation_id, ["Body", "Physical Aspects"]),
                    profanity_obscene=self._get_offensive_type(item["annotations"], annotation_id, ["Profanity", "Profanity/Obscene"]),
                    racism=self._get_offensive_type(item["annotations"], annotation_id, "Racism"),
                    religious_intolerance=self._get_offensive_type(item["annotations"], annotation_id, "Religious intolerance"),
                    sexism=self._get_offensive_type(item["annotations"], annotation_id, "Sexism"),
                    xenophobia=self._get_offensive_type(item["annotations"], annotation_id, "Xenophobia"),
                    )

                text.annotations.append(annotation)

        return text

    def get_raw_texts(self, raw: List[Dict[Any, Any]]):
        """Get all annotations for a list of label studio raw data.

        Args:
        - raw: The raw data from the label studio.
        
        Returns:
        - A list of RawText and Metadata objects.
        """
        _logger.debug(f"Getting the annotation for {len(raw)} items.")

        texts = []
        for item in raw:
            text = self._get(item)
            texts.append(text)

        _logger.debug(f"Got raw texts for {len(texts)} items.")
        return texts

    def get_processed_texts(self, raw: List[Dict[Any, Any]],
                            label_strategy: LabelStrategy = LabelStrategy()) -> List[ProcessedText]:
        """Get processed texts from raw texts.

        Args:
        - raw: The raw data from the label studio.
        - label_strategy: The label strategy.

        Returns:
        - A list of ProcessedText objects.
        """
        _logger.debug(f"Processing {len(raw)} texts.")

        texts = []
        metadata = []

        for text in raw:
            # Processed Text
            processed_text = ProcessedText(
                id=text.id,
                text=text.text,
                is_offensive=label_strategy.is_offensive([i.is_offensive for i in text.annotations]),
                is_targeted=label_strategy.is_targeted([i.is_targeted for i in text.annotations]),
                targeted_type=label_strategy.targeted_type([i.targeted_type for i in text.annotations]),
                toxic_spans=label_strategy.toxic_spans([i.toxic_spans for i in text.annotations]),
                health=label_strategy.health([i.health for i in text.annotations]),
                ideology=label_strategy.ideology([i.ideology for i in text.annotations]),
                insult=label_strategy.insult([i.insult for i in text.annotations]),
                lgbtqphobia=label_strategy.lgbtqphobia([i.lgbtqphobia for i in text.annotations]),
                other_lifestyle=label_strategy.other_lifestyle([i.other_lifestyle for i in text.annotations]),
                physical_aspects=label_strategy.physical_aspects([i.physical_aspects for i in text.annotations]),
                profanity_obscene=label_strategy.profanity_obscene([i.profanity_obscene for i in text.annotations]),
                racism=label_strategy.racism([i.racism for i in text.annotations]),
                religious_intolerance=label_strategy.religious_intolerance([i.religious_intolerance for i in text.annotations]),
                sexism=label_strategy.sexism([i.sexism for i in text.annotations]),
                xenophobia=label_strategy.xenophobia([i.xenophobia for i in text.annotations]),
            )

            # Origin metadata
            meta_info = Metadata(
                id=text.id,
                source=text.source,
                created_at=text.created_at,
                collected_at=text.collected_at,
                toxicity_score=text.toxicity_score,
                category=text.publisher_category
            )

            texts.append(processed_text)
            metadata.append(meta_info)

            # Annotators
            for annotation in text.annotations:
                annotator = [i for i in self.annotators if i.annotator_id == annotation.annotator_id][0].copy()
                annotator.id = text.id
                metadata.append(annotator)

        _logger.debug("Processed all texts.")
        return texts, metadata

    def get_annotations(self, texts: List[RawText], feature: str):
        """Get all annotations for a list of texts.

        Args:
        - texts: The list of texts to get the annotations for.
        - feature: The feature to get the annotations for.

        Returns:
        - A dictionary of annotators and their annotations.
            (e.g. {annotator_id: [annotation1, annotation2, ...]})
        """
        data = {}

        for text in texts:
            for annotation in text.annotations:
                if annotation.annotator_id not in data.keys():
                    data[annotation.annotator_id] = [annotation[feature]]
                else:
                    data[annotation.annotator_id].append(annotation[feature])
        return data
        
    def build(self, raw: List[Dict[Any, Any]], label_strategy: LabelStrategy = LabelStrategy()):
        """Process a list of label studio raw data and build the dataset.
        
        Args:
        - raw: The raw data from the label studio.
        - label_strategy: The label strategy.

        Returns:
        - A tuple of (List[ProcessedText], List[Metadata]) objects.
        """
        _logger.debug(f"Building the dataset for {len(raw)} items.")

        raw_texts = self.get_raw_texts(raw)
        texts, metadata = self.get_processed_texts(raw_texts, label_strategy)
                
        _logger.debug(f"Built the dataset for {len(texts)} items.")
        return texts, metadata