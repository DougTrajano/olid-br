---
title: Get Started
summary: How to use the OLID-BR dataset.
---

The dataset will be available on Kaggle and Hugging Face.

## Kaggle

You can see the dataset on [OLID-BR | Kaggle](https://www.kaggle.com/datasets/dougtrajano/olidbr).

The snippet below shows how to download the dataset using the Kaggle API.

```python
from kaggle.api.kaggle_api_extended import KaggleApi

kaggle = KaggleApi()
kaggle.authenticate()
kaggle.dataset_download_files(dataset="olidbr", unzip=True)
```

## Hugging Face

You can see the OLID-BR dataset on [dougtrajano/olid-br · Datasets at Hugging Face](https://huggingface.co/datasets/dougtrajano/olid-br).

```python
# pending
```

## Dataset Files

The dataset is composed of the following files:

- `train.csv`: contains the training.
- `test.csv`: contains the test data.
- `train_metadata.csv`: contains the metadata of the training data.
- `test_metadata.csv`: contains the metadata of the test data.
- `train.json`: contains the training data in JSON format.
- `test.json`: contains the test data in JSON format.
- `additional_data.json`: contains additional data in JSON format. This data was not used in the creation of the dataset.

`train.csv` and `test.csv` follow the label assignment described in the [**Label Assignment**](#label-assignment) section.

The JSON files (`train.json`, `test.json`, and `additional_data.json`) contain all three annotations and the metadata for each instance.

Hugging Face only has the train (`train.csv`) and test (`test.csv`) files.

### Data Format

#### CSV

The **CSV** files are encoded in UTF-8 and have the following columns:

- `id` (string): Unique identifier of the instance.
- `text` (string): The text of the instance.
- `is_offensive` (string): Whether the text is offensive (`OFF`) or not (`NOT`).
- `is_targeted` (string): Whether the text is targeted (`TIN`) or untargeted (`UNT`).
- `targeted_type` (string): Type of the target (individual `IND`, group `GRP`, or other `OTH`). Only available if `is_targeted` is `True`.
- `toxic_spans` (string): List of toxic spans.
- `health` (boolean): Whether the text contains hate speech based on health conditions such as disability, disease, etc.
- `ideology` (boolean): Indicates if the text contains hate speech based on a person's ideas or beliefs.
- `insult` (boolean): Whether the text contains insult, inflammatory, or provocative content.
- `lgbtqphobia` (boolean): Whether the text contains harmful content related to gender identity or sexual orientation.
- `other_lifestyle` (boolean): Whether the text contains hate speech related to life habits (e.g. veganism, vegetarianism, etc.).
- `physical_aspects` (boolean): Whether the text contains hate speech related to physical appearance.
- `profanity_obscene` (boolean): Whether the text contains profanity or obscene content.
- `racism` (boolean): Whether the text contains prejudiced thoughts or discriminatory actions based on differences in race/ethnicity.
- `religious_intolerance` (boolean): Whether the text contains religious intolerance.
- `sexism` (boolean): Whether the text contains discriminatory content based on differences in sex/gender (e.g. sexism, misogyny, etc.).
- `xenophobia` (boolean): Whether the text contains hate speech against foreigners.

The CSV files follow our label assignment strategy as described below.

- `is_offensive`: majority vote.
- `is_targeted`: majority vote.
- `targeted_type`: majority vote.
- `toxic_spans`: all labeled spans.
- `health`: at least one.
- `ideology`: at least one.
- `insult`: at least one.
- `lgbtqphobia`: at least one.
- `other_lifestyle`: at least one.
- `physical_aspects`: at least one.
- `profanity_obscene`: at least one.
- `racism`: at least one.
- `religious_intolerance`: at least one.
- `sexism`: at least one.
- `xenophobia`: at least one.

#### JSON

The **JSON** files are encoded in UTF-8 and have the following schema:

```json
{
  "id": "string",
  "text": "string",
  "metadata": {
    "source": "string",
    "created_at": "string",
    "collected_at": "string",
    "toxicity_score": "number",
  },
  "annotations": [
    {
      "annotator_id": "number",
      "is_offensive": "string",
      "is_targeted": "string",
      "targeted_type": "string",
      "toxic_spans": ["number"],
      "health": "boolean",
      "ideology": "boolean",
      "insult": "boolean",
      "lgbtqphobia": "boolean",
      "other_lifestyle": "boolean",
      "physical_aspects": "boolean",
      "profanity_obscene": "boolean",
      "racism": "boolean",
      "religious_intolerance": "boolean",
      "sexism": "boolean",
      "xenophobia": "boolean"
    }
  ]
}
```

## Metadata

We provide some metadata for the dataset to help further analysis.

### Annotators

For each qualified annotator, we asked him/her to provide the following information:

- `annotator_id`: The annotator's unique ID.
- `age`: The annotator's age.
- `gender` The gender of the annotator.
    - Male
    - Female
    - Other
- `education_level`: The education level of the annotator.
    - Primary School
    - Secondary School
    - Bachelor's Degree
    - Master's Degree
    - Doctoral Degree
- `annotator_type`: The type of the annotator.
    - Volunteer
    - Researcher
    - Contract Worker
- `background`: The background of the annotator.
    - Computer Science
    - Social Science

This information can be used to provide a better understanding of the annotator profile, maintaining the anonymity of the annotator

### Comments

For each comment, we collect contextual information based on the social media posts or the dataset that it comes from.

- `source` The social media platform where the text was posted.
- `created_at` The date and time of the post.
- `collected_at` The date and time of the collection.
- `toxicity_score` The toxicity score of the comment.