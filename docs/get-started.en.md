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

- `id`: ID of the comment.
- `text`: Text of the comment.
- `is_offensive`: Whether the comment is offensive or not.
- `is_targeted`: Whether the comment is targeted or not.
- `targeted_type`: Type of the target (individual, group, or other). Only available if `is_targeted` is `True`.
- `toxic_spans`: List of toxic spans.
- `health`: Whether the comment contains health-related toxicity.
- `ideology`: Whether the comment contains ideology-related toxicity.
- `insult`: Whether the comment contains insult-related toxicity.
- `lgbtqphobia`: Whether the comment contains lgbtqphobia-related toxicity.
- `other_lifestyle`: Whether the comment contains other_lifestyle-related toxicity.
- `physical_aspects`: Whether the comment contains physical_aspects-related toxicity.
- `profanity_obscene`: Whether the comment contains profanity-related toxicity.
- `racism`: Whether the comment contains racism-related toxicity.
- `religious_intolerance`: Whether the comment contains religious_intolerance-related toxicity.
- `sexism`: Whether the comment contains sexism-related toxicity.
- `xenophobia`: Whether the comment contains xenophobia-related toxicity.

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