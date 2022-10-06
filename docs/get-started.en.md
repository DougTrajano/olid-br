---
title: Get Started
summary: How to use the OLID-BR dataset.
---

The dataset will be available on Kaggle and Hugging Face.

[Kaggle Datasets](https://www.kaggle.com/dougtrajano/olidbr){ .md-button }

## Dataset Sampling

The dataset is composed of the following files:

- `train.csv`: contains the training.
- `test.csv`: contains the test data.
- `train_metadata.csv`: contains the metadata of the training data.
- `test_metadata.csv`: contains the metadata of the test data.
- `train.json`: contains the training data in JSON format.
- `test.json`: contains the test data in JSON format.
- `additional_data.json`: contains additional data in JSON format. This data was not used in the creation of the dataset.

`train.csv` and `test.csv` follow the label assignment described in the [Label Assignment](#label-assignment) section.

The JSON files (`train.json`, `test.json`, and `additional_data.json`) contain all three annotations and the metadata for each instance.

Hugging Face only has the train (`train.csv`) and test (`test.csv`) files.

## Data Format

### CSV

The CSV files are encoded in UTF-8 and have the following columns:

| Column | Description |
|--------|-------------|
| id | The ID of the tweet. |
| text | The text of the tweet. |
| is\_offensive | The label for the offensive language detection task. |
| is\_targeted | The label for the offensive language target identification task. |
| targeted\_type | The label for the categorization of offensive language task. |
| toxic\_spans | The toxic spans of the tweet. |
| health | The label for the categorization of offensive language task. |
| ideology | The label for the categorization of offensive language task. |
| insult | The label for the categorization of offensive language task. |
| lgbtqphobia | The label for the categorization of offensive language task. |
| other\_lifestyle | The label for the categorization of offensive language task. |
| physical\_aspects | The label for the categorization of offensive language task. |
| profanity\_obscene | The label for the categorization of offensive language task. |
| racism | The label for the categorization of offensive language task. |
| religious\_intolerance | The label for the categorization of offensive language task. |
| sexism | The label for the categorization of offensive language task. |
| xenophobia | The label for the categorization of offensive language task. |

### JSON

The JSON files are encoded in UTF-8 and have the following schema:

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

## Label Assignment

We applied the following rules to assign the labels:

