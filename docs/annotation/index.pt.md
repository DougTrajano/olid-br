---
title: Visão geral da anotação
summary: Uma visão geral sobre o processo de anotação utilizado no conjunto de dados OLID-BR.
---

# Visão geral da anotação

Nesta seção, descreveremos em detalhes o [**processo de anotação**]{A anotação de dados é a categorização e rotulagem de dados para aplicativos de IA.} desenvolvido para o conjunto de dados OLID-BR.

## O que é rotulagem de dados?

A rotulagem de dados, ou anotação de dados, é o processo de identificação de dados brutos (imagens, arquivos de texto, vídeos etc.) ao desenvolver um modelo de aprendizado de máquina (ML). Requer a identificação de dados brutos com um ou mais rótulos significativos e informativos que forneçam contexto para que um modelo de aprendizado de máquina possa aprender com ele. Por exemplo, os rótulos podem indicar se uma foto contém um pássaro ou um carro, quais palavras foram pronunciadas em uma gravação de áudio ou se um raio-x contém um tumor. A rotulagem de dados é necessária para vários casos de uso, incluindo visão computacional, processamento de linguagem natural e reconhecimento de fala.[^1][^2]

## Abordagens de rotulagem de dados

A literatura apresenta várias abordagens para rotulagem de dados. No projeto OLID-BR, usamos a seguinte abordagem:

- ***Internal labeling***: o uso de especialistas internos em ciência de dados simplifica o rastreamento, oferece maior precisão e aumenta a qualidade. No entanto, essa abordagem normalmente requer mais tempo e favorece grandes empresas com recursos extensos.
- ***Terceirização***: Esta pode ser a escolha ideal para projetos temporários de alto nível, mas desenvolver e gerenciar um fluxo de trabalho orientado a freelance também pode ser demorado. Embora as plataformas de freelancers forneçam informações abrangentes sobre os candidatos para facilitar o processo de verificação, a contratação de equipes de rotulagem de dados gerenciadas fornece uma equipe pré-avaliada e ferramentas de rotulagem de dados pré-criadas.

Na primeira iteração do processo de anotação, usaremos a abordagem ***internal labeling**, ou seja, o autor do conjunto de dados anotou os dados. Também tivemos um voluntário que nos ajudou a rotular os dados.

Nas próximas iterações, usaremos a abordagem de ***outsourcing***, três trabalhadores contratados rotularão os dados.

[^1]: [O que é rotulagem de dados? - AWS](https://aws.amazon.com/sagemaker/data-labeling/what-is-data-labeling/)

[^2]: [O que é rotulagem de dados? - IBM](https://www.ibm.com/cloud/learn/data-labeling)