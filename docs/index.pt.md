---
title: Overview
summary: Offensive Language Identification Dataset for Brazilian Portuguese.
---

# OLID-BR

O Offensive Language Identification Dataset for Brazilian Portuguese (OLID-BR) é um conjunto de dados com anotações multiplas tarefas para a detecção de linguagem ofensiva.

A versão atual (v1.0) contém **7.943** comentários de diferentes fontes, incluindo mídias sociais (YouTube e Twitter) e conjuntos de dados relacionados.

OLID-BR contém uma coleção de comentários em Português do Brasil anotados que abrangem os seguintes níveis:

- [[Offensive content detection](#offensive-content-detection)]{Detect offensive content in sentences and categorize it.|top-right}
- [[Offense target identification](#offense-target-identification)]{Detect if an offensive sentence is targeted to a person or group of people.|top-right}
- [[Offensive spans identification](#offensive-spans-identification)]{Detect curse words in sentences.|top-right}

<figure>
  <img src="images/olid-br-taxonomy.png"/>
  <figcaption>Taxonomia hierárquica para categorizar linguagem ofensiva, proposta pelo autor.</figcaption>
</figure>

## Categorização

### Offensive content detection

Este nível é usado para detectar conteúdo ofensivo em uma frase.

#### Este texto é ofensivo?

Nós utilizamos a [[Perspective API](https://www.perspectiveapi.com/)]{A Perspective API é o produto de um esforço de pesquisa colaborativo da Jigsaw e da equipe de tecnologia de combate ao abuso do Google.|top-right} para detectar se um comentário é ofensivo ou não. Adicionalmente, nossos anotadores reclassificaram comentários identificados como ofensivos incorretamente.

- `OFF`: O comentário é ofensivo.
- `NOT`: O comentário não é ofensivo.

#### Qual tipo de ofensa o texto contém?

Os rótulos abaixo foram anotados pelos nossos anotadores.

`Health`, `Ideology`, `Insult`, `LGBTQphobia`, `Other-Lifestyle`, `Physical Aspects`, `Profanity/Obscene`, `Racism`, `Religious Intolerance`, `Sexism` e `Xenophobia`.

Veja [Glossary](glossary.pt.md) para maiores informações.

### Offense target identification

Este nível é usado para detectar se um comentário ofensivo é direcionado a um indivíduo, grupo de pessoas ou outros.

#### Este comentário ofensivo é direcionado a alguém?

- `TIN`: O comentário é direcionado a um indivíduo, grupo de pessoas ou outros.
- `UNT`: O comentário não é direcionado.

#### Qual o alvo do comentário ofensivo?

- `IND`: O comentário é direcionado a um indivíduo. Também conhecido como *Cyberbullying*.
- `GRP`: O comentário é direcionado a um grupo de pessoas. Também conhecido como *Hate Speech*.
- `OTH`: O comentário é direcionado a outras categorias, como uma organização, um evento, etc.

### Offensive spans identification

Os *toxic spans* fornecem uma lista com os caracteres de um determinado comentário que são considerados ofensivos.

Por exemplo, vamos considerar o comentário:

> "USER `Canalha` URL"

Os toxic spans são:

```python
[5, 6, 7, 8, 9, 10, 11, 12, 13]
```

## Estrutura do conjunto de dados

### Instâncias de dados

Cada instância é um comentário de mídia social com um ID e anotações correspondentes para todas as tarefas descritas abaixo.

### Campos de dados

A configuração simplificada inclui:

- `id`: ID do comentário.
- `texto`: Texto do comentário.
- `is_offensive`: Se o comentário é ofensivo ou não.
- `is_targeted`: Se o comentário é direcionado ou não.
- `targeted_type`: Tipo do alvo (individual, grupo ou outro). Disponível apenas se `is_targeted` for `True`.
- `toxic_spans`: Lista de spans tóxicos.
- `saúde`: se o comentário contém toxicidade relacionada à saúde.
- `ideologia`: se o comentário contém toxicidade relacionada à ideologia.
- `insult`: se o comentário contém toxicidade relacionada ao insulto.
- `lgbtqphobia`: Se o comentário contém toxicidade relacionada à lgbtqphobia.
- `other_lifestyle`: se o comentário contém toxicidade relacionada a other_lifestyle.
- `physical_aspects`: se o comentário contém toxicidade relacionada a physical_aspects.
- `profanity_obscene`: se o comentário contém toxicidade relacionada a palavrões.
- `racism`: se o comentário contém toxicidade relacionada ao racismo.
- `religious_intolerance`: se o comentário contém toxicidade relacionada à religião.
- `sexism`: se o comentário contém toxicidade relacionada ao sexismo.
- `xenofobia`: se o comentário contém toxicidade relacionada à xenofobia.

Consulte a página [**Get Started**](get-started.en.md) para obter mais informações.

## Considerações para usar os dados

### Impacto social do conjunto de dados

A detecção de toxicidade é um valioso problema para ser estudado que pode garantir um ambiente online mais seguro para todos.

No entanto, os algoritmos de detecção de toxicidade têm se concentrado no inglês e não consideram as especificidades de outros idiomas.

Isso é um problema porque a toxicidade de um comentário pode ser diferente em diferentes idiomas.

Além disso, os algoritmos de detecção de toxicidade focam na classificação binária de um comentário como tóxico ou não tóxico.

Portanto, acreditamos que o conjunto de dados OLID-BR pode ajudar a melhorar o desempenho dos algoritmos de detecção de toxicidade em português brasileiro.

### Discussão de preconceitos

Estamos cientes de que o conjunto de dados contém vieses e não é representativo da diversidade global.

Estamos cientes de que a linguagem usada no conjunto de dados pode não representar a linguagem usada em diferentes contextos.

Possíveis vieses nos dados incluem: Preconceitos inerentes nas mídias sociais e vieses da base de usuários, as listas de palavras ofensivas/vulgares usadas para filtragem de dados e vieses inerentes ou inconscientes na avaliação de rótulos de identidade ofensivos.

Tudo isso provavelmente afeta a rotulagem, a precisão e a recuperação de um modelo treinado.

## Citação

Pending

## Referências

O conjunto de dados OLID-BR é baseado no conjunto de dados OLID proposto por Zampieri et al. (2019)[^1] e outros trabalhos relacionados.

[^1]: Zampieri et al. "Predicting the type and target of offensive posts in social media." NAACL 2019.
[^2]: João A. Leite, Diego F. Silva, Kalina Bontcheva, Carolina Scarton (2020): Toxic Language Detection in Social Media for Brazilian Portuguese: New Dataset and Multilingual Analysis. Published at AACL-IJCNLP 2020.
[^3]: S. Malmasi, "Offensive Language Identification Dataset - OLID", Scholar.harvard.edu, 2021. [Online]. Available: https://scholar.harvard.edu/malmasi/olid. [Accessed: 28- Aug- 2021].
[^4]: Weng, L. (2021, March 21). Reducing toxicity in language models. Lil'Log. https://lilianweng.github.io/lil-log/2021/03/21/reducing-toxicity-in-language-models.html.
