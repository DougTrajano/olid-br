---
title: Diretrizes de anotação
summary: As diretrizes de anotação são um conjunto de regras e convenções que são utilizadas para a anotação de dados.
---

# Diretrizes de anotação

Nessa página detalhamos as diretrizes seguidas pelos anotadores durante o processo de anotação dos textos presentes no OLID-BR.

Na figura abaixo, você pode ver o esquema de anotação para o conjunto de dados OLID-BR.

<figure>
  <img src="../images/olid-br-taxonomy.png"/>
  <figcaption>Taxonomia hierárquica para categorizar linguagem ofensiva, proposta pelo autor.</figcaption>
</figure>

## Qual a tarefa que você está fazendo?

Você visualizará comentários com conteúdo ofensivo/tóxico e precisará responder algumas perguntas sobre isso, essas perguntas ajudarão a identificar comentários ofensivos e/ou entender melhor o comportamento dos *haters*.

Na imagem abaixo, você pode ver um exemplo da tela de anotação visualizada pelo anotador.

<figure>
  <img src="../images/label_studio.png"/>
  <figcaption>Annotation - Label Studio</figcaption>
</figure>

## Quais perguntas você deverá responder?

Para cada comentário, você deve responder as seguintes perguntas:

### Is this text toxic?

A primeira pergunta identifica se o texto é ofensivo ou não. Ela já vem preenchida como "Yes", visto que o comentário foi pré-filtrado por um classificador de textos ofensivos.

Avalie se o texto é de fato ofensivo, caso contrário, escolha a opção "No".

Ao selecionar a opção "No", as perguntas seguintes não serão exibidas.

### Which kind of toxicity it has?

Essa pergunta procura identificar o(s) tipo(s) de toxicidade que o comentário possui dentro de algumas categorias pré-definidas.

Abaixo é possível ver as categorias, suas definições e exemplos de comentários que possuem cada uma dessas categorias.

??? abstract "Health"

    Comentário ofensivo com base na saúde, deficiências físicas, discriminação por idade, características causadas por doenças, etc.

    Exemplos:

    - USER velho broxa
    - Me desculpem gente mulher nenhuma é Feliz com esse corpo? Ela precisa de tratamento isso é uma doença
    - rt USER esse curso eh coisa de gente retardada mental vsf q porra
    - USER IMBECIL PROMOVENDO A AGLOMERAÇÃO DO POVO USER E A PROPAGAÇÃO DA DOENÇA. QUANTA USER !!!!!!!!!!!!!!!!!!!!!
    - parece legenda pra cego surdo e mudo

??? abstract "Ideology"

    Discurso de ódio com base nas ideologias, como feminista, esquerda política, etc.

    Exemplos:

    - esse partido chamado P T e esse P Sol sao uma doenca pra nossa nacao um enfermo
    - USER A Folha desde sempre apoiando a DITADURA e apoiando FASCISTAS que até se esquece de falar sobre seus ESCÂNDALOS como EMPRESTAR CARROS para a DITADURA ir TORTURAR PESSOAS. A Folha GOLPISTA nunca faz uma “autocrítica” URL
    - USER Aqui na minha família fechado com o MITO PT LADRÃO NUNCA VOLTAMOS NESSA RAÇA IMUNDA FDP DE LADRÕES ✅🇧🇷🇧🇷 URL
    - USER USER USER O Bolsonaro é corrupto mlk, para de ser retardado, seu cérebro tá atrofiando
    - A juiza é pilantra igual a Sergio USER quer impor a lei da mordaça ameaçando e obrigado o rél o expresidente Lula a ficar calado Armação geral do judiciario partidario de Curitiba de Sergio USER
    - Bolsonaro: “Como é duro ser patrão no Brasil". 19 milhões de brasileiros passam fome e a grande preocupação do cretino é com os patrões.

??? abstract "Insult"

    Discurso de ódio que possui insulto, injúria, xingamento. Tem o objetivo de inflamar uma discussão, irritar uma parte, atingir um ponto fraco da vítima, etc.

    Exemplos:

    - USER USER Fodase denovo tmc para de aoarecer pra min desgraça
    - USER Kkkkkkkk é mesmo q ano de bosta vai toma no c uuuuuuuu
    - USER Você é um lixo!
    - USER Depois que acaba os campeonatos VC vem falar em liberar público nos estádios seu bosta calca apertada

??? abstract "LGBTQphobia"

    Discurso de ódio com base na identidade de gênero ou orientação sexual. 

    O comentário possui ataque a orientação sexual ou a identidade de gênero.

    Inclui afobia, bifobia, homofobia, lesbofobia, transfobia e outras fobias relacionadas à sexualidade.

    !!! warning

        Cuidado para não confundir com sexismo.

    Exemplos:

    - Que vergonha esse pais só tem gay
    - USER voce so gosta d sapatao caminhoeira de cabelo rapado
    - USER baitola lixo
    - USER USER lamentável acredita que existe pessoas que apóia o LGBT
    - USER O problema não é sexualidade e sim competência. É diferente ferrar só um rabo ou ferrar de milhares.
    - USER E quando não consegue espaço e relevância no meio, mente que é bi.
    - USER Você é uma vergonha para os gays pq tu é um gay ladrão de dinheiro da Pandemia.
    
??? abstract "Other-Lifestyle"

    Discurso de ódio com base em hábitos de vida, como vegetariano, vegano, fumante, etc.

    Exemplos:

    - Povo da ração com milho he he
    - Povinho irritante e desinformado esses veganos chatos. Com certeza nao convencem nem suas familias.
    - USER crackudo voz de fumante
    - Coisa brega esse piercing no nariz. Muito feio para uma jornalista.
    - USER USER seu cérebro derreteu por causa da maconha?????????
    - Como ser feminista: Ser feia e gorda Pagar peitinho em passeata Ser peluda Odiar homens E achar q isso fará diferença
    - Aula de como comer um maconheiro! Hahaha
    - Ai aonde a tua maconha te levou KKKkKkkK

??? abstract "Physical Aspects"

    Discurso de ódio com base em características físicas, como gordofobia, tamanhismo, etc.

    Exemplos:

    - Próximo major já sabem, galera: caçar o gordo e extermina-lo.
    - Deveriam ter escolhido uma modelo menos gordinha, ela parece que não está passando fome !! 
    - USER pode achar seu principe encantado,mas sempre vai acabar: Gorda,feia,virgem,cheia de poster de crepúsculo a parede!!
    - Me desculpem gente mulher nenhuma é Feliz com esse corpo? Ela precisa de tratamento isso é uma doença
    - USER nao é gorda nao,USER esta obesa.vai se tratar é o melhor que USER faz.
    - RT USER: e olha pra cara gorda e feia de Isabelle .. sem contar da voz irritante dela URL
    - A obesidade está acabando com essa mulher. Ridícula
    - EU NÃO AGUENTO MAIS ESSE ALEIJADO SEM UMA PERNA DO CARALHO VAI TOMAR NO CU, O MALUCO NN SABE ANDAR COM A PERNA DIREITA FUDIDO HORRÍVEL URL

??? abstract "Profanity/Obscene"
    
    Discurso de ódio possui palavras obscenas, vulgar, pornográficas, etc.

    Exemplos:

    - USER Comer cu de curioso
    - USER Mas que grande fdp.
    - USER Passar porte de vacina é o meu pau
    - USER Cada filho da puta que apertou 17 tem as mas sujas de sangue
    - USER Com a PF na tua casa tu ficou bravinho né vagabundo?
    - USER Toma no cu é vitamina como tu e tua prima.
    - fudeu minha mãe acabou de chegar em casa e eu acabei de acordar tomei no cu

??? abstract "Racism"

    O comentário é preconceituoso ou discriminatório com base na raça, cor ou etnia de uma pessoa ou grupo de pessoas.

    Exemplos:

    - Essas filhas de pedreiro africano e foda
    - Não tenho tv colorida pra ficar olhando essa preta nao
    - USER E quantos desses negros são inocentes e quantos são criminosos e bandidos? Te dou absoluta certeza que a maioria dos negros mortos não são inocentes, infelizmente muitas vezes inocentes acabam sendo mortos pela corrupção na polícia
    - USER Sai macaco
    - Essa nega do cão quer ser a dona da razão e da situação smp 😂😂😂

??? abstract "Religious Intolerance"

    O comentário é preconceituoso ou discriminatório com base na religião, culto ou prática religiosa.

    Exemplos:

    - USER Um governo de Evangelicos. Um governo de Corruptos. Um governo de Criminosos.
    - Uma macumbeira a menos
    - Que diabo de Ogum, por isso que não vai pra frente

??? abstract "Sexism"

    O comentário é preconceituoso ou discriminatório com base no gênero ou sexo de uma pessoa ou grupo de pessoas.

    Exemplos:

    - Se eu fosse o Temer criava o Ministério da Cozinha e da Limpeza e colocava uma mulher, só pro pessoal chorar menos. hahahaha
    - USER Uma calcinha dessa fio-dental dentro da bunda não tem que resistir uma tentação dessa?
    - Homem é um bicho estranho ao mesmo tmp ridículo 🤣
    - Resumindo" Meteu gostoso na safada" fim da historia!
    - Não tem dinheiro q essa mulher,ela é terrível não vai ter homem q a suporte
    - Dá uma rola pras feminazi.quem sabe elas param de falar bosta.

??? abstract "Xenophobia"

    Discurso de ódio contra pessoas estrangeiras ou de outras culturas.

    Exemplos:

    - Quem liga pra judeu kkkk
    - odeio goiano e mineiro
    - rt USER USER nao sei . pra mim todo japones que é comunista é burro... uma coisa q meu pai ensinou kk
    - esse chinezinho falsificado e um pilantra. Não se deixa enganar como ele enganou os que votaram nele. Esse tipo de jumento só se elege uma vez.
    - USER O brasileiro merece o que tá passando povo ignorante e sem a menor consciência bando de fudido do caralho
    - USER USER PUTAQUEPARIUUUUUU........ESSAS PORCARIAS SÓ ACONTECE NO BRASIL.... RAÇA MALDITA ESSES BRASILEIROS....EXTINÇAO
    - Nordestino é uma desgraça cambada de demônio

### There's a specific target?

Essa pergunta procura identificar se o comentário tóxico é direcionado a um indivíduo, um grupo ou a outros.

Marque apenas se existir um alvo claro do comentário tóxico.

Opções:

- **Individual**: O comentário tóxico é direcionado a um indivíduo, uma pessoa específica.
- **Group**: O comentário tóxico é direcionado a um grupo, uma comunidade.
- **Other**: O comentário tóxico é direcionado, porém não a um indivíduo ou grupo específicos.
    - Ex.: empresas, eventos, natureza, etc.

### Which words make this text toxic/offensive?

Os *toxic spans* são os trechos do texto que são identificados como ofensivas, profanas, insultantes, etc.

Exemplo:

- Vai tomar no c@, seu arr0mb@d0

Na frase acima, temos dois grupos de *toxic spans* que devem ser marcados: `vai tomar no c@` e `arr0mb@d0`.

Um outro exemplo:

- "Que exemplo idiota! Você é burro demais."

Na frase acima, a palavra `idiota` e `burro` são exemplos de *toxic spans*.

Também são consideradas *toxic spans* conjunto de palavras, por exemplo: `vai a merda`.

!!! warning

    Não selecione palavras como "seu", "sua", "é", etc.

## Perguntas frequentes

### Diferença entre uma opinião negativa e um comentário tóxico

É importante entender a diferença entre uma opinião negativa e um comentário tóxico.

Uma **opinião negativa** é um texto que expõem uma opinião ou fato desagradável com duras palavras, normalmente criticam o trabalho ou ação de alguém, mas sem ferir a dignidade ou a honra de uma pessoa ou grupo.

Exemplos:

- USER Agora é "estupro" mesmo com a mulher dizendo que quis e gostou. Eu avisei que esse dia ia chegar.
- Moro conseguiu o que queria: eleger Bolsonaro em troca de um ministério. O que aconteceu depois foi "briga de quadrilha", na opinião do advogado Kakay. Por tudo isso, ele considera o ex-juiz "a própria fake news". Veja na última HASHTAG do ano! HASHTAG URL
- USER Crime é invadir a casa dos outros.
- USER perder faz parte do esporte. Agora insultar e trazer o racismo pra nossas vidas não, eu não estou de acordo.

Um **comentário tóxico** extrapola a liberdade de expressão, normalmente contém palavras ofensivas ou insultantes. Procura denegrir a dignidade ou a honra de uma pessoa ou grupo.

Exemplos:

- O presidente da empresa USER é um idiota e não entende o que é importante para a empresa.
- Como se dá mídia pra um safado desses...merece cadeia... A mulher estava vuneravel...em surto... Ficam dando cartaz pra esse canalha... que mundo é esse?????
- Esse cara não sabe jogar pqp

### Erros ortográficos e formas de evitar a detecção de toxicidade

Os usuários podem digitar palavras errôneamente ou substituir caracteres para evitar a detecção de toxicidade. Neste caso, você deve interpretar as palavras como se fossem escritas corretamente.

Exemplos:

- arr0mb@d0 > arrombado
- vai tomar no c@ > vai tomar no cu

Sobre os *toxic spans*, você deve seguir com a marcação da mesma forma, como se estivessem corretas.

### O texto é ilegível, o que fazer?

Se você não conseguir compreender o texto, você pode clicar no botão **Skip** e pular para o próximo texto.

### É possível voltar em um comentário já anotado?

Não é possível voltar durante o processo de anotação, mas é possível filtrá-lo na tabela inicial. Em caso de dúvidas, consulte a ajuda.

Tenha cuidado ao submeter um comentário caso não tenha certeza, na dúvida clique no botão "Skip".
