import math
import requests
from pyqiwip2p import AioQiwiP2P
from glQiwiApi import *
from config import *
from main import *
from coinbase.wallet.client import Client
from random import *
from math import *

he_client = []

p2p = AioQiwiP2P(auth_key = p2p_closed_token)

storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)

async def create_payment_qiwi(price, chat_id):

    conn = sqlite3.connect('bebra.db')
    cursor = conn.cursor()

    new_bill = await p2p.bill(amount = price)

    cursor.execute('UPDATE payment_qiwi SET bill_id = ? WHERE user_id = ?', (f'{new_bill.bill_id}', chat_id,))
    conn.commit()

    cursor.execute('UPDATE payment_qiwi SET amount = ? WHERE user_id = ?', (f'{new_bill.amount}', chat_id,))
    conn.commit()

    cursor.close()

    b33 = InlineKeyboardButton('Проверить 🔎', callback_data='check_bill_qiwi')
    b35 = InlineKeyboardButton('Оплатить 💳', callback_data='oplata', url = new_bill.pay_url)
    kb27 = InlineKeyboardMarkup(row_width=2).add(b35, b33)

    await bot.send_message(chat_id, f'Сумма пополнения: *{round(float(new_bill.amount))} 🪙*', reply_markup = kb27, parse_mode = 'Markdown')

async def check_payment_qiwi(c, chat_id, message_id, username):

    conn = sqlite3.connect('bebra.db')
    cursor = conn.cursor()

    bill = cursor.execute('SELECT bill_id FROM payment_qiwi WHERE user_id = ?', (chat_id,)).fetchone()[0]
    amount = cursor.execute('SELECT amount FROM payment_qiwi WHERE user_id = ?', (chat_id,)).fetchone()[0]
    balance = cursor.execute('SELECT balance FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]
    referer = cursor.execute('SELECT referer FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]
    status = ((await p2p.check(bill_id = bill.split(':')[0])).status)
    referal_level = cursor.execute('SELECT referal_level FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]
    voucher = cursor.execute('SELECT voucher FROM info WHERE user_id = ?', (chat_id,)).fetchone()[0]
    promo = cursor.execute('SELECT promo FROM info WHERE user_id = ?', (chat_id,)).fetchone()[0]

    if status == 'PAID':

        await bot.answer_callback_query(c.id)

        cursor.execute('UPDATE info SET method = ? WHERE user_id = ?', ('qiwi', chat_id,))
        conn.commit()

        if referer:

            if voucher:

                voucher = round(amount) + int(voucher)

                cursor.execute('UPDATE info SET voucher = ? WHERE user_id = ?', (None, chat_id,))
                conn.commit()

            else:

                voucher = 0

            if promo:

                promo = (round(amount) / 100) * promo

                cursor.execute('UPDATE info SET promo = ? WHERE user_id = ?', (None, chat_id,))
                conn.commit()

            else:

                promo = 0

            if referal_level == 1:

                cursor.execute('UPDATE info SET referal_profit = ? WHERE user_id = ?',
                               (referal_profit + (round(int(amount / 100)) * 2), referer,))
                conn.commit()

                cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                               (balance + (round(amount / 100) * 2), referer,))
                conn.commit()

                cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                               (balance + round(amount) + promo + voucher, chat_id,))
                conn.commit()

                cursor.execute('UPDATE info SET method = ? WHERE user_id = ?',
                               ('youmoney', chat_id,))
                conn.commit()

                balance = cursor.execute('SELECT balance FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]

                amount = cursor.execute('SELECT amount FROM info WHERE user_id = ?', (chat_id,)).fetchone()[0]

                await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                            text=f'Вы успешно пополнили счет ✅ \n\n Ваш баланс: *{balance}* 🪙 \n\n ',
                                            parse_mode='Markdown')
                for i in admin:

                    await bot.send_message(i,
                                           f'💰 Новое поступление \n\n От пользователя: \n\n@{username} | {chat_id} \n\n На сумму: \n\n*{round(amount)}* 🪙',
                                           parse_mode='Markdown')
                cursor.close()

            elif referal_level == 2:

                cursor.execute('UPDATE info SET referal_profit = ? WHERE user_id = ?',
                               (referal_profit + (round(int(amount / 100)) * 4), referer,))
                conn.commit()

                cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                               (balance + (round(amount / 100) * 4), referer,))
                conn.commit()

                cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                               (balance + round(amount) + promo + voucher, chat_id,))
                conn.commit()

                cursor.execute('UPDATE info SET method = ? WHERE user_id = ?',
                               ('youmoney', chat_id,))
                conn.commit()

                balance = cursor.execute('SELECT balance FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]

                amount = cursor.execute('SELECT amount FROM info WHERE user_id = ?', (chat_id,)).fetchone()[0]

                await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                            text=f'Вы успешно пополнили счет ✅ \n\n Ваш баланс: *{balance}* 🪙 \n\n ',
                                            parse_mode='Markdown')
                for i in admin:

                    await bot.send_message(i,
                                           f'💰 Новое поступление \n\n От пользователя: \n\n@{username} | {chat_id} \n\n На сумму: \n\n*{round(amount)}* 🪙',
                                           parse_mode='Markdown')
                cursor.close()

            elif referal_level == 3:

                cursor.execute('UPDATE info SET referal_profit = ? WHERE user_id = ?',
                               (referal_profit + (round(int(amount / 100)) * 6), referer,))
                conn.commit()

                cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                               (balance + (round(amount / 100) * 6), referer,))
                conn.commit()

                cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                               (balance + round(amount) + promo + voucher, chat_id,))
                conn.commit()

                cursor.execute('UPDATE info SET method = ? WHERE user_id = ?',
                               ('youmoney', chat_id,))
                conn.commit()

                balance = cursor.execute('SELECT balance FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]

                amount = cursor.execute('SELECT amount FROM info WHERE user_id = ?', (chat_id,)).fetchone()[0]

                await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                            text=f'Вы успешно пополнили счет ✅ \n\n Ваш баланс: *{balance}* 🪙 \n\n ',
                                            parse_mode='Markdown')
                for i in admin:

                    await bot.send_message(i,
                                           f'💰 Новое поступление \n\n От пользователя: \n\n@{username} | {chat_id} \n\n На сумму: \n\n*{round(amount)}* 🪙',
                                           parse_mode='Markdown')
                cursor.close()

            elif referal_level == 4:

                cursor.execute('UPDATE info SET referal_profit = ? WHERE user_id = ?',
                               (referal_profit + (round(int(amount / 100)) * 8), referer,))
                conn.commit()

                cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                               (balance + (round(amount / 100) * 8), referer,))
                conn.commit()

                cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                               (balance + round(amount) + promo + voucher, chat_id,))
                conn.commit()

                cursor.execute('UPDATE info SET method = ? WHERE user_id = ?',
                               ('youmoney', chat_id,))
                conn.commit()

                balance = cursor.execute('SELECT balance FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]

                amount = cursor.execute('SELECT amount FROM info WHERE user_id = ?', (chat_id,)).fetchone()[0]

                await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                            text=f'Вы успешно пополнили счет ✅ \n\n Ваш баланс: *{balance}* 🪙 \n\n ',
                                            parse_mode='Markdown')
                for i in admin:

                    await bot.send_message(i,
                                           f'💰 Новое поступление \n\n От пользователя: \n\n@{username} | {chat_id} \n\n На сумму: \n\n*{round(amount)}* 🪙',
                                           parse_mode='Markdown')
                cursor.close()

            elif referal_level == 5:

                cursor.execute('UPDATE info SET referal_profit = ? WHERE user_id = ?',
                               (referal_profit + (round(int(amount / 100)) * 10), referer,))
                conn.commit()

                cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                               (balance + (round(amount / 100) * 10), referer,))
                conn.commit()

                cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                               (balance + round(amount) + promo + voucher, chat_id,))
                conn.commit()

                cursor.execute('UPDATE info SET method = ? WHERE user_id = ?',
                               ('youmoney', chat_id,))
                conn.commit()

                balance = cursor.execute('SELECT balance FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]

                amount = cursor.execute('SELECT amount FROM info WHERE user_id = ?', (chat_id,)).fetchone()[0]

                await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                            text=f'Вы успешно пополнили счет ✅ \n\n Ваш баланс: *{balance}* 🪙 \n\n ',
                                            parse_mode='Markdown')
                for i in admin:

                    await bot.send_message(i,
                                       f'💰 Новое поступление \n\n От пользователя: \n\n@{username} | {chat_id} \n\n На сумму: \n\n*{round(amount)}* 🪙',
                                       parse_mode='Markdown')
                cursor.close()

        else:

            if voucher:

                voucher = round(amount) + int(voucher)

                cursor.execute('UPDATE info SET voucher = ? WHERE user_id = ?', (None, chat_id,))
                conn.commit()

            else:

                voucher = 0

            if promo:

                promo = (round(amount) / 100) * promo

                cursor.execute('UPDATE info SET promo = ? WHERE user_id = ?', (None, chat_id,))
                conn.commit()

            else:

                promo = 0

            balance = cursor.execute('SELECT balance FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]
            amount = cursor.execute('SELECT amount FROM info WHERE user_id = ?', (chat_id,)).fetchone()[0]

            cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                           (balance + round(amount) + promo + voucher, chat_id,))
            conn.commit()

            balance = cursor.execute('SELECT balance FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]
            cursor.close()

            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=f'Вы успешно пополнили счет ✅ \n\n Ваш баланс: *{balance}* 🪙 \n\n ',
                                       parse_mode='Markdown')

            for i in admin:

                await bot.send_message(i,
                                   f'💰 Новое поступление \n\n От пользователя: \n\n@{username} | {chat_id} \n\n На сумму: \n\n*{amount}* 🪙',
                                  parse_mode='Markdown')

    else:

        await c.answer(text='Платеж не оплачен ❌')

async def create_bill_btc(chat_id, message_id, summa, amount):

    client = Client(open_coinbase, close_coinbase)
    account_id = client.get_primary_account()['id']

    btc_price = float(((client.get_exchange_rates(currency = 'RUB')['rates']['BTC']))[0:10])
    btc_price = ("{:.8f}".format(btc_price * int(amount)))

    address_for_tranz = client.create_address(account_id)['address']  # получение кошелька для оплты

    conn = sqlite3.connect('bebra.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE payment_bitcoin SET bill_id = ? WHERE user_id = ?', (address_for_tranz, chat_id,))
    conn.commit()

    cursor.execute('UPDATE payment_bitcoin SET amount = ? WHERE user_id = ?', (btc_price + f':{amount}', chat_id,))
    conn.commit()

    cursor.close()

    check_btc = InlineKeyboardButton('Проверить 🔎', callback_data='check_bill_bitcoin')
    bitcoin_kb = InlineKeyboardMarkup(row_width=2).add(check_btc)

    try:

        await bot.send_message(chat_id, '🏷 Сумма пополнения: \n\n *' + str(btc_price) + '* ₿ \n\n 📩 Адрес для пополнения: *\n\n' + str(address_for_tranz) + '*' , parse_mode='Markdown', reply_markup = bitcoin_kb)

    except:

        await bot.send_message(chat_id, 'В данный момент платеж провести невозможно, обратитесь в поддержку 🤕')

    he_client.append(chat_id)

async def check_oplata_btc(chat_id, c, username, message_id):

    conn = sqlite3.connect('bebra.db')
    cursor = conn.cursor()

    address = cursor.execute('SELECT bill_id FROM payment_bitcoin WHERE user_id = ?', (chat_id,)).fetchone()[0]
    summa = cursor.execute('SELECT amount FROM payment_bitcoin WHERE user_id = ?', (chat_id,)).fetchone()[0]
    amount = summa.split(':')[1]
    balance = cursor.execute('SELECT balance FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]
    voucher = cursor.execute('SELECT voucher FROM info WHERE user_id = ?', (chat_id,)).fetchone()[0]
    promo = cursor.execute('SELECT promo FROM info WHERE user_id = ?', (chat_id,)).fetchone()[0]
    referer = cursor.execute('SELECT referer FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]

    if chat_id in he_client:

        r = requests.get('https://blockchain.info/q/addressbalance/' + address)
        s = r.text

        if referer is not None:

            referal_level = cursor.execute('SELECT referal_level FROM users WHERE user_id = ?', (referer,)).fetchone()[
                0]
            referal_profit = cursor.execute('SELECT referal_profit FROM info WHERE user_id = ?', (referer,)).fetchone()[
                0]

            if float(s) >= float(summa.split(':')[0]):

                if referal_level == 1:

                    cursor.execute('UPDATE info SET referal_profit = ? WHERE user_id = ?',
                                   (referal_profit + (round(int(amount / 100)) * 2), referer,))
                    conn.commit()

                    cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                                   (balance + (round(amount / 100) * 2), referer,))
                    conn.commit()

                    cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                                   (balance + round(amount) + voucher + promo, chat_id,))
                    conn.commit()

                    cursor.execute('UPDATE info SET method = ? WHERE user_id = ?',
                                   ('bitcoin', chat_id,))
                    conn.commit()

                    balance = cursor.execute('SELECT balance FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]

                    amount = cursor.execute('SELECT amount FROM info WHERE user_id = ?', (chat_id,)).fetchone()[0]

                    await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                                text=f'Вы успешно пополнили счет ✅ \n\n Ваш баланс: *{balance}* 🪙 \n\n ',
                                                parse_mode='Markdown')
                    await bot.send_message(admin[0],
                                           f'💰 Новое поступление \n\n От пользователя: \n\n@{username} | {chat_id} \n\n На сумму: \n\n*{round(amount)}* 🪙',
                                           parse_mode='Markdown')
                    cursor.close()

                elif referal_level == 2:

                    cursor.execute('UPDATE info SET referal_profit = ? WHERE user_id = ?',
                                   (referal_profit + (round(int(amount / 100)) * 4), referer,))
                    conn.commit()

                    cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                                   (balance + (round(amount / 100) * 4), referer,))
                    conn.commit()

                    cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                                   (balance + round(amount) + voucher + promo, chat_id,))
                    conn.commit()

                    cursor.execute('UPDATE info SET method = ? WHERE user_id = ?',
                                   ('bitcoin', chat_id,))
                    conn.commit()

                    balance = cursor.execute('SELECT balance FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]

                    amount = cursor.execute('SELECT amount FROM info WHERE user_id = ?', (chat_id,)).fetchone()[0]

                    await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                                text=f'Вы успешно пополнили счет ✅ \n\n Ваш баланс: *{balance}* 🪙 \n\n ',
                                                parse_mode='Markdown')
                    await bot.send_message(admin[0],
                                           f'💰 Новое поступление \n\n От пользователя: \n\n@{username} | {chat_id} \n\n На сумму: \n\n*{round(amount)}* 🪙',
                                           parse_mode='Markdown')
                    cursor.close()

                elif referal_level == 3:

                    cursor.execute('UPDATE info SET referal_profit = ? WHERE user_id = ?',
                                   (referal_profit + (round(int(amount / 100)) * 6), referer,))
                    conn.commit()

                    cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                                   (balance + (round(amount / 100) * 6), referer,))
                    conn.commit()

                    cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                                   (balance + round(amount) + voucher + promo, chat_id,))
                    conn.commit()

                    cursor.execute('UPDATE info SET method = ? WHERE user_id = ?',
                                   ('bitcoin', chat_id,))
                    conn.commit()

                    balance = cursor.execute('SELECT balance FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]

                    amount = cursor.execute('SELECT amount FROM info WHERE user_id = ?', (chat_id,)).fetchone()[0]

                    await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                                text=f'Вы успешно пополнили счет ✅ \n\n Ваш баланс: *{balance}* 🪙 \n\n ',
                                                parse_mode='Markdown')
                    await bot.send_message(admin[0],
                                           f'💰 Новое поступление \n\n От пользователя: \n\n@{username} | {chat_id} \n\n На сумму: \n\n*{round(amount)}* 🪙',
                                           parse_mode='Markdown')
                    cursor.close()

                elif referal_level == 4:

                    cursor.execute('UPDATE info SET referal_profit = ? WHERE user_id = ?',
                                   (referal_profit + (round(int(amount / 100)) * 8), referer,))
                    conn.commit()

                    cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                                   (balance + (round(amount / 100) * 8), referer,))
                    conn.commit()

                    cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                                   (balance + round(amount) + voucher + promo, chat_id,))
                    conn.commit()

                    cursor.execute('UPDATE info SET method = ? WHERE user_id = ?',
                                   ('bitcoin', chat_id,))
                    conn.commit()

                    balance = cursor.execute('SELECT balance FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]

                    amount = cursor.execute('SELECT amount FROM info WHERE user_id = ?', (chat_id,)).fetchone()[0]

                    await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                                text=f'Вы успешно пополнили счет ✅ \n\n Ваш баланс: *{balance}* 🪙 \n\n ',
                                                parse_mode='Markdown')
                    await bot.send_message(admin[0],
                                           f'💰 Новое поступление \n\n От пользователя: \n\n@{username} | {chat_id} \n\n На сумму: \n\n*{round(amount)}* 🪙',
                                           parse_mode='Markdown')
                    cursor.close()

                elif referal_level == 5:

                    cursor.execute('UPDATE info SET referal_profit = ? WHERE user_id = ?',
                                   (referal_profit + (round(int(amount / 100)) * 10), referer,))
                    conn.commit()

                    cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                                   (balance + (round(amount / 100) * 10), referer,))
                    conn.commit()

                    cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?',
                                   (balance + round(amount) + voucher + promo, chat_id,))
                    conn.commit()

                    cursor.execute('UPDATE info SET method = ? WHERE user_id = ?',
                                   ('bitcoin', chat_id,))
                    conn.commit()

                    balance = cursor.execute('SELECT balance FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]

                    amount = cursor.execute('SELECT amount FROM info WHERE user_id = ?', (chat_id,)).fetchone()[0]

                    await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                                text=f'Вы успешно пополнили счет ✅ \n\n Ваш баланс: *{balance}* 🪙 \n\n ',
                                                parse_mode='Markdown')
                    await bot.send_message(admin[0],
                                           f'💰 Новое поступление \n\n От пользователя: \n\n@{username} | {chat_id} \n\n На сумму: \n\n*{round(amount)}* 🪙',
                                           parse_mode='Markdown')
                    cursor.close()

            else:

                await c.answer(text='Платеж не оплачен ❌')

        else:

            if float(s) >= float(summa.split(':')[0]):

                if voucher:

                    voucher = round(amount) + int(voucher)

                    cursor.execute('UPDATE info SET voucher = ? WHERE user_id = ?', (None, chat_id,))
                    conn.commit()

                else:

                    voucher = 0

                if promo:

                    promo = (round(amount) / 100) * promo

                    cursor.execute('UPDATE info SET promo = ? WHERE user_id = ?', (None, chat_id,))
                    conn.commit()

                else:

                    promo = 0

                await bot.answer_callback_query(c.id)

                conn = sqlite3.connect('bebra.db')
                cursor = conn.cursor()

                cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?', (balance + summa + voucher + promo, chat_id,))
                conn.commit()

                cursor.execute('UPDATE info SET method = ? WHERE user_id = ?', ('bitcoin', chat_id,))
                conn.commit()

                balance = cursor.execute('SELECT balance FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]

                cursor.close()

                await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                            text=f'Вы успешно пополнили счет ✅\n\n Ваш баланс: *{balance} 🪙*',
                                            parse_mode='Markdown')
                await bot.send_message(admin, f'🛎️ Пополнение от: {chat_id} | @{username} \n\n💰 На сумму: {summa} ₿ | {amount} 🪙')

            else:

                await c.answer(text='Платеж не оплачен ❌')

    else:

        print(1)

async def create_payment_crystalpay(amount, chat_id):

    a = requests.get(f'https://api.crystalpay.ru/v1/?s={secret_crystal}&n={login_crystal}&o=invoice-create&amount={amount}').json()

    id = a['id']
    url = a['url']

    conn = sqlite3.connect('bebra.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE payment_crystalpay SET bill_id = ? WHERE user_id = ?', (id, chat_id,))
    conn.commit()

    cursor.execute('UPDATE payment_crystalpay SET amount = ? WHERE user_id = ?', (amount, chat_id,))
    conn.commit()

    cursor.close()

    b33 = InlineKeyboardButton('Проверить 🔎', callback_data='check_bill_crystalpay')
    b35 = InlineKeyboardButton('Оплатить 💳', callback_data='oplata', url = url)
    kb27 = InlineKeyboardMarkup(row_width=2).add(b35, b33)

    await bot.send_message(chat_id, f'Сумма пополнения: *{round(float(amount))} 🪙*', reply_markup = kb27, parse_mode = 'Markdown')

async def check_payment_crystalpay(c, chat_id, message_id):

    conn = sqlite3.connect('bebra.db')
    cursor = conn.cursor()

    bill_id = cursor.execute('SELECT bill_id FROM payment_crystalpay WHERE user_id = ?', (chat_id,)).fetchone()[0]

    a = requests.get(f'https://api.crystalpay.ru/v1/?s={secret_crystal}&n={login_crystal}&o=invoice-check&i={bill_id}').json()

    if a['state'] == 'payed':

        await bot.answer_callback_query(c.id)

        balance = cursor.execute('SELECT balance FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]
        amount = cursor.execute('SELECT amount FROM payment_crystalpay WHERE user_id = ?', (chat_id,)).fetchone()[0]

        cursor.execute('UPDATE users SET balance = ? WHERE user_id = ?', (balance + amount, chat_id,))
        conn.commit()

        balance = cursor.execute('SELECT balance FROM users WHERE user_id = ?', (chat_id,)).fetchone()[0]

        await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                    text=f'Вы успешно пополнили счет ✅ \n\n Ваш баланс: *{balance}* 🪙 \n\n ',
                                   parse_mode='Markdown')

        for i in list(admin):

            await bot.send_message(i,
                               f'💰 Новое поступление \n\n От пользователя: \n\n{chat_id} \n\n На сумму: \n\n*{amount}* 🪙',
                              parse_mode='Markdown')

        cursor.close()

    else:

        await c.answer(text='Платеж не оплачен ❌')












