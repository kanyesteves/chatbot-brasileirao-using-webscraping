import telepot
from searchTeamStatics import SearchTeamStatics

TOKEN = '6496122569:AAH-dKLOmI7dxoz6-URPI0DK1zMtgyXnUaU'

def init(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        chat_id = msg['chat']['id']
        message = msg['text']
        times = []
        time_statics = SearchTeamStatics()



        if message == "oi":
            bot.sendMessage(chat_id, 'Olá sou um chatbot que busca estatísticas de times de futebol da Serie A do Brasileirão de 2023. \n\n1- Ver todos os times.')

        if message == '1':
            bot.sendMessage(chat_id, 'Listando times da Seria A:')
            for time in time_statics.teams_address_A:
                bot.sendMessage(chat_id, f'{time}')
                times.append(time)
            
            bot.sendMessage(chat_id, '\n\n2- Selecione o seu time e verifique as estatísticas: ')

        if message == 'palmeiras':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'gremio':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'atletico-mineiro':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'flamengo':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'botafogo':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'red-bull-bragantino':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'fluminense':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'athletico':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'internacional':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'fortaleza':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'sao-paulo':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'cuiaba':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'corinthians':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'cruzeiro':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'vasco':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'bahia':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'santos':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'goias':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'coritiba':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message == 'america-mineiro':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')


bot = telepot.Bot(TOKEN)
bot.message_loop(init)

while True:
    pass