# Data Pipeline

Nessa página, nós vamos descrever a [**pipeline de dados**]{A data pipeline é uma série de processos de processamento de dados.} usados para gerar o dataset.

## Fonte de dados

Coletamos comentários de diferentes fontes, como [**Twitter**]{Twitter is a microblogging and social networking service.}, [**YouTube**]{YouTube is a video-sharing website.} e conjuntos de dados relacionados.

Para cada rede social (Twitter e YouTube), definimos um conjunto de perfis públicos que consideramos relevantes para o tema.

Além disso, usamos textos em Português do Brasil de outros conjuntos de dados, como:

- [rogersdepelle/OffComBR: Here we provide a data set of web comments which have been annotated for hate speech.](https://github.com/rogersdepelle/OffComBR)
- [paulafortuna/Portuguese-Hate-Speech-Dataset: A Hierarchically-Labeled Portuguese Hate Speech Dataset](https://github.com/paulafortuna/Portuguese-Hate-Speech-Dataset)
- [LaCAfe/Dataset-Hatespeech: Hate Speech Detection Dataset](https://github.com/LaCAfe/Dataset-Hatespeech)
- [JAugusto97/ToLD-Br: Toxic Language Detection in Social Media for Brazilian Portuguese: New Dataset and Multilingual Analysis](https://github.com/JAugusto97/ToLD-Br)

## Arquitetura

O seguinte diagrama mostra a arquitetura da [**pipeline de dados**]{A data pipeline é uma série de processos de processamento de dados.}.

<figure>
  <img src="images/data-pipeline.png"/>
  <figcaption>Arquitetura - Fonte: Elaborada pelo autor.</figcaption>
</figure>

## Filtragem

Nós queremos filtrar comentários que não sejam relevantes para o escopo do dataset. Para isso, definimos alguns critérios que cada comentário deve possuir.

- Comentários devem ser em português.
- Comentários devem ter um nível de toxicidade (medido pela Perspective API) maior que 0.5.

## Privacidade

Para garantir a privacidade dos usuários, nós aplicaremos algumas regras de anonimização dos dados diretamente na pipeline de dados.

- Usuários mencionados foram substituídos pelo texto "@USER".
- URLs foram substituídos pelo texto "URL".