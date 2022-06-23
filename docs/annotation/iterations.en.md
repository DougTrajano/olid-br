---
title: Annotation Iterations
summary: The iterations of the annotation process of the OLID-BR dataset.
---

# Iterations

We decided to work in iterations because it allow us validate and improve the annotation process and guidelines. Each iteration has its own goals and objectives.

## Iteration 1

[![Status badge](https://img.shields.io/badge/Status-Finished-blue.svg)](https://shields.io/)

In this iteration, our goal was to validate and refine our annotation process. It was the first time that we applied the annotation process. Two annotators labeled the data. The first annotator was a volunteer, the second was the author of the dataset. The volunteer provided useful feedback to adjust the annotation process. The data labeled by the researcher was predominated under the volunteer's labels as the researcher fixed some mistakes in the annotation process.

### Inter-Rater Reliability

In this iteration, we didn't generated the inter-rater reliability analysis because we did some changes and alignments during the iteration.

<details><summary>Profiling Report</summary>

<iframe width=100% height=500 frameBorder=0 src="../reports/olidbr_pilot.html"></iframe>

</details>

## Iteration 2

[![Status badge](https://img.shields.io/badge/Status-Finished-blue.svg)](https://shields.io/)

In the second iteration, we introduced contract workers to do the annotations. The annotators were trained by the author of the dataset as described in [**Qualified annotators**](qualified-annotators.en.md).

### Inter-Rater Reliability

As described in the [**Inter-Rater Reliability**](inter-rater-reliability.en.md) section, we evaluate the reliability of the annotators using a several coefficients.

We also address the analysis considering as a multi-label problem or several binary problems.

**Multi-Label Problem**

For all our [**toxicity labels**]{health, ideology, insult, lgbtqphobia, other_lifestyle, physical_aspects, profanity_obscene, racism, religious_intolerance, sexism, xenophobia} we calculate the Krippendorff's alpha (using the MASI distance) and the Percent Agreement.

- **Krippendorff's alpha**: 0.1962 (slight agreement)
- **Percent Agreement**: 0.1877

**Binary Problem**

| Feature / metrics          | Percent Agreement | Krippendorff's alpha | Gwet's AC<sub>1</sub> | Comments |
| -------------------------- | :---------------: | :------------------: | :--------: | -------- |
| **is\_offensive**          | 0.7277            | 0.0595               | 0.7750     | |
| **is\_targeted**           | 0.1610            | \-0.1348             | \-0.1029   | [1] |
| **targeted\_type**         | 0.0641            | 0.2461               | 0.4978     | [1] |
| **toxic\_spans**           | 0.1220            | 0.2709               | N/A        | |
| **health**                 | 0.9760            | 0.0447               | 0.9837     | |
| **ideology**               | 0.7647            | 0.3019               | 0.7976     | [3] |
| **insult**                 | 0.4713            | 0.0895               | 0.425      | [3] |
| **lgbtqphobia**            | 0.9453            | 0.5583               | 0.9603     | |
| **other\_lifestyle**       | 0.9860            | 0.0824               | 0.9906     | |
| **physical\_aspects**      | 0.9463            | 0.3272               | 0.9622     | |
| **profanity\_obscene**     | 0.6837            | 0.0850               | 0.726      | [3] |
| **racism**                 | 0.9750            | 0.2564               | 0.9829     | |
| **religious\_intolerance** | 1.0               | 1.0                  | 1.0        | [2] |
| **sexism**                 | 0.8753            | 0.1721               | 0.9076     | |
| **xenophobia**             | 0.9673            | 0.0732               | 0.9777     | |

#### Comments

- [1] The question that originated features `is_targeted` and `targeted_type` are optional, it must be marked only if the text is targeted. Looks like the annotator 126 didn't understand it and marked everything as targeted.
- [2] We don't have any text tagged with `religious_intolerance` by our annotators.
- [3] We have more inconsistent annotations in labels `idelogy`, `insult`, and `profanity_obscene` (disconsidering [1] [2])

#### Conclusions

We had a misunderstanding of the annotation guidelines by one of the annotators, which resulted in inconsistency in the `is_targeted` and `targeted_type` labels.

Regarding toxicity labels, we noticed that there are rare cases in which all annotators agree with the annotation, leading to a high rate of disagreement and consequently to a low value of Krippendorff's alpha. The labels with the highest disagreement are `insult`, `ideology` and `profanity_obscene`.

We will pass along the annotation guidelines with the annotators for the next iteration.

<details><summary>Profiling Report</summary>

<iframe width=100% height=500 frameBorder=0 src="../reports/olidbr_pilot_2.html"></iframe>

</details>

## Iteration 3

[![Status badge](https://img.shields.io/badge/Status-In%20Progress-yellow.svg)](https://shields.io/)

In the third iteration, we retrained the annotators using the output of the previous iteration. One of the annotators was replaced. The annotators were requested to label more 3,000 comments.

### Inter-Rater Reliability

As described in the [**Inter-Rater Reliability**](inter-rater-reliability.en.md) section, we evaluate the reliability of the annotators using a several coefficients.

We also address the analysis considering as a multi-label problem or several binary problems.

**Multi-Label Problem**

For all our [**toxicity labels**]{health, ideology, insult, lgbtqphobia, other_lifestyle, physical_aspects, profanity_obscene, racism, religious_intolerance, sexism, xenophobia} we calculate the Krippendorff's alpha (using the MASI distance) and the Percent Agreement.

- **Krippendorff's alpha**: 0.4387 (moderate agreement)
- **Percent Agreement**: 0.2843

**Binary Problem**

| Feature / metrics          | Percent Agreement | Krippendorff's alpha | Gwet's AC<sub>1</sub> | Comments |
| -------------------------- | :---------------: | :------------------: | :--------: | -------- |
| **is\_offensive**          | 0.7137            | 0.2064               | 0.7487     | |
| **is\_targeted**           | 0.4397            | 0.1415               | 0.3389     | |
| **targeted\_type**         | 0.2611            | 0.5031               | 0.6303     | |
| **toxic\_spans**           | 0.1830            | 0.4958               | N/A        | |
| **health**                 | 0.9703            | 0.1847               | 0.9797     | |
| **ideology**               | 0.8620            | 0.4265               | 0.8904     | |
| **insult**                 | 0.5685            | 0.3355               | 0.4929     | |
| **lgbtqphobia**            | 0.9683            | 0.7329               | 0.9770     | |
| **other\_lifestyle**       | 0.9724            | 0.2612               | 0.9811     | |
| **physical\_aspects**      | 0.9387            | 0.3605               | 0.9563     | |
| **profanity\_obscene**     | 0.7290            | 0.5087               | 0.7144     | |
| **racism**                 | 0.9908            | 0.3049               | 0.9938     | |
| **religious\_intolerance** | 1.0               | 1.0                  | 1.0        | |
| **sexism**                 | 0.9591            | 0.1531               | 0.9718     | |
| **xenophobia**             | 0.9734            | 0.3571               | 0.9818     | |

#### Comments

Pending

#### Conclusions

Pending

<details><summary>Profiling Report</summary>

<iframe width=100% height=500 frameBorder=0 src="../reports/olidbr_pilot_3.html"></iframe>

</details>
