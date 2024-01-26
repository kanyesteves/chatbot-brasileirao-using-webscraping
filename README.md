# Web Scraping com dashboard e chatboot

Esse projeto fiz com base no curso de `Web Scraping – Extraindo dados da web` da **Asimov Academy**.

## Objetivo

Buscar estatísticas de cada time da Seria A do Brasileirão.

## Dashboard
link do webapp: https://app-brasileirao.streamlit.app/

## Implemenação 

Esse projeto foi feito seguindo os conhecimentos obtidos nos projetos anteriores de web-scraping, mas de uma forma diferente de extrair os dados do site.
Em um projeto padrao de web-scraping você consegue entender como e feita a "raspagem" dos dados do site com a biblioteca beautifulsoup para tratar o html.
Mas como esse site ele e dinâmico e nao estático vamos usar a API que ele fornece para buscar esses dados la do proprio banco de dados do site.

**Url para a API:** https://api.sofascore.com/api/v1/team/
## Bibliotecas
- pandas
- requests
- telepot
- streamlit

## Colunas para apresentação do dataframe

1. matches - Partidas.
2. goalsScored - Gols marcados.
3. goalsConceded - Gols sofridos.
4. Assists - Assistências.
