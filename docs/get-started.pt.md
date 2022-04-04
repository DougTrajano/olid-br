## Usando OLID-BR

O dataset está disponível no Kaggle.

[Kaggle Datasets](https://www.kaggle.com/datasets){ .md-button }

## Exemplo de dados

A tabela abaixo mostra um exemplo dos dados fornecidos pelo dataset.

| id                               | text                                              | is\_offensive | is\_targeted | targeted\_type | toxic\_spans                                       | health | lgbtqphobia | ideology | insult | other\_lifestyle | physical\_aspects | profanity\_obscene | racism | religious\_intolerance | sexism | xenophobia |
| -------------------------------- | ------------------------------------------------- | ------------- | ------------ | -------------- | -------------------------------------------------- | ------ | -------------- | -------- | ------ | ---------------- | ----------------- | ------------------ | ------ | ---------------------- | ------ | ---------- |
| b1f25b94adda4724b587a9af556c0a3b | USER Canalha URL                                  | OFF           | TIN          | IND            | \[5, 6, 7, 8, 9, 10, 11, 12, 13\]                  | FALSE  | FALSE          | FALSE    | TRUE   | FALSE            | FALSE             | FALSE              | FALSE  | FALSE                  | FALSE  | FALSE      |
| 5102cdbdbefd4e4eb4dac40726093d66 | USER VTNSC FDP                                    | OFF           | TIN          | IND            | \[5, 6, 7, 8, 9, 10, 11, 12, 13, 14\]              | FALSE  | FALSE          | FALSE    | TRUE   | FALSE            | FALSE             | TRUE               | FALSE  | FALSE                  | FALSE  | FALSE      |
| 5676273151be40a4adb16b53a121c98d | USER O partido do Kim votou à favor do fundão.... | OFF           | TIN          | IND            | None                                               | FALSE  | FALSE          | FALSE    | TRUE   | FALSE            | FALSE             | FALSE              | FALSE  | FALSE                  | FALSE  | FALSE      |
| 28dc2bfddd9b4bef8b738363f0668886 | USER Grande homem. Em um país de covardes. Ete... | OFF           | TIN          | GRP            | \[34, 35, 36, 37, 38, 39, 40, 41, 42\]             | FALSE  | FALSE          | FALSE    | TRUE   | FALSE            | FALSE             | FALSE              | FALSE  | FALSE                  | FALSE  | FALSE      |
| 5f2974fa03e84b1bba817a8f1c7d619a | USER USER QAnon Brasil é um bicho estranho. Ob... | OFF           | TIN          | IND            | \[28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 3... | FALSE  | FALSE          | FALSE    | TRUE   | FALSE            | FALSE             | TRUE               | FALSE  | FALSE                  | FALSE  | FALSE      |