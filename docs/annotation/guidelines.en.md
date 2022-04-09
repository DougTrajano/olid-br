# Annotation Guidelines

On this page, we will detail the guidelines followed by our annotators in the data labeling process in the OLID-BR.

## What task are you doing?

You will see comments with offensive/toxic content and you will need to answer some questions about that, these questions will help us identify offensive comments and/or better understand the behavior of *haters*.

In the image below, you can see an example of the annotation screen viewed by the annotator.

<figure>
  <img src="../images/label_studio.png"/>
  <figcaption>Annotation - Label Studio</figcaption>
</figure>

## What questions should you answer?

For each comment, you must answer the following questions:

### Is this text toxic?

The first question identifies if a given text contains toxic language or not.

It's comes pre-filled with "Yes", because the comment was filtered by a text classifier previously.

You action is to evaluate if the text is really toxic, if not, you can choose the option "No".

When selecting the "No" option, the next questions will be hidden.

### Which kind of toxicity it has?

In this question, we will try to identify the toxicity type within some pre-defined categories.

You can see the categories, their definitions and examples of comments that have each one of them in the blocks below.

??? abstract "Health"

    Offensive comment based on health, physical disabilities, age discrimination, characteristics caused by illness, etc.

    Examples:

    - USER velho broxa
    - USER Igualzinho a você, usa uma massa por fora pra esconder que por dentro é frango.
    - Ela tá dando vários surtos, amo que seja cancelada. Não aguento mais o povo forçando essa aleijada

??? abstract "Ideology"

    Hate speech based on ideologies such as feminist, political left, etc.

    Examples:

    - Bolsonaro: “Como é duro ser patrão no Brasil". 19 milhões de brasileiros passam fome e a grande preocupação do cretino é com os patrões.
    - USER Um governo de Evangelicos. Um governo de Corruptos. Um governo de Criminosos. Um governo de Irresponsaveis. Um governo de Bandidos. Um governo de Psicopatas.

??? abstract "Insult"

    Hate speech that contains insult, injury, swearing. Its purpose is to ignite an argument, irritate a party, hit a victim's weak point, etc.

    Examples:

    - USER USER Fodase denovo tmc para de aoarecer pra min desgraça
    - USER Kkkkkkkk é mesmo q ano de bosta vai toma no c uuuuuuuu
    - USER Você é um lixo!
    - USER Depois que acaba os campeonatos VC vem falar em liberar público nos estádios seu bosta calca apertada

??? abstract "LGBTQphobia"
    
    Hate speech based on gender identity or sexual orientation.

    The comment attacks sexual orientation or gender identity.

    It includes aphobia, biphobia, homophobia, lesbophobia, transphobia and other phobias related to sexuality.

    !!! warning

        Be careful to don't confuse it with sexism.

    Examples:

    - USER O problema não é sexualidade e sim competência. É diferente ferrar só um rabo ou ferrar de milhares.
    - USER E quando não consegue espaço e relevância no meio, mente que é bi.
    - USER Você é uma vergonha para os gays pq tu é um gay ladrão de dinheiro da Pandemia.
    
??? abstract "Other-Lifestyle"

    Hate speech based on lifestyle habits such as vegetarian, vegan, smoker, etc.

    Examples:

    - Povo da ração com milho he he
    - Povinho irritante e desinformado esses veganos chatos. Com certeza nao convencem nem suas familias.
    - USER crackudo voz de fumante
    - Coisa brega esse piercing no nariz. Muito feio para uma jornalista.

??? abstract "Physical Aspects"

    Hate speech based on physical characteristics such as fatphobia, size, etc.

    Examples:

    - Próximo major já sabem, galera: caçar o gordo e extermina-lo.
    - Deveriam ter escolhido uma modelo menos gordinha, ela parece que não está passando fome !!
    
??? abstract "Profanity/Obscene"
    
    Hate speech has obscene, vulgar, pornographic, etc.

    Examples:

    - USER Comer cu de curioso
    - USER Mas que grande fdp.
    - USER Passar porte de vacina é o meu pau
    - USER Cada filho da puta que apertou 17 tem as mas sujas de sangue
    - USER Com a PF na tua casa tu ficou bravinho né vagabundo?

??? abstract "Racism"

    The comment is biased or discriminatory based on the race, color or ethnicity of a person or group of people.

    Examples:

    - Essas filhas de pedreiro africano e foda
    - Não tenho tv colorida pra ficar olhando essa preta nao

