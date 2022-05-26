---
title: Annotation Overview
summary: An overview about the annotation process used in the OLID-BR dataset.
---

# Annotation Overview

In this section, we will describe in detail the [**annotation process**]{Data annotation is the categorization and labeling of data for AI applications.} developed for the OLID-BR dataset.

## What is data labeling?

Data labeling, or data annotation, is the process of identifying raw data (images, text files, videos, etc.) when developing a machine learning (ML) model. It requires the identification of raw data with one or more meaningful and informative labels that provides context so that a machine learning model can learn from it. For example, labels might indicate whether a photo contains a bird or car, which words were uttered in an audio recording, or if an x-ray contains a tumor. Data labeling is required for a variety of use cases including computer vision, natural language processing, and speech recognition.[^1][^2]

## Data labeling approaches

The literature presents several approaches to data labeling. In the OLID-BR project, we used the following approach:

- **Internal labeling**: Using in-house data science experts simplifies tracking, provides greater accuracy, and increases quality. However, this approach typically requires more time and favors large companies with extensive resources.
- **Outsourcing**: This can be an optimal choice for high-level temporary projects, but developing and managing a freelance-oriented workflow can also be time-consuming. Though freelancing platforms provide comprehensive candidate information to ease the vetting process, hiring managed data labeling teams provides pre-vetted staff and pre-built data labeling tools.

In the first iteration of the annotation process, we will use the **internal labeling** approach, in other words, the author of the dataset labeled the data. We also had a volunteer who helped us label the data.

In the next iterations, we will use the **outsourcing** approach, three contract workers will label the data.

[^1]: [What is data labeling? - AWS](https://aws.amazon.com/sagemaker/data-labeling/what-is-data-labeling/)

[^2]: [What is data labeling? - IBM](https://www.ibm.com/cloud/learn/data-labeling)
