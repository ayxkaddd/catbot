import telebot
from colorama import init, Fore
import os
import random
from datetime import datetime

time = datetime.now()

init()


print(Fore.GREEN + 'Start')


token = '' # <---- token here

bot = telebot.TeleBot(token)


def save_file(text):
    f = open('logs/logs.txt', 'a')
    f.write(f'{text}')
    f.close()


@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.from_user.id, '/cat - кидает котенка\n/send_cat - ты можешь отправить котита мне дааа\n\
/meow - котик мяукает в гс\n/meme_from_2012 - кидает вам мемчик из 2012 что бы поднять настроение!')
    print(f'{message.from_user.username} использовал бота.')


@bot.message_handler(commands=['cat'])
def cat(message):
    print(f'UserID {message.from_user.id} | UserName {message.from_user.username}')
    photo = open('cute_cat/' + random.choice(os.listdir('cute_cat')), 'rb')
    fototootot = message.from_user.username, photo.name
    print(Fore.GREEN + f'{fototootot}')
    save_file(text=f'{message.from_user.username} получил {photo.name} использовав функцию cat.\n')
    bot.send_photo(message.from_user.id, photo, caption='мяяяуу')


@bot.message_handler(commands=['send_cat'])
def send_photo(message):
    print(f'UserID {message.from_user.id} | UserName {message.from_user.username}')
    print(f'{message.from_user.username} хочет фотку отправить???? пиздеееец')
    bot.send_message(message.from_user.id, 'аошвыраы короче отправь фотку кота да и я ее добавлю')


@bot.message_handler(commands=['meow'])
def meow(message):
    print(f'UserID {message.from_user.id} | UserName {message.from_user.username}')
    meow = open('meow/' + random.choice(os.listdir('meow')), 'rb')
    mememe = message.from_user.username, meow.name
    print(Fore.GREEN + f'{mememe}')
    save_file(text=f'{message.from_user.username} получил {meow.name} использовав функцию meow.\n')
    bot.send_voice(message.from_user.id, meow)
    meow.close()


@bot.message_handler(commands=['meme_from_2012'])
def meme(message):
    meme = open('meme/' + random.choice(os.listdir('meme')), 'rb')
    bot.send_photo(message.from_user.id, meme)
    save_file(text=f'{message.from_user.username} получил {meme.name} использовав функцию meme.\n')
    print(f'UserID {message.from_user.id} | UserName {message.from_user.username}')
    meme.close()


@bot.message_handler(content_types=['text'])
def main(message):

    text = f'[TIME] - {time} | [USERNAME] - {message.from_user.username} | [MESSAGE] - {message.text}'
    print(Fore.WHITE + '[username]:', Fore.RED + message.from_user.username, Fore.WHITE + '[message]:', Fore.RED + message.text)
    print(f'UserID {message.from_user.id} | UserName {message.from_user.username}')
    save_file(text=text + '\n')
    if message.text == 'мяукай':    
        meow = open('meow/' + random.choice(os.listdir('meow')), 'rb')
        bot.send_voice(message.from_user.id, meow)
        meow.close()  
    else:
        bot.send_message(message.from_user.id, 'мяу мяу мяу')


@bot.message_handler(content_types=['photo'])
def photo(message):
    print(f'UserID {message.from_user.id} | UserName {message.from_user.username}')
    photo_id = message.photo[0].file_id
    your_id = '' #<--- your tg id 
    bot.send_message(message.from_user.id, 'спасибо за котика')
    print(Fore.CYAN + f'{message.from_user.username} отправил котика (нет)')
    save_file(text=f'{message.from_user.username} отправил фото')
    bot.send_photo(your_id, photo_id, caption=f'message from - @{message.from_user.username}')


bot.polling(none_stop=True, interval=0)