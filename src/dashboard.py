from searchTeamStatics import SearchTeamStatics
import streamlit as st
import pandas

######### Variáveis Globais #########
teams = SearchTeamStatics()
teams_list = teams.teams_address_A

######### SIDEBAR #########
st.sidebar.header("Filtros")
time_selected = st.sidebar.selectbox("Times", teams_list.keys())

######### BODY #########
df = teams.build_dataframe(time_selected)
year_selected = st.sidebar.selectbox("Ano", df.columns)

df_filtered = df.loc[["matches", "goalsScored", "goalsConceded", "assists"]]

st.title(time_selected.upper())

if year_selected == "Média": 
    st.subheader(f"Média dos campeonatos do Brasileirão seria A")
else:
    st.subheader(f"Resumo do campeonato Brasileirão {year_selected} serie A")

st.divider()

col1, col2, col3, col4 = st.columns(4)
col5, col6 = st.columns(2)

if year_selected == "2021":
    col1.metric(label="Partidas",      value=df_filtered[year_selected]["matches"])
    col2.metric(label="Assistências",  value=df_filtered[year_selected]["assists"])
    col3.metric(label="Gols marcados", value=df_filtered[year_selected]["goalsScored"])
    col4.metric(label="Gols sofridos", value=df_filtered[year_selected]["goalsConceded"])

elif year_selected == "2022":
    col1.metric(label="Partidas",      value=df_filtered[year_selected]["matches"])
    col2.metric(label="Assistências",  value=df_filtered[year_selected]["assists"])
    col3.metric(label="Gols marcados", value=df_filtered[year_selected]["goalsScored"])
    col4.metric(label="Gols sofridos", value=df_filtered[year_selected]["goalsConceded"])
    
elif year_selected == "Média":
    col1.metric(label="Partidas",      value=df_filtered[year_selected]["matches"])
    col2.metric(label="Assistências",  value=df_filtered[year_selected]["assists"])
    col3.metric(label="Gols marcados", value=df_filtered[year_selected]["goalsScored"])
    col4.metric(label="Gols sofridos", value=df_filtered[year_selected]["goalsConceded"])

    ppj = df_filtered[year_selected]["goalsScored"] / df_filtered[year_selected]["matches"]
    col5.metric(label="Pontos por jogo", value=f"{ppj:.0f}")