??? abstract "Religious Intolerance"

    The comment is biased or discriminatory based on religion, cult or religious practice.

    Examples:

    - USER Um governo de Evangelicos. Um governo de Corruptos. Um governo de Criminosos.
    - Uma macumbeira a menos
    - Que diabo de Ogum, por isso que não vai pra frente

??? abstract "Sexism"

    The comment is biased or discriminatory based on the gender or sex of a person or group of people.

    Examples:

    - Se eu fosse o Temer criava o Ministério da Cozinha e da Limpeza e colocava uma mulher, só pro pessoal chorar menos. hahahaha
    - USER Uma calcinha dessa fio-dental dentro da bunda não tem que resistir uma tentação dessa?

??? abstract "Xenophobia"

    Hate speech against foreigners or people from other cultures.

    Examples:

    - USER O brasileiro merece o que tá passando povo ignorante e sem a menor consciência bando de fudido do caralho
    - USER USER PUTAQUEPARIUUUUUU........ESSAS PORCARIAS SÓ ACONTECE NO BRASIL.... RAÇA MALDITA ESSES BRASILEIROS....EXTINÇAO
    - Nordestino é uma desgraça cambada de demônio

### There's a specific target?

In this question, we want to know if the toxic comment is targeted or not, and if it is, the type of target.

!!! info "Important"

    Check only if there is a clear target for the toxic comment.

Options:

- **Individual**: The comment is targeted to a specific person.
- **Group**: The comment is targeted to a group of people.
- **Other**: The comment is targeted, but it is not targeted to a specific person or group of people.
    - e.g. companies, events, etc.

### Which words make this text toxic/offensive?

The toxic spans are the parts of the text that are identified as offensive, profane, insulting, etc.

Example:

- Vai tomar no c@, seu arr0mb@d0

In the above example, we have two toxic spans: `vai tomar no c@` e `arr0mb@d0`.

Another example:

- "Que exemplo idiota! Você é burro demais."

In this example, the words `idiota` and `burro` are toxic spans.

We also consider set of words as toxic spans, for example: `vai a merda`.

!!! warning

    Don't select words that are too generic, like "que", "o", "a", etc.

## Frequently asked questions

### What's the difference between a toxic comment and a negative opinion?

It's important to understand the difference between a negative opinion and a toxic comment.

A **negative opinion** is a text that exposes an unpleasant opinion or fact with uncomfortable words, usually criticizing someone's work or action, but without hurting the dignity or honor of a person or group.

Examples:

- USER Agora é "estupro" mesmo com a mulher dizendo que quis e gostou. Eu avisei que esse dia ia chegar.
- Moro conseguiu o que queria: eleger Bolsonaro em troca de um ministério. O que aconteceu depois foi "briga de quadrilha", na opinião do advogado Kakay. Por tudo isso, ele considera o ex-juiz "a própria fake news". Veja na última HASHTAG do ano! HASHTAG URL
- USER Crime é invadir a casa dos outros.
- USER perder faz parte do esporte. Agora insultar e trazer o racismo pra nossas vidas não, eu não estou de acordo.

A **toxic comment** goes beyond freedom of expression, usually contains offensive or insulting words. It seeks to denigrate the dignity or honor of a person or group.

Examples:

- O presidente da empresa USER é um idiota e não entende o que é importante para a empresa.
- Como se dá mídia pra um safado desses...merece cadeia... A mulher estava vuneravel...em surto... Ficam dando cartaz pra esse canalha... que mundo é esse?????
- Esse cara não sabe jogar pqp

### Should we consider misspellings words as toxic?

Users may misspell words or change some characters to avoid toxicity detection systems. In this case, you must interpret the words as if they were spelled correctly.

Examples:

- arr0mb@d0 > arrombado
- vai tomar no c@ > vai tomar no cu

About the *toxic spans*, you should mark the words in the same way, as if they were spelled correctly.

### The text is unreadable, what should I do?

If you cannot understand the text, you can click the **Skip** button and go to the next comment.

### Can I go back to the previous comment?

It's not possible to go back during the annotation task, but it's possible to filter comments in the table present in the project page. If you are in doubt, ask for help.

Be careful when submitting a comment if you are not sure, click the "Skip" button when in doubt.
