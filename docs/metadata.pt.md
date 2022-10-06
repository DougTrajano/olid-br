# Metadados

Nós forneceremos alguns metadados do dataset para auxiliar em futuras análises.

## Anotadores

Para cada anotador qualificado, nós coletamos as seguintes informações:

- `annotator_id` O ID do anotador.
- `gender` O gênero do anotador.
    - Male
    - Female
    - Other
- `year_of_birth` O ano de nascimento do anotador.
- `education_level` O nível de educação do anotador.
    - Primary School
    - Secondary School
    - Bachelor's degree
    - Master's degree
    - Doctoral degree
- `annotator_ type` O tipo do anotador.
    - Volunteer
    - Researcher
    - Contract Worker

Essas informações podem ser usadas para ajudar a entender o perfil dos anotadores, mantendo a anonimidade dos mesmos.

## Comentários

Para cada comentário, coletamos informações contextuais baseadas nas postagens em redes sociais.

- `source` A rede social ou dataset onde o comentário foi coletado.
- `created_at` A data e hora da postagem do comentário.
- `collected_at` A data e hora da coleta do comentário.
- `toxicity_score` A pontuação de toxicidade do comentário.