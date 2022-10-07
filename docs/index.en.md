---
title: Overview
summary: Offensive Language Identification Dataset for Brazilian Portuguese.
---

# OLID-BR

Offensive Language Identification Dataset for Brazilian Portuguese (OLID-BR) is a dataset with multi-task annotations for the detection of offensive language.

The current version (v1.0) contains **7,943** comments from different sources, including social media (YouTube and Twitter) and related datasets.

OLID-BR contains a collection of annotated sentences in Brazilian Portuguese using an annotation model that encompasses the following levels:

- [[Offensive content detection](#offensive-content-detection)]{Detect offensive content in sentences and categorize it.|top-right}
- [[Offense target identification](#offense-target-identification)]{Detect if an offensive sentence is targeted to a person or group of people.|top-right}
- [[Offensive spans identification](#offensive-spans-identification)]{Detect curse words in sentences.|top-right}

<figure>
  <img src="images/olid-br-taxonomy.png"/>
  <figcaption>Hierarchical taxonomy for categorizing offensive language. Proposed by author, adapted from <a href="https://arxiv.org/abs/1902.09666" target="_blank">Zampieri et al. (2019)</a>.</figcaption>
</figure>

## Categorization

### Offensive Content Detection

This level is used to detect offensive content in the sentence.

**Is this text offensive?**

We use the [[Perspective API](https://www.perspectiveapi.com/)]{Perspective API is the product of a collaborative research effort by Jigsaw and Google's Counter Abuse Technology team.|top-right} to detect if the sentence contains offensive content with double-checking by our [qualified annotators](annotation/index.en.md#who-are-qualified-annotators).

- `OFF` Offensive: Inappropriate language, insults, or threats.
- `NOT` Not offensive: No offense or profanity.

**Which kind of offense does it contain?**

The following labels were tagged by our annotators:

`Health`, `Ideology`, `Insult`, `LGBTQphobia`, `Other-Lifestyle`, `Physical Aspects`, `Profanity/Obscene`, `Racism`, `Religious Intolerance`, `Sexism`, and `Xenophobia`.

See the [Glossary](glossary.en.md) for further information.

### Offense Target Identification

This level is used to detect if an offensive sentence is targeted to a person or group of people.

**Is the offensive text targeted?**

- `TIN` Targeted Insult: Targeted insult or threat towards an individual, a group or other.
- `UNT` Untargeted: Non-targeted profanity and swearing.

**What is the target of the offense?**

- `IND` The offense targets an individual, often defined as “cyberbullying”.
- `GRP` The offense targets a group of people based on ethnicity, gender, sexual
- `OTH` The target can belong to other categories, such as an organization, an event, an issue, etc.

### Offensive Spans Identification

As toxic spans, we define a sequence of words that attribute to the text's toxicity.

For example, let's consider the following text:

> "USER `Canalha` URL"

The toxic spans are:

```python
[5, 6, 7, 8, 9, 10, 11, 12, 13]
```

## Dataset Structure

### Data Instances

Each instance is a social media comment with a corresponding ID and annotations for all the tasks described below.

### Data Fields

The simplified configuration includes:

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

See the [**Get Started**](get-started.en.md) page for more information.

## Considerations for Using the Data

### Social Impact of Dataset

Toxicity detection is a worthwhile problem that can ensure a safer online environment for everyone.

However, toxicity detection algorithms have focused on English and do not consider the specificities of other languages.

This is a problem because the toxicity of a comment can be different in different languages.

Additionally, the toxicity detection algorithms focus on the binary classification of a comment as toxic or not toxic.

Therefore, we believe that the OLID-BR dataset can help to improve the performance of toxicity detection algorithms in Brazilian Portuguese.

### Discussion of Biases

We are aware that the dataset contains biases and is not representative of global diversity.

We are aware that the language used in the dataset could not represent the language used in different contexts.

Potential biases in the data include: Inherent biases in the social media and user base biases, the offensive/vulgar word lists used for data filtering, and inherent or unconscious bias in the assessment of offensive identity labels.

All these likely affect labeling, precision, and recall for a trained model.

## Citation

Pending

## References

The OLID-BR dataset is based on the OLID dataset proposed by Zampieri et al. (2019)[^1] and other related works.

[^1]: Zampieri et al. "Predicting the type and target of offensive posts in social media." NAACL 2019.
[^2]: João A. Leite, Diego F. Silva, Kalina Bontcheva, Carolina Scarton (2020): Toxic Language Detection in Social Media for Brazilian Portuguese: New Dataset and Multilingual Analysis. Published at AACL-IJCNLP 2020.
[^3]: S. Malmasi, "Offensive Language Identification Dataset - OLID", Scholar.harvard.edu, 2021. [Online]. Available: https://scholar.harvard.edu/malmasi/olid. [Accessed: 28- Aug- 2021].
[^4]: Weng, L. (2021, March 21). Reducing toxicity in language models. Lil'Log. https://lilianweng.github.io/lil-log/2021/03/21/reducing-toxicity-in-language-models.html.
