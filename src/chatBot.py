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



        if message.lower() == "oi":
            bot.sendMessage(chat_id, 'Olá sou um chatbot que busca estatísticas de times de futebol da Serie A do Brasileirão de 2023. \n\n1- Ver todos os times.')

        if message == '1':
            bot.sendMessage(chat_id, 'Listando times da Seria A:')
            for time in time_statics.teams_address_A:
                bot.sendMessage(chat_id, f'{time}')
                times.append(time)
            
            bot.sendMessage(chat_id, '\n\n2- Selecione o seu time e verifique as estatísticas: ')

        if message.lower() == 'palmeiras':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'gremio':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'atletico-mineiro':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'flamengo':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'botafogo':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'red-bull-bragantino':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'fluminense':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'athletico':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'internacional':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'fortaleza':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'sao-paulo':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'cuiaba':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'corinthians':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'cruzeiro':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'vasco':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'bahia':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'santos':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'goias':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'coritiba':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')

        elif message.lower() == 'america-mineiro':
            statics = time_statics.choose_team(message)
            bot.sendMessage(chat_id, f'Estatísticas do {message}: TESTE')


bot = telepot.Bot(TOKEN)
bot.message_loop(init)

while True:
    pass