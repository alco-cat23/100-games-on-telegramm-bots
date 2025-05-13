import telebot
import random


bot = telebot.TeleBot('7935460812:AAGdnG1Vbr5VrC0eUSFLoXTwtOzg9_uYamE')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Русская рулетка, выбери пулю от /1 до /6')


@bot.message_handler(commands=['1', '2', '3', '4', '5', '6'])
def russian_roulette(message):
    bullet_nums = ['1', '2', '3', '4', '5', '6']
    bullet = random.choice(bullet_nums)
    user_choice = message.text[1:]  # Убираем "/" из команды

    if user_choice == bullet:
        bot.send_message(message.chat.id, 'Ты остался жив, выиграл')
    else:
        bot.send_message(message.chat.id, 'Ты умер, проиграл')


bot.infinity_polling()