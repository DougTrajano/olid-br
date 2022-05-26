---
title: Esquema de Anotação
summary: O esquema de anotação para o conjunto de dados OLID-BR.
---

# Esquema de anotação

Desenvolvemos o esquema de anotação para maximizar a eficiência do anotador.

O OLID-BR contém uma coleção de frases anotadas em português brasileiro usando um modelo de anotação que abrange os seguintes níveis:

- [[Offensive content detection](#offensive-content-detection)]{Detectar conteúdo ofensivo em frases e categorizá-lo.|top-right}
- [[Offense target identification](#offense-target-identification)]{Detectar se uma frase ofensiva é alvo de uma pessoa ou grupo de pessoas.|top-right}
- [[Offensive spans identification](#offensive-spans-identification)]{Detectar palavras ou conjunto de palavras que são consideradas ofensivas em frases.|top-right}

<figure>
  <img src="../images/olid-br-taxonomy.png"/>
  <figcaption>Taxonomia hierárquica para categorizar linguagem ofensiva, proposta pelo autor.</figcaption>
</figure>

Para isso, definimos 4 perguntas que nossos [anotadores qualificados](qualified-annotators.pt.md) responderão a cada frase.

- Este texto é tóxico?
- Que tipo de toxicidade tem?
- Há um alvo específico?
- Quais palavras tornam este texto tóxico/ofensivo?

A imagem a seguir mostra a tela de anotação que nossos anotadores utilizarão.

<figure>
  <img src="../images/label_studio.png"/>
  <figcaption>Interface de rotulagem - Label Studio</figcaption>
</figure>
