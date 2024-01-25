from searchTeamStatics import SearchTeamStatics
import streamlit as st
import pandas

teams = SearchTeamStatics()

flamengo = teams.build_dataframe('Flamengo')

flamengo

