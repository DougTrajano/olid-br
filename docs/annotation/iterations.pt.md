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

[![Status badge](https://img.shields.io/badge/Status-Finished-blue.svg)](https://shields.io/)

Na segunda iteração, introduzimos trabalhadores contratados para fazer as anotações. Os anotadores foram treinados pelo autor do conjunto de dados conforme descrito em [**Anotadores qualificados**](qualified-annotators.en.md).

### Confiabilidade entre avaliadores

Conforme descrito na seção [**Inter-Rater Reliability**](inter-rater-reliability.en.md), avaliamos a confiabilidade dos anotadores usando diferentes coeficientes.

Também abordamos a análise considerando como um problema *multi-label* ou vários problemas binários.

**Problem *Multi-Label***

Para todos os nossos [**rótulos de toxicidade**]{health, ideology, insult, lgbtqphobia, other_lifestyle, physical_aspects, profanity_obscene, racism, religious_intolerance, sexism, xenophobia} calculamos o Krippendorff's alpha (usando MASI distance) e o *Percent Agreement*.

- **Krippendorff's alpha**: 0,1962 (pequena concordância)
- **Percent Agreement**: 0,1877

**Problema binário**

| Feature / metrics          | Percent Agreement | Krippendorff's alpha | Gwet's AC<sub>1</sub> | Comments |
| -------------------------- | :---------------: | :------------------: | :--------: | -------- |
| **is\_offensive**          | 0,7277            | 0,0595               | 0,7750     | |
| **is\_targeted**           | 0,1610            | \-0,1348             | \-0,1029   | [1] |
| **targeted\_type**         | 0,0641            | 0,2461               | 0,4978     | [1] |
| **toxic\_spans**           | 0,1220            | 0,2709               | N/A        | |
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

Tivemos um mal entendimento das diretrizes de anotação por um dos anotadores, o que acabou gerando inconsistência nos rótulos `is_targeted` e `targeted_type`.

Sobre os rótulos de toxicidade (*toxicity labels*), percebemos que são raros os casos em que todos os anotadores concordam com a anotação, levando a um alto índice de discordância e consequentemente a um baixo valor de Krippendorff's alpha. Os rótulos que apresentaram maior discordância são `insult`, `ideology` e `profanity_obscene`.

Iremos repassar as diretrizes de anotação com os anotadores para a próxima iteração.

<details><summary>Profiling Report</summary>

<iframe width=100% height=500 frameBorder=0 src="../reports/olidbr_pilot_2.html"></iframe>

</details>

## Iteração 3

[![Status badge](https://img.shields.io/badge/Status-Finished-blue.svg)](https://shields.io/)

Na terceira iteração, nós retreinamos os anotadores com base nas lições aprendidas na iteração anterior. Também substituímos um dos anotadores contratados. Os anotadores foram solicitados a rotular mais 3.000 comentários.

### Inter-Rater Reliability

Como descrito na seção [**Inter-Rater Reliability**](inter-rater-reliability.pt.md), avaliamos a confiabilidade dos anotadores usando diferentes coeficientes.

Para avaliar os rótulos de toxicidade, temos duas possíveis abordagens: Multi-Label ou Binary.

**Multi-Label Problem**

Para todos os nossos [**rótulos de toxicidade**]{health, ideology, insult, lgbtqphobia, other_lifestyle, physical_aspects, profanity_obscene, racism, religious_intolerance, sexism, xenophobia} calculamos o Krippendorff's alpha (usando MASI distance) e o *Percent Agreement*.

- **Krippendorff's alpha**: 0,4653 (concordância moderada)
- **Percent Agreement**: 0,2758

**Binary Problem**

| Feature / metrics          | Percent Agreement | Krippendorff's alpha | Gwet's AC<sub>1</sub> | Comments |
| -------------------------- | :---------------: | :------------------: | :--------: | -------- |
| **is\_offensive**          | 0.6509            | 0.1777               | 0.6754     | |
| **is\_targeted**           | 0.3551            | 0.1072               | 0.1709     | |
| **targeted\_type**         | 0.1975            | 0.4887               | 0.6300     | |
| **toxic\_spans**           | 0.1757            | 0.4427               | N/A        | |
| **health**                 | 0.9700            | 0.2641               | 0.9794     | |
| **ideology**               | 0.8670            | 0.4728               | 0.8934     | |
| **insult**                 | 0.5488            | 0.3317               | 0.4531     | |
| **lgbtqphobia**            | 0.9613            | 0.6393               | 0.9722     | |
| **other\_lifestyle**       | 0.9787            | 0.4683               | 0.9854     | |
| **physical\_aspects**      | 0.9560            | 0.4160               | 0.9691     | |
| **profanity\_obscene**     | 0.7089            | 0.4894               | 0.6870     | |
| **racism**                 | 0.9913            | 0.3781               | 0.9942     | |
| **religious\_intolerance** | 1.0               | 1.0                  | 1.0        | 1 |
| **sexism**                 | 0.9550            | 0.1566               | 0.9689     | |
| **xenophobia**             | 0.9847            | 0.2980               | 0.9896     | |

#### Comentários

- [1] Não temos nenhum texto marcado com `religious_intolerance` por nossos anotadores.

#### Conclusões

In this iteration, we had more consistent annotations which led to a better agreement between the annotators. Krippendorff's alpha for toxicity labels increased from **0.1962** to **0.4653**.

Nesta iteração, tivemos anotações mais consistentes que levaram a uma melhor concordância entre os anotadores. O Krippendorff's alpha para rótulos de toxicidade aumentou de **0,1962** para **0,4653**.

<details><summary>Profiling Report</summary>

<iframe width=100% height=500 frameBorder=0 src="../reports/olidbr_pilot_3.html"></iframe>

</details>

## Iteração 4

[![Status badge](https://img.shields.io/badge/Status-Finished-blue.svg)](https://shields.io/)

Na quarta iteração, solicitamos aos anotadores que rotulassem um número maior de textos seguindo as mesmas diretrizes das iterações anteriores. Fixamos o prazo para 4 de outubro de 2022 (+- um mês).

### Inter-Rater Reliability

Como descrito na seção [**Inter-Rater Reliability**](inter-rater-reliability.pt.md), avaliamos a confiabilidade dos anotadores usando diferentes coeficientes.

Para avaliar os rótulos de toxicidade, temos duas possíveis abordagens: Multi-Label ou Binary.

**Multi-Label Problem**

Para todos os nossos [**rótulos de toxicidade**]{health, ideology, insult, lgbtqphobia, other_lifestyle, physical_aspects, profanity_obscene, racism, religious_intolerance, sexism, xenophobia} calculamos o Krippendorff's alpha (usando MASI distance) e o *Percent Agreement*.

- **Krippendorff's alpha**: 0,4424 (concordância moderada)
- **Percent Agreement**: 0,2769

**Binary Problem**

| Feature / metrics          | Percent Agreement | Krippendorff's alpha | Gwet's AC<sub>1</sub> | Comments |
| -------------------------- | :---------------: | :--------------------: | :--------: | -------- |
| **is\_offensive**          | 0.5847            | 0.2174                 | 0.5716     | |
| **is\_targeted**           | 0.4253            | 0.1825                 | 0.2790     | |
| **targeted\_type**         | 0.2223            | 0.4840                 | 0.5756     | |
| **toxic\_spans**           | 0.2249            | 0.4760 (MASI distance) | N/A        | |
| **health**                 | 0.9800            | 0.1424                 | 0.9865     | |
| **ideology**               | 0.8531            | 0.2909                 | 0.8863     | |
| **insult**                 | 0.4938            | 0.2923                 | 0.3549     | |
| **lgbtqphobia**            | 0.9550            | 0.4901                 | 0.9681     | |
| **other\_lifestyle**       | 0.9705            | 0.2239                 | 0.9798     | |
| **physical\_aspects**      | 0.9570            | 0.3623                 | 0.9700     | |
| **profanity\_obscene**     | 0.7436            | 0.5530                 | 0.7233     | |
| **racism**                 | 0.9940            | 0.2481                 | 0.9960     | |
| **religious\_intolerance** | 1.0               | 1.0                    | 1.0        | 1 |
| **sexism**                 | 0.9640            | 0.1880                 | 0.9753     | |
| **xenophobia**             | 0.9905            | 0.3840                 | 0.9936     | |

#### Comentários

- [1] Não temos nenhum texto marcado com `religious_intolerance` por nossos anotadores.

#### Conclusões

Assim como na iteração anterior, tivemos anotações mais consistentes que levaram a uma melhor concordância entre os anotadores.

<details><summary>Profiling Report</summary>

<iframe width=100% height=500 frameBorder=0 src="../reports/olidbr_pilot_4.html"></iframe>

</details>
