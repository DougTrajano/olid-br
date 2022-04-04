import pytest
from src.anonymize import Anonymizer

TESTS = [
    {
        "input": "Acabei de solicitar minha portabilidade para a @vivobr, @TIMBrasil acabou de perder um cliente #decepcao https://www.consumidor.gov.br/",
        "without_users": "Acabei de solicitar minha portabilidade para a USER, USER acabou de perder um cliente #decepcao https://www.consumidor.gov.br/",
        "without_urls": "Acabei de solicitar minha portabilidade para a @vivobr, @TIMBrasil acabou de perder um cliente #decepcao URL",
        "without_hashtags": "Acabei de solicitar minha portabilidade para a @vivobr, @TIMBrasil acabou de perder um cliente HASHTAG https://www.consumidor.gov.br/",
        "without_all": "Acabei de solicitar minha portabilidade para a USER, USER acabou de perder um cliente HASHTAG URL"
    },
    {
        "input": "@doug_trajano teste normal https://www.google.com.br",
        "without_users": "USER teste normal https://www.google.com.br",
        "without_urls": "@doug_trajano teste normal URL",
        "without_hashtags": "@doug_trajano teste normal https://www.google.com.br",
        "without_all": "USER teste normal URL"
    },
    {
        "input": "Siga nossos canais: Instagram @SunoNoticias e Telegram https://t.me/sunonoticias",
        "without_users": "Siga nossos canais: Instagram USER e Telegram https://t.me/sunonoticias",
        "without_urls": "Siga nossos canais: Instagram @SunoNoticias e Telegram URL",
        "without_hashtags": "Siga nossos canais: Instagram @SunoNoticias e Telegram https://t.me/sunonoticias",
        "without_all": "Siga nossos canais: Instagram USER e Telegram URL"
    },
    {
        "input": "Previsão é que vacinação de adolescentes seja retomada na quinta-feira https://glo.bo/3k4gXd5 #G1 #Vacina #RJ",
        "without_users": "Previsão é que vacinação de adolescentes seja retomada na quinta-feira https://glo.bo/3k4gXd5 #G1 #Vacina #RJ",
        "without_urls": "Previsão é que vacinação de adolescentes seja retomada na quinta-feira URL #G1 #Vacina #RJ",
        "without_hashtags": "Previsão é que vacinação de adolescentes seja retomada na quinta-feira https://glo.bo/3k4gXd5 HASHTAG HASHTAG HASHTAG",
        "without_all": "Previsão é que vacinação de adolescentes seja retomada na quinta-feira URL HASHTAG HASHTAG HASHTAG"
    },
    {
        "input": "Números foram divulgados nesta segunda, um dia após ação na Praia do Porto de Santo Antônio https://glo.bo/3lKJALM #g1 #Noronha #entulho",
        "without_users": "Números foram divulgados nesta segunda, um dia após ação na Praia do Porto de Santo Antônio https://glo.bo/3lKJALM #g1 #Noronha #entulho",
        "without_urls": "Números foram divulgados nesta segunda, um dia após ação na Praia do Porto de Santo Antônio URL #g1 #Noronha #entulho",
        "without_hashtags": "Números foram divulgados nesta segunda, um dia após ação na Praia do Porto de Santo Antônio https://glo.bo/3lKJALM HASHTAG HASHTAG HASHTAG",
        "without_all": "Números foram divulgados nesta segunda, um dia após ação na Praia do Porto de Santo Antônio URL HASHTAG HASHTAG HASHTAG"
    },
    {
        "input": "Cerimônia de Lançamento do Projeto Pró-Águas Urucuia. - Arinos/MG - 17 Set 21. @mdregional_br @rogeriosmarinho @govbr #brasil",
        "without_users": "Cerimônia de Lançamento do Projeto Pró-Águas Urucuia. - Arinos/MG - 17 Set 21. USER USER USER #brasil",
        "without_urls": "Cerimônia de Lançamento do Projeto Pró-Águas Urucuia. - Arinos/MG - 17 Set 21. @mdregional_br @rogeriosmarinho @govbr #brasil",
        "without_hashtags": "Cerimônia de Lançamento do Projeto Pró-Águas Urucuia. - Arinos/MG - 17 Set 21. @mdregional_br @rogeriosmarinho @govbr HASHTAG",
        "without_all": "Cerimônia de Lançamento do Projeto Pró-Águas Urucuia. - Arinos/MG - 17 Set 21. USER USER USER HASHTAG"
    },
    {
        "input": "O @minsaude assim investirá R$ 10,8 milhões no incentivo a gestores municipais com foco no atendimento de 32 milhões de adolescentes do Brasil, mesmo nos locais de mais difícil acesso! Mais informações no nosso telegram: https://t.me/jairbolsonarobrasil",
        "without_users": "O USER assim investirá R$ 10,8 milhões no incentivo a gestores municipais com foco no atendimento de 32 milhões de adolescentes do Brasil, mesmo nos locais de mais difícil acesso! Mais informações no nosso telegram: https://t.me/jairbolsonarobrasil",
        "without_urls": "O @minsaude assim investirá R$ 10,8 milhões no incentivo a gestores municipais com foco no atendimento de 32 milhões de adolescentes do Brasil, mesmo nos locais de mais difícil acesso! Mais informações no nosso telegram: URL",
        "without_hashtags": "O @minsaude assim investirá R$ 10,8 milhões no incentivo a gestores municipais com foco no atendimento de 32 milhões de adolescentes do Brasil, mesmo nos locais de mais difícil acesso! Mais informações no nosso telegram: https://t.me/jairbolsonarobrasil",
        "without_all": "O USER assim investirá R$ 10,8 milhões no incentivo a gestores municipais com foco no atendimento de 32 milhões de adolescentes do Brasil, mesmo nos locais de mais difícil acesso! Mais informações no nosso telegram: URL"
    }
]

@pytest.mark.parametrize("text, output", [(i["input"], i["without_users"]) for i in TESTS])
def test_remove_user(text: str, output: str):
    anonymizer = Anonymizer()
    assert anonymizer.remove_users(text) == output
    print(f"TEST OK for Anonymizer().remove_users - Input: {text} - Output: {output}")

@pytest.mark.parametrize("text, output", [(i["input"], i["without_urls"]) for i in TESTS])
def test_remove_urls(text: str, output: str):
    anonymizer = Anonymizer()
    assert anonymizer.remove_urls(text) == output
    print(f"TEST OK for Anonymizer().remove_urls - Input: {text} - Output: {output}")

@pytest.mark.parametrize("text, output", [(i["input"], i["without_hashtags"]) for i in TESTS])
def test_remove_hashtags(text: str, output: str):
    anonymizer = Anonymizer()
    assert anonymizer.remove_hashtags(text) == output
    print(f"TEST OK for Anonymizer().remove_hashtags - Input: {text} - Output: {output}")

@pytest.mark.parametrize("text, output", [(i["input"], i["without_all"]) for i in TESTS])
def test_apply_all(text: str, output: str):
    anonymizer = Anonymizer()
    assert anonymizer.apply_all(text) == output
    print(f"TEST OK for Anonymizer().apply_all - Input: {text} - Output: {output}")
