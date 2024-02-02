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
df_filtered = df.loc[["matches", "goalsScored", "goalsConceded", "assists", "penaltyGoals", "averageBallPossession"]]

st.title(time_selected.upper())
st.subheader(f"Campeonato Brasileirão {year_selected} serie A")
st.divider()

col1, col2, col3, col4 = st.columns(4)
col5, col6, col7 = st.columns(3)

if year_selected == "2023":
    col1.metric(label="Partidas",      value=f"{df_filtered[year_selected]['matches']:.0f}")
    col2.metric(label="Gols marcados", value=f"{df_filtered[year_selected]['goalsScored']:.0f}")
    col3.metric(label="Gols sofridos", value=f"{df_filtered[year_selected]['goalsConceded']:.0f}")
    col4.metric(label="Assistências",  value=df_filtered[year_selected]["assists"])

    ppj = df_filtered[year_selected]["goalsScored"] / df_filtered[year_selected]["matches"]
    col5.metric(label="Posse de bola", value=f"{df_filtered[year_selected]['averageBallPossession']:.1f}%")
    col6.metric(label="Pontos por jogo", value=f"{ppj:.1f}")
    col7.metric(label="Gols de penalty", value=f"{df_filtered[year_selected]['penaltyGoals']:.0f}")

    

