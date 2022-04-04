# Annotation

This section describes the [**data annotation process**]{Data annotation is the categorization and labeling of data for AI applications,.} and the [annotators guidelines](#annotators-guidelines) for the dataset.

## Annotation Process

We use [qualified annotators](#who-are-qualified-annotators) to annotate the dataset. The annotators are trained by the authors of the dataset.

### Inter-annotator agreement

The inter-annotator agreement varies depending on the task. Basically, each comment will be tagged by two judges, if they disagree, a third annotator will be used to decide the annotation.

We will provide the Kappa statistic that measures the agreement between the annotators.

## Who are qualified annotators?

A qualified annotator must have the following attributes:
 
- **Basic English** as it has the language used in the annotation tool.
- **Native Portuguese** as the texts presented in the dataset are in Brazilian Portuguese.
- A good understanding of offensive language (in Portuguese) and how to detect it. The concepts will be explained below.

Note takers will be trained by the course [Comunicação Não Violenta - FECAP](https://www.fecap.br/curta-duracao/comunicacao-nao-violenta-1/) with the following syllabus:

- Differences between negativity and toxicity in communication and behavior;
- Toxic people and behavior;
- Assertive behavior and communication;
- Non-violent communication, awareness and non-judgment.

## Annotation Guidelines

Annotators must follow the following guidelines:

---

Hi! Welcome to the Offensive Language Annotation Project in Brazilian Portuguese.

Warning! You will see several offensive comments, be aware that they are not directed to you. Avoid spending too many consecutive hours doing this work, your health first, okay? ❤

Before starting, let's align some concepts.

### What's the task you are doing?

You must annotate/labeling offensive comments. The information you provide will be used to help identify offensive comments and/or better understand *haters* behavior.

### What questions should you answer?

For each comment, you must answer the following questions:

#### Is this text toxic? (Yes/No)

Is the comment offensive? By default the system will pre-select it as "Yes", if the comment is not offensive, mark it as "No".

#### Which kind of toxicity it has?

What kind of toxicity does the comment have? Respond with one of the options below:

##### Health

Hate speech based on health conditions, such as against disabled people, against the elderly people (ageism), etc.

##### Ideology

Hate speech based on a person's ideas, such as feminist or left wing ideology.

##### Insult

The comment has an insult, insult, name calling, etc. for the purpose of humiliating or hitting a victim's weak point.

##### LGBTQphobia

Negative or hateful comments targeting someone because of their gender identity, sexual orientation. 

It includes aphobia, biphobia, homophobia, lesbophobia, transphobia, and other sexuality-related phobias.

> Be careful to don't confuse it with [sexism](#sexism).

##### Other-Lifestyle

Hate speech based on life habits, such as vegetarian, vegan, etc.

##### Physical Aspects

Hate speech based on physical aspects, such as fat, thin, tail or short people, etc.

##### Profanity/Obscene

The comment has obscene, vulgar, pornographic, etc.

##### Racism

The comment is prejudiced or discriminatory based on the race, color or ethnicity of a person or group of people.

##### Religious Intolerance

The comment is prejudiced or discriminatory based on the religion, cult or religious practice of a person or group of people.

##### Sexism

The comment is prejudiced or discriminatory based on the gender of a person or group of people.

##### Xenophobia

The comment is prejudiced or discriminatory towards people who are foreigners or from other cultures.

#### There's a specific target?

This question seeks to identify whether the toxic comment is directed at an individual, a group, or others.

Check only if there is a clear target for the toxic comment.

#### What words are offensive/toxic?

What words are offensive or toxic? Mark words in the text that are profane, insulting, or toxic.

*curse words* are words or set of words that will be profane/insulting.

Example:

- Will take it in c@, your arr0mb@d0

In the comment above, we have two *curse words* that must be marked: `will take no c@` and `arr0mb@d0`.

Another example:

"Que exemplo idiota! Você é burro demais."

In the comment above, the word `idiota` and `burro` are examples of *curse words*.

*curse words* are also considered a set of words, for example: `go to shit`.

### Frequently Asked Questions

#### Difference between a negative opinion and a toxic comment

It's important to understand the difference between a negative opinion and a toxic comment.

A **negative opinion** is a text that exposes an unpleasant opinion or fact in harsh words, usually criticizing someone's work or action, but without hurting the dignity or honor of a person or group.

Examples:

- USER Agora é " estupro" mesmo com a mulher dizendo que quis e gostou. Eu avisei que esse dia ia chegar.
- Moro conseguiu o que queria: eleger Bolsonaro em troca de um ministério. O que aconteceu depois foi "briga de quadrilha", na opinião do advogado Kakay. Por tudo isso, ele considera o ex-juiz "a própria fake news". Veja na última HASHTAG do ano! HASHTAG URL
- USER Crime é invadir a casa dos outros.
- USER Você não é homem de assumir teu erro, perder faz parte do esporte. Agora insultar e trazer o racismo pra nossas vidas não, eu não estou de acordo. EU NÃO TE RESPEITO

A **toxic comment** goes beyond freedom of expression, usually contains offensive or insulting words. It seeks to denigrate the dignity or honor of a person or group.

Examples:

- O presidente da empresa USER é um idiota e não entende o que é importante para a empresa.
- Esse cara não sabe jogar pqp

#### Misspellings and ways to avoid detection of toxicity

Users may mistype words or substitute characters to avoid detection of toxicity. In this case, you should interpret them as normal words, but they won't be corrected.

You should follow through with the tags in the same way, capturing the words as if they were correct.

#### The text is ilegible, what should I do?

If the text is ilegible or the anonimization process removed context of the text, you can click on the "Skip" button to skip the comment.

Exemplo:

- USER HASHTAG
- USER f
- 💐💐💐 URL

#### Can I review an labeled comment?

It's not possible to review a comment that has been labeled.

---

If you have any questions, you can contact Douglas Trajano.