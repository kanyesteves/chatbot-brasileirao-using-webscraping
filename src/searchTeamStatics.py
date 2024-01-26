import pandas as pd
import requests


class SearchTeamStatics:
    def __init__(self):
        self.teams_address_A = {
            'palmeiras': 'palmeiras/1963',
            'gremio': 'gremio/5926',
            'atletico-mineiro': 'atletico-mineiro/1977',
            'flamengo': 'flamengo/5981',
            'botafogo': 'botafogo/1958',
            'red-bull-bragantino': 'red-bull-bragantino/1999',
            'fluminense': 'fluminense/1961',
            'athletico': 'athletico/1967',
            'internacional': 'internacional/1966',
            'fortaleza': 'fortaleza/2020',
            'sao-paulo': 'sao-paulo/1981',
            'cuiaba': 'cuiaba/49202',
            'corinthians': 'corinthians/1957',
            'cruzeiro': 'cruzeiro/1954',
            'vasco': 'vasco/1974',
            'bahia': 'bahia/1955',
            'santos': 'santos/1968',
            'goias/1960': 'goias/1960',
            'coritiba': 'coritiba/1982',
            'america-mineiro': 'america-mineiro/1973',
        }
        self.browsers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        self.base_api = 'https://api.sofascore.com/api/v1/team/'
        self.end_api = '/statistics/overall'

    def choose_team(self, time:str):
        self.data_list = []
        self.count_url_list = 0
        self.count_data_list = 0

        serie = '325'
        id_time = self.teams_address_A[time.lower()][-4:]
        endpoint_23 = '48982'
        middle_api = f'/unique-tournament/{serie}/season/'

        url_23 = self.base_api + id_time + middle_api + endpoint_23 + self.end_api

        url_list = [url_23]
        for url in url_list:
            api_link = requests.get(url, headers=self.browsers).json()
            if not 'error' in api_link:
                self.data_list.append(api_link['statistics'])

                if url_list.index(url_list[self.count_url_list]) == 0:
                    self.data_list[self.count_data_list]['ano'] = 2023

                self.count_data_list +=1
            self.count_url_list +=1
        
        return self.data_list
    
    def build_dataframe(self, time:str):
        team = self.choose_team(time.lower())
        team_df = pd.DataFrame(index=team[0].keys())

        for i in range(len(team)):
            team_df[str(team[i]['ano'])] = team[i].values()

        return team_df