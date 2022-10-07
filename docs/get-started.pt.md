---
title: Get Started
summary: Como usar o conjunto de dados OLID-BR.
---

O dataset está disponível no Kaggle e no Hugging Face.

## Kaggle

Você pode ver o conjunto de dados em [OLID-BR | Kaggle](https://www.kaggle.com/datasets/dougtrajano/olidbr).

O código abaixo mostra como baixar o conjunto de dados usando a API Kaggle.

```python
from kaggle.api.kaggle_api_extended import KaggleApi

kaggle = KaggleApi()
kaggle.authenticate()
kaggle.dataset_download_files(dataset="olidbr", unzip=True)
```

## Hugging Face

Você pode ver o dataset OLID-BR em [dougtrajano/olid-br · Datasets at Hugging Face](https://huggingface.co/datasets/dougtrajano/olid-br).

```python
# pending
```

## Arquivos do conjunto de dados

O conjunto de dados é composto pelos seguintes arquivos:

- `train.csv`: contém o treinamento.
- `test.csv`: contém os dados de teste.
- `train_metadata.csv`: contém os metadados dos dados de treinamento.
- `test_metadata.csv`: contém os metadados dos dados de teste.
- `train.json`: contém os dados de treinamento no formato JSON.
- `test.json`: contém os dados de teste no formato JSON.
- `additional_data.json`: contém dados adicionais no formato JSON. Esses dados não foram usados na criação do conjunto de dados.

`train.csv` e `test.csv` seguem a atribuição de rótulo descrita na seção [**Label Assignment**](#label-assignment).

Os arquivos JSON (`train.json`, `test.json` e `additional_data.json`) contêm todas as três anotações e os metadados de cada instância.

Hugging Face tem apenas os arquivos train (`train.csv`) e test (`test.csv`).

### Formato de dados

#### CSV

Os arquivos **CSV** são codificados em UTF-8 e possuem as seguintes colunas:

- `id`: identificador único da instância.
- `text`: texto da instância.
- `is_offensive`: rótulo binário que indica se o texto é ofensivo ou não.
- `is_targeted`: rótulo binário que indica se o texto é direcionado a uma pessoa ou não.
- `targeted_type`: Tipo de alvo (individual, group, or other). Aplicável apenas se `is_targeted` for `True`.
- `toxic_spans`: Lista de spans tóxicos.
- `health`: rótulo binário que indica se o texto possui ou não conteúdo tóxico relacionado à saúde.
- `ideology`: rótulo binário que indica se o texto possui ou não conteúdo tóxico relacionado à ideologia.
- `insult`: rótulo binário que indica se o texto possui ou não conteúdo tóxico relacionado a insultos.
- `lgbtqphobia`: rótulo binário que indica se o texto possui ou não conteúdo tóxico relacionado à LGBTQ+phobia.
- `other_lifestyle`: rótulo binário que indica se o texto possui ou não conteúdo tóxico relacionado a diferentes estilos de vida.
- `physical_aspects`: rótulo binário que indica se o texto possui ou não conteúdo tóxico relacionado a aspectos físicos.
- `profanity_obscene`: rótulo binário que indica se o texto possui ou não palavrões ou conteúdo obsceno.
- `racism`: rótulo binário que indica se o texto possui ou não conteúdo tóxico relacionado à raça ou etnia.
- `religious_intolerance`: rótulo binário que indica se o texto possui ou não intolerância religiosa.
- `sexism`: rótulo binário que indica se o texto possui ou não conteúdo tóxico relacionado a discriminação de gênero.
- `xenophobia`: rótulo binário que indica se o texto possui ou não conteúdo tóxico relacionado à xenofobia.

Os arquivos CSV seguem nossa estratégia de atribuição de rótulos conforme descrito abaixo.

- `is_offensive`: voto majoritário.
- `is_targeted`: voto majoritário.
- `targeted_type`: voto majoritário.
- `toxic_spans`: todos os *spans* rotulados.
- `health`: pelo menos um.
- `ideology`: pelo menos um.
- `insult`: pelo menos um.
- `lgbtqphobia`: pelo menos um.
- `other_lifestyle`: pelo menos um.
- `physical_aspects`: pelo menos um.
- `profanity_obscene`: pelo menos um.
- `racism`: pelo menos um.
- `religious_intolerance`: pelo menos um.
- `sexism`: pelo menos um.
- `xenophobia`: pelo menos um.

#### JSON

Os arquivos **JSON** são codificados em UTF-8 e possuem o seguinte esquema:

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

## Metadados

Nós forneceremos alguns metadados do dataset para auxiliar em futuras análises.

### Anotadores

Para cada anotador qualificado, nós coletamos as seguintes informações:

- `annotator_id` O ID do anotador.
- `gender` O gênero do anotador.
    - Male
    - Female
    - Other
- `year_of_birth` O ano de nascimento do anotador.
- `education_level` O nível de educação do anotador.
    - Primary School
    - Secondary School
    - Bachelor's Degree
    - Master's Degree
    - Doctoral Degree
- `annotator_ type` O tipo do anotador.
    - Volunteer
    - Researcher
    - Contract Worker
- `background` A área de estudo do anotador.
    - Computer Science
    - Social Science

Essas informações podem ser usadas para ajudar a entender o perfil dos anotadores, mantendo a anonimidade dos mesmos.

### Comentários

Para cada comentário, coletamos informações contextuais baseadas nas postagens em redes sociais.

- `source` A rede social ou dataset onde o comentário foi coletado.
- `created_at` A data e hora da postagem do comentário.
- `collected_at` A data e hora da coleta do comentário.
- `toxicity_score` A pontuação de toxicidade do comentário.