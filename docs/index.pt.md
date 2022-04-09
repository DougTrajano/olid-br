---
title: Overview
summary: Offensive Language Identification Dataset for Brazilian Portuguese.
---

# OLID-BR

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

[^1]: Zampieri et al. "Predicting the type and target of offensive posts in social media." NAACL 2019.
[^2]: João A. Leite, Diego F. Silva, Kalina Bontcheva, Carolina Scarton (2020): Toxic Language Detection in Social Media for Brazilian Portuguese: New Dataset and Multilingual Analysis. Published at AACL-IJCNLP 2020.
