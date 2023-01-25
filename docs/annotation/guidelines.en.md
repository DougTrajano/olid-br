---
title: Annotation Guidelines
summary: The guidelines followed by our annotators in the OLID-BR dataset.
---

# Annotation Guidelines

On this page, we will detail the guidelines followed by our annotators in the data labeling process in the OLID-BR.

In the figure below, you can see the annotation schema for the OLID-BR dataset.

<figure>
  <img src="../images/olid-br-taxonomy.png"/>
  <figcaption>Hierarchical taxonomy for categorizing offensive language, proposed by author.</figcaption>
</figure>

## What task are you doing?

You will see comments with offensive/toxic content and you will need to answer some questions about that, these questions will help us identify offensive comments and/or better understand the behavior of *haters*.

In the image below, you can see an example of the labeling interface that our annotators will see.

<figure>
  <img src="../images/label_studio.png"/>
  <figcaption>Labeling Interface - Label Studio</figcaption>
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
    - Me desculpem gente mulher nenhuma é Feliz com esse corpo? Ela precisa de tratamento isso é uma doença
    - rt USER esse curso eh coisa de gente retardada mental vsf q porra
    - USER IMBECIL PROMOVENDO A AGLOMERAÇÃO DO POVO USER E A PROPAGAÇÃO DA DOENÇA. QUANTA USER !!!!!!!!!!!!!!!!!!!!!
    - parece legenda pra cego surdo e mudo

??? abstract "Ideology"

    Hate speech based on ideologies such as feminist, political left, etc.

    Examples:

    - esse partido chamado P T e esse P Sol sao uma doenca pra nossa nacao um enfermo
    - USER A Folha desde sempre apoiando a DITADURA e apoiando FASCISTAS que até se esquece de falar sobre seus ESCÂNDALOS como EMPRESTAR CARROS para a DITADURA ir TORTURAR PESSOAS. A Folha GOLPISTA nunca faz uma “autocrítica” URL
    - USER Aqui na minha família fechado com o MITO PT LADRÃO NUNCA VOLTAMOS NESSA RAÇA IMUNDA FDP DE LADRÕES ✅🇧🇷🇧🇷 URL
    - USER USER USER O Bolsonaro é corrupto mlk, para de ser retardado, seu cérebro tá atrofiando
    - A juiza é pilantra igual a Sergio USER quer impor a lei da mordaça ameaçando e obrigado o rél o expresidente Lula a ficar calado Armação geral do judiciario partidario de Curitiba de Sergio USER
    - Bolsonaro: “Como é duro ser patrão no Brasil". 19 milhões de brasileiros passam fome e a grande preocupação do cretino é com os patrões.

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

    - Que vergonha esse pais só tem gay
    - USER voce so gosta d sapatao caminhoeira de cabelo rapado
    - USER baitola lixo
    - USER USER lamentável acredita que existe pessoas que apóia o LGBT
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
    - USER USER seu cérebro derreteu por causa da maconha?????????
    - Como ser feminista: Ser feia e gorda Pagar peitinho em passeata Ser peluda Odiar homens E achar q isso fará diferença
    - Aula de como comer um maconheiro! Hahaha
    - Ai aonde a tua maconha te levou KKKkKkkK

??? abstract "Physical Aspects"

    Hate speech based on physical characteristics such as fatphobia, size, etc.

    Examples:

    - Próximo major já sabem, galera: caçar o gordo e extermina-lo.
    - Deveriam ter escolhido uma modelo menos gordinha, ela parece que não está passando fome !! 
    - USER pode achar seu principe encantado,mas sempre vai acabar: Gorda,feia,virgem,cheia de poster de crepúsculo a parede!!
    - Me desculpem gente mulher nenhuma é Feliz com esse corpo? Ela precisa de tratamento isso é uma doença
    - USER nao é gorda nao,USER esta obesa.vai se tratar é o melhor que USER faz.
    - RT USER: e olha pra cara gorda e feia de Isabelle .. sem contar da voz irritante dela URL
    - A obesidade está acabando com essa mulher. Ridícula
    - EU NÃO AGUENTO MAIS ESSE ALEIJADO SEM UMA PERNA DO CARALHO VAI TOMAR NO CU, O MALUCO NN SABE ANDAR COM A PERNA DIREITA FUDIDO HORRÍVEL URL
    
??? abstract "Profanity/Obscene"
    
    Hate speech has obscene, vulgar, pornographic, etc.

    Examples:

    - USER Comer cu de curioso
    - USER Mas que grande fdp.
    - USER Passar porte de vacina é o meu pau
    - USER Cada filho da puta que apertou 17 tem as mas sujas de sangue
    - USER Com a PF na tua casa tu ficou bravinho né vagabundo?
    - USER Toma no cu é vitamina como tu e tua prima.
    - fudeu minha mãe acabou de chegar em casa e eu acabei de acordar tomei no cu

??? abstract "Racism"

    The comment is biased or discriminatory based on the race, color or ethnicity of a person or group of people.

    Examples:

    - Essas filhas de pedreiro africano e foda
    - Não tenho tv colorida pra ficar olhando essa preta nao
    - USER E quantos desses negros são inocentes e quantos são criminosos e bandidos? Te dou absoluta certeza que a maioria dos negros mortos não são inocentes, infelizmente muitas vezes inocentes acabam sendo mortos pela corrupção na polícia
    - USER Sai macaco
    - Essa nega do cão quer ser a dona da razão e da situação smp 😂😂😂

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
    - Homem é um bicho estranho ao mesmo tmp ridículo 🤣
    - Resumindo" Meteu gostoso na safada" fim da historia!
    - Não tem dinheiro q essa mulher,ela é terrível não vai ter homem q a suporte
    - Dá uma rola pras feminazi.quem sabe elas param de falar bosta.

??? abstract "Xenophobia"

    Hate speech against foreigners or people from other cultures.

    Examples:

    - Quem liga pra judeu kkkk
    - odeio goiano e mineiro
    - rt USER USER nao sei . pra mim todo japones que é comunista é burro... uma coisa q meu pai ensinou kk
    - esse chinezinho falsificado e um pilantra. Não se deixa enganar como ele enganou os que votaram nele. Esse tipo de jumento só se elege uma vez.
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
