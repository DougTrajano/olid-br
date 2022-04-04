from typing import List, Any

def has_32_annotator(annotations: List[Any]) -> bool:
    for annotation in annotations:
        if annotation["completed_by"] == 32:
            return True
    return False

def get_is_offensive(annotations: List[Any]) -> str:
    """
    Get the is_toxic attribute from the annotations.

    Args:
    - annotations: List of annotations.

    Returns:
    - "OFF" if text is offensive, "NOT" otherwise.
    """
    has_32 = has_32_annotator(annotations)
    for annotation in annotations:
        # If we have annotator 32, return this annotation
        if has_32:
            if annotation["completed_by"] == 32:
                for each in annotation["result"]:
                    if each["from_name"] == "is_toxic":
                        if each["value"]["choices"][0] == "Yes":
                            return "OFF"
                        else:
                            return "NOT"
        else:
            # Return the first annotation
            for each in annotation["result"]:
                if each["from_name"] == "is_toxic":
                    if each["value"]["choices"][0] == "Yes":
                        return "OFF"
                    else:
                        return "NOT"

def get_is_targeted(annotations: List[Any]) -> str:
    """
    Get the is_targeted attribute from the annotations.

    Args:
    - annotations: List of annotations.

    Returns:
    - "TIN" if text is targeted, "UNT" otherwise.
    """
    targeted_type = get_targeted_type(annotations)
    if isinstance(targeted_type, str):
        return "TIN"
    else:
        return "UNT"

def get_targeted_type(annotations: List[Any]) -> str:
    """
    Get the targeted_type attribute from the annotations.

    Args:
    - annotations: List of annotations.

    Returns:
    - "IND" if text is targeted to an individual, "GRP" if it is targeted to a group, "OTH" otherwise.
    """
    has_32 = has_32_annotator(annotations)
    for annotation in annotations:
        # If we have annotator 32, return this annotation
        if has_32:
            if annotation["completed_by"] == 32:
                for each in annotation["result"]:
                    if each["from_name"] == "target":
                        if each["value"]["choices"][0] == "Individual":
                            return "IND"
                        elif each["value"]["choices"][0] == "Group":
                            return "GRP"
                        elif each["value"]["choices"][0] == "Other":
                            return "OTH"
                        else:
                            raise ValueError("Invalid targeted type")
        else:
            # Return the first annotation
            for each in annotation["result"]:
                if each["from_name"] == "target":
                    if each["value"]["choices"][0] == "Individual":
                        return "IND"
                    elif each["value"]["choices"][0] == "Group":
                        return "GRP"
                    elif each["value"]["choices"][0] == "Other":
                        return "OTH"
                    else:
                        raise ValueError("Invalid targeted type")

def get_offensive_type(annotations: List[Any], label: str) -> str:
    """
    Get the health attribute from the annotations.

    Args:
    - annotations: List of annotations.
    - label: The label of the offensive type.
    
    Returns:
    - True if the offensive text is related to label, False otherwise.
    """
    has_32 = has_32_annotator(annotations)
    for annotation in annotations:
        # If we have annotator 32, return this annotation
        if has_32:
            if annotation["completed_by"] == 32:
                for each in annotation["result"]:
                    if each["from_name"] == "Sentiment":
                        if label in each["value"]["choices"]:
                            return True
        else:
            # Return the first annotation
            for each in annotation["result"]:
                if each["from_name"] == "Sentiment":
                    if label in each["value"]["choices"]:
                        return True
    return False

def get_toxic_spans(annotations: List[Any]) -> List[Any]:
    """
    Get the toxic_spans attribute from the annotations.

    Args:
    - annotations: List of annotations.

    Returns:
    - List of spans.
    """
    spans = []
    has_32 = has_32_annotator(annotations)
    for annotation in annotations:
        # If we have annotator 32, return this annotation
        if has_32:
            if annotation["completed_by"] == 32:
                for each in annotation["result"]:
                    if each["from_name"] == "BadWords":
                        tmp_spans = list(range(each["value"]["start"], each["value"]["end"]))
                        spans.extend(tmp_spans)
        else:
            # Return the first annotation
            for each in annotation["result"]:
                if each["from_name"] == "BadWords":
                    tmp_spans = list(range(each["value"]["start"], each["value"]["end"]))
                    spans.extend(tmp_spans)
    
    if len(spans) > 0:
        spans = list(set(spans))
        spans.sort()
        
        return spans