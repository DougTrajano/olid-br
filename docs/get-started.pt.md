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

- `id` (string): Identificador único da instância.
- `text` (string): O texto da instância.
- `is_offensive` (string): Se o texto é ofensivo (`OFF`) ou não (`NOT`).
- `is_targeted` (string): Se o texto é direcionado (`TIN`) ou não direcionado (`UNT`).
- `targeted_type` (string): Tipo de destino (individual `IND`, grupo `GRP` ou outro `OTH`). Disponível apenas se `is_targeted` for `True`.
- `toxic_spans` (string): Lista de spans tóxicos.
- `saúde` (booleano): Se o texto contém discurso de ódio com base em condições de saúde, como deficiência, doença, etc.
- `ideologia` (boolean): Indica se o texto contém discurso de ódio baseado nas ideias ou crenças de uma pessoa.
- `insult` (boolean): se o texto contém conteúdo insultuoso, inflamatório ou provocativo.
- `lgbtqphobia` (booleano): se o texto contém conteúdo nocivo relacionado à identidade de gênero ou orientação sexual.
- `other_lifestyle` (boolean): Se o texto contém discurso de ódio relacionado a hábitos de vida (por exemplo, veganismo, vegetarianismo, etc.).
- `physical_aspects` (boolean): Se o texto contém discurso de ódio relacionado à aparência física.
- `profanity_obscene` (boolean): Se o texto contém palavrões ou conteúdo obsceno.
- `racism` (boolean): Se o texto contém pensamentos preconceituosos ou ações discriminatórias baseadas em diferenças de raça/etnia.
- `religious_intolerance` (boolean): Se o texto contém intolerância religiosa.
- `sexism` (booleano): se o texto contém conteúdo discriminatório com base em diferenças de sexo/gênero (por exemplo, sexismo, misoginia, etc.).
- `xenophobia` (boolean): Se o texto contém discurso de ódio contra estrangeiros.

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