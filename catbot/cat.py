import telebot
from colorama import init, Fore
import os
import random
from datetime import datetime

time = datetime.now()

init()


print(Fore.GREEN + 'Start')


token = '5047054429:AAEwvvjPJ5qyaPhmFgF4beMN7neBF8S9Sp4'


bot = telebot.TeleBot(token)


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
    f = open('logs/logs.txt', 'a')
    f.write(f'{message.from_user.username} получил {photo.name} использовав функцию cat.\n')
    f.close()
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
    f = open('logs/logs.txt', 'a')
    f.write(f'{message.from_user.username} получил {meow.name} использовав функцию meow.\n')
    f.close()
    bot.send_voice(message.from_user.id, meow)
    meow.close()


@bot.message_handler(commands=['meme_from_2012'])
def meme(message):
    meme = open('meme/' + random.choice(os.listdir('meme')), 'rb')
    bot.send_photo(message.from_user.id, meme)
    f = open('logs/logs.txt', 'a')
    f.write(f'{message.from_user.username} получил {meme.name} использовав функцию meme.\n')
    f.close()
    print(f'UserID {message.from_user.id} | UserName {message.from_user.username}')
    meme.close()


@bot.message_handler(content_types=['text'])
def main(message):

    text = f'[TIME] - {time} | [USERNAME] - {message.from_user.username} | [MESSAGE] - {message.text}'
    print(Fore.WHITE + '[username]:', Fore.RED + message.from_user.username, Fore.WHITE + '[message]:', Fore.RED + message.text)
    print(f'UserID {message.from_user.id} | UserName {message.from_user.username}')
    f = open('logs/logs.txt', 'a')
    f.write(text + '\n')
    f.close()
    if message.text == 'мяукай':    
        meow = open('meow/' + random.choice(os.listdir('meow')), 'rb')
        bot.send_voice(message.from_user.id, meow)
        meow.close()  
    else:
        bot.send_message(message.from_user.id, 'мяу мяу мяу')


@bot.message_handler(content_types=['photo'])
def photo(message):
    print(f'UserID {message.from_user.id} | UserName {message.from_user.username}')
    id_ = message.photo[0].file_id
    ids = '1968765091'
    bot.send_message(message.from_user.id, 'спасибо за котика')
    print(Fore.CYAN + f'{message.from_user.username} отправил котика (нет)')
    f = open('logs/logs.txt', 'a')
    f.write(f'{message.from_user.username} отправил фото')
    f.close()
    bot.send_photo(ids, id_, caption=f'message from - @{message.from_user.username}')


aid = '2123111736'
aid1 = '1968765091'
#vid = open('D:/Download/w.mp4', 'rb')
#bot.send_video_note(aid1, vid)

import keyboard as kb

def input_to_you():
    id_ = '2123111736'
    a = Fore.CYAN + 'type text... '
    message = input(Fore.CYAN + a)
    bot.send_message(id_, message)

#kb.add_hotkey('up', input_to_you)

bot.polling(none_stop=True, interval=0)