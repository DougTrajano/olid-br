# OLID-BR

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=DougTrajano_olid-br&metric=alert_status)](https://sonarcloud.io/dashboard?id=DougTrajano_olid-br)
[![](https://img.shields.io/github/license/DougTrajano/olid-br.svg)](LICENSE)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)

Offensive Language Identification Dataset for Brazilian Portuguese (OLID-BR) is a collection of Portuguese text with annotations for several NLP tasks related to toxicity/offensive language.

See the [Dataset documentation](https://dougtrajano.github.io/olid-br/) for more information.

## Technical details

This repository contains the source code to prepare, build, and publish the OLID-BR dataset.

The repository is structured as follows:

- `/docs` contains the documentation for the dataset (available [here](https://dougtrajano.github.io/olid-br/)).
- `/notebooks/baselines` contains notebooks for baseline models.
- `/notebooks/collecting` contains notebooks for data collection.
- `/notebooks/exploring` contains notebooks for data exploration.
- `/notebooks/processing` contains notebooks for data processing.
- `/properties` contains the properties for the dataset.
- `/src` contains the source code for the dataset.
- `/tests` contains the tests for the dataset.

<details><summary>Architecture</summary>
<p>

![](docs/images/data-pipeline.png)

</p>
</details>

### Running Notebooks

You must define the following environment variables to run the notebooks:

<details><summary>Environment Variables</summary>
<p>

| Variable | Description | Default | Required |
| --- | --- | --- | --- |
| `AWS_ACCESS_KEY_ID` | AWS Access Key ID | `None` | Optional |
| `AWS_S3_BUCKET_PREFIX` | AWS S3 Bucket Prefix | `None` | Required |
| `AWS_S3_BUCKET` | AWS S3 Bucket | `None` | Required |
| `AWS_SECRET_ACCESS_KEY` | AWS Secret Access Key | `None` | Optional |
| `FILTER_TOXIC_COMMENTS` | Filter Toxic Comments | `True` | Optional |
| `HUGGINGFACE_HUB_TOKEN` | HuggingFace Hub Token | `None` | Required |
| `KAGGLE_KEY` | Kaggle Key | `None` | Required |
| `KAGGLE_USERNAME` | Kaggle Username | `None` | Required |
| `LOG_LEVEL` | Log level | `INFO` | Optional |
| `PERSPECTIVE_API_KEY` | Perspective API Key | `None` | Required |
| `PERSPECTIVE_THRESHOLD` | Perspective Threshold | `0.5` | Optional |
| `TWITTER_ACCESS_TOKEN` | Twitter Access Token | `None` | Required |
| `TWITTER_ACCESS_TOKEN_SECRET` | Twitter Access Token Secret | `None` | Required |
| `TWITTER_CONSUMER_KEY` | Twitter Consumer Key | `None` | Required |
| `TWITTER_CONSUMER_SECRET` | Twitter Consumer Secret | `None` | Required |
| `TWITTER_MAX_TWEETS` | Twitter Max Tweets or replies | `None` | Required |
| `YOUTUBE_API_KEY` | YouTube API Key | `None` | Required | `YOUTUBE_MAX_COMMENTS` | YouTube Max Comments | 50 | Optional |
| `YOUTUBE_MAX_COMMENTS_PER_VIDEO` | YouTube Max Comments per video | `None` | Optional |

The Jupyter Notebooks uses a `.env` file to read the environment variables.

</p>
</details>

If you are running the notebooks on [Google Colab](https://colab.research.google.com/), you need to run the following commands:

```bash
!git clone https://github.com/DougTrajano/olid-br.git
!mv olid-br/* .
!rm -rf olid-br
!pip install -r requirements.txt
```

The Google Colab uses Python 3.7 which means that the `numpy`, `pandas`, and `scikit-learn` versions in the requirements.txt are not compatible, please update the requirements.txt file to the following versions:

```
numpy~=1.23.1
pandas~=1.3.5
scikit-learn~=1.0.2
```

### Install dependencies

You can install the dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Changelog

See the [GitHub Releases](https://github.com/DougTrajano/olid-br/releases) page for a history of notable changes to this project.

## License

The source code is licensed under the [Apache 2.0 License](LICENSE).

The dataset is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) (CC BY 4.0).
