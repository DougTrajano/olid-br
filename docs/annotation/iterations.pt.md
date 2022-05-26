---
title: Iterações de Anotação
summary: As iterações do processo de anotação do conjunto de dados OLID-BR.
---

# Iterações

Decidimos trabalhar em iterações porque nos permite validar e melhorar o processo de anotação e as diretrizes. Cada iteração tem suas próprias metas e objetivos.

## Iteração 1

[![Status badge](https://img.shields.io/badge/Status-Finished-blue.svg)](https://shields.io/)

Nesta iteração, nosso objetivo foi validar e refinar nosso processo de anotação. Foi a primeira vez que aplicamos o processo de anotação. Dois anotadores rotularam os dados. O primeiro anotador era um voluntário, o segundo era o autor do conjunto de dados. O voluntário forneceu feedbacks construtivos para ajustar o processo de anotação. Os dados rotulados pelo pesquisador predominaram sob os rótulos do voluntário, pois o pesquisador corrigiu alguns erros no processo de anotação.

### Confiabilidade entre avaliadores

Nesta iteração, não geramos a análise de confiabilidade entre avaliadores porque fizemos algumas alterações e alinhamentos durante a iteração.

<details><summary>Profiling Report</summary>

<iframe width=100% height=500 frameBorder=0 src="../reports/olidbr_pilot.html"></iframe>

</details>

## Iteração 2

[![Distintivo de status](https://img.shields.io/badge/Status-Finished-blue.svg)](https://shields.io/)

Na segunda iteração, introduzimos trabalhadores contratados para fazer as anotações. Os anotadores foram treinados pelo autor do conjunto de dados conforme descrito em [**Anotadores qualificados**](qualified-annotators.en.md).

### Confiabilidade entre avaliadores

Conforme descrito na seção [**Inter-Rater Reliability**](inter-rater-reliability.en.md), avaliamos a confiabilidade dos anotadores usando um conjunto de métricas.

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

#### Comentários

- [1] A pergunta que originou os recursos `is_targeted` e `targeted_type` são opcionais, devem ser marcadas somente se o texto for direcionado. Parece que o anotador 126 não entendeu e marcou tudo como direcionado.
- [2] Não temos nenhum texto marcado com `religious_intolerance` por nossos anotadores.
- [3] Temos anotações mais inconsistentes nos rótulos `idelogy`, `insult` e `profanity_obscene` (desconsiderando [1] [2])

#### Conclusões

A análise de acordo mostra que temos anotações mais inconsistentes nos rótulos `is_targeted`, `targeted_type` e `insult`. Também temos alguns equívocos nas diretrizes de anotação por um de nossos anotadores, garantiremos que as diretrizes sejam seguidas por nossos anotadores na próxima fase. Para outros rótulos, temos anotações mais consistentes, o que significa que o processo de treinamento dos anotadores é crucial para garantir a qualidade das anotações.

Média sem `is_targeted` e `targeted_type` devido a uma anotação inconsistente de um dos anotadores.

- Percent Agreement: 0.9458
- Krippendorff's alpha: 0.1308
- Gwet's AC<sub>1</sub>: 0.9613

<details><summary>Profiling Report</summary>

<iframe width=100% height=500 frameBorder=0 src="../reports/olidbr_pilot_2.html"></iframe>

</details>

## Iteração 3

[![Status badge](https://img.shields.io/badge/Status-In%20Progress-yellow.svg)](https://shields.io/)

Na terceira iteração, nosso objetivo foi treinar novamente os anotadores com base nas lições da iteração anterior. Também substituímos um dos trabalhadores contratados. Os anotadores foram solicitados a rotular mais 3.000 comentários.
