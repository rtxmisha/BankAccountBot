import telebot
from telebot import types
import configure
import random
from bank_account import BankAccount

bot = telebot.TeleBot(configure.config['token'])



@bot.message_handler(commands=['start'])
def start(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard = True)

    item1 = types.KeyboardButton('🗄 Баланс')
    item2 = types.KeyboardButton('📈 Доход')
    item3 = types.KeyboardButton('📉 Расход')
    item4 = types.KeyboardButton('📊 История опреций')
    item5 = types.KeyboardButton('❓ Помощь')


    murkup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}!'.format(message.from_user), reply_markup=murkup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':

        if message.text == '🗄 Баланс':
            myAccount = BankAccount()
            bot.send_message(message.chat.id, myAccount.displayBalance())

        elif message.text == '📈 Доход':
            murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('📈 Основной доход')
            item2 = types.KeyboardButton('📈 Дополнительный доход')
            back = types.KeyboardButton('🔙Назад')
            murkup.add(item1, item2, back)
            bot.send_message(message.chat.id,'📈 Доход', reply_markup=murkup)

        elif message.text == '🔙Назад':
            murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🗄 Баланс')
            item2 = types.KeyboardButton('📈 Доход')
            item3 = types.KeyboardButton('📉 Расход')
            item4 = types.KeyboardButton('📊 История опреций')
            item5 = types.KeyboardButton('❓ Помощь')
            murkup.add(item1, item2, item3, item4, item5)
            bot.send_message(message.chat.id, 'Главное меню', reply_markup=murkup)

        elif message.text == '📈 Основной доход':
            @bot.message_handler(content_types=['text'])
            def ask_age(message):

                bot.send_message(message.chat.id, "What is your age?")

                # with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
                #     data['surname'] = message.text

            #
            # msg = bot.send_message(message.chat.id, 'Введите добавляемую сумму:?')
            # myAccount = BankAccount()
            # bot.send_message(message.chat.id, myAccount.deposit(amount=msg))


            # def user_answer(message):
            #     value = int(message.text)
            #     myAccount = BankAccount()
            #     bot.send_message(message.chat.id, myAccount.deposit(amount=value))






            # bot.send_message(message.chat.id, 'Введите сумму:')
            # msg = bot.message_handler(message.chat.id, )
            #
            #
            # value = int(msg)
            # myAccount = BankAccount()
            # bot.send_message(message.chat.id, myAccount.deposit(amount=value))
            # bot.send_message(message.chat.id, f'Спасибо')



# @client.message_handler(content_types=['text'])
# def get_text(message):
#     if message.text.lower() == 'start':
#         client.send_message(message.chat.id, 'Добро пожаловать в MyBankAccountBot!')


# @client.message_handler(commands = ['get_info', 'info'])
# def get_user_info(message):
#     markup_inline = types.InlineKeyboardMarkup()
#     item_yes = types.InlineKeyboardButton(text = 'YES', callback_data = 'yes')
#     item_no = types.InlineKeyboardButton(text='NO', callback_data='no')
#
#     markup_inline.add(item_yes, item_no)
#     client.send_message(message.chat.it, 'Would you like to know more info?', reply_markup = markup_inline)
#
# @client.callback_query_handler(func = lambda call: True)
# def answer(call):
#     if call.data == 'yes':
#         pass
#     elif call.data == 'no':
#         pass




# myAccount = BankAccount(000000, "Sber")
#
# myAccount.deposit(35.52)
# myAccount.withdraw(15)
#
# print("Название счета:", myAccount.acct_name)
# print("Номер счета:", myAccount.acct_number)
# myAccount.displayBalance()
# from telebot import types





# @client.message_handler(message):
#     markup_inline = types.InlineKeyboardMarkup():
#     item_yes = types.InlineKeyboardbutton(text = )




bot.polling(none_stop=True, interval=0)
