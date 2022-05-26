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

As described in the [**Inter-Rater Reliability**](inter-rater-reliability.en.md) section, we evaluate the reliability of the annotators using a set of metrics.

| Feature / metrics          | Percent Agreement | Krippendorff's alpha | Gwet's AC<sub>1</sub> | Comments |
| -------------------------- | :---------------: | :------------------: | :--------: | -------- |
| **is\_offensive**          | 0,7277            | 0,0595               | 0,7750     | |
| **is\_targeted**           | 0,1610            | \-0,1348             | \-0,1029   | [1] |
| **targeted\_type**         | 0,0641            | 0,2461               | 0,4978     | [1] |
| **health**                 | 0,9760            | 0,0447               | 0,9837     | |
| **ideology**               | 0,7647            | 0,3019               | 0,7976     | [3] |
| **insult**                 | 0,4713            | 0,0895               | 0,425      | [3] |
| **lgbtqphobia**            | 0,9453            | 0,5583               | 0,9603     | |
| **other\_lifestyle**       | 0,9860            | 0,0824               | 0,9906     | |
| **physical\_aspects**      | 0,9463            | 0,3272               | 0,9622     | |
| **profanity\_obscene**     | 0,6837            | 0,0850               | 0,726      | [3] |
| **racism**                 | 0,9750            | 0,2564               | 0,9829     | |
| **religious\_intolerance** | 1,0               | 1,0                  | 1,0        | [2] |
| **sexism**                 | 0,8753            | 0,1721               | 0,9076     | |
| **xenophobia**             | 0,9673            | 0,0732               | 0,9777     | |

#### Comments

- [1] The question that originated features `is_targeted` and `targeted_type` are optional, it must be marked only if the text is targeted. Looks like the annotator 126 didn't understand it and marked everything as targeted.
- [2] We don't have any text tagged with `religious_intolerance` by our annotators.
- [3] We have more inconsistent annotations in labels `idelogy`, `insult`, and `profanity_obscene` (disconsidering [1] [2])

#### Conclusions

The Agreement Analysis shows that we have more inconsistent annotations in labels `is_targeted`, `targeted_type`, and `insult`. We also have some misunderstandings in the annotation guidelines by one of our annotators, we will ensure that the guidelines are followed by our annotators in the next phase. For other labels, we have more consistent annotations which means that the process to train the annotators is crucial to ensure the quality of the annotations.

Average without `is_targeted` and `targeted_type` due an inconsistent annotation by one annotator.

- Percent Agreement: 0.9458
- Krippendorff's alpha: 0.1308
- Gwet's AC<sub>1</sub>: 0.9613

<details><summary>Profiling Report</summary>

<iframe width=100% height=500 frameBorder=0 src="../reports/olidbr_pilot_2.html"></iframe>

</details>

## Iteration 3

[![Status badge](https://img.shields.io/badge/Status-In%20Progress-yellow.svg)](https://shields.io/)

In the third iteration, our goal was retrain the annotators based on the output of the previous iteration. We also replaced one of the contract worker. The annotators were requested to label more 3,000 comments.
