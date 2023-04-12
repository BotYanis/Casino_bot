from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard = True, row_width=2, one_time_keyboard=False)
kb_ban = ReplyKeyboardMarkup(resize_keyboard = True, row_width=2, one_time_keyboard=False)
button = KeyboardButton('Игры 🎮')
button1 = KeyboardButton('Профиль 👨‍💻 ')
button2 = KeyboardButton('FAQ 📖')
button3 = KeyboardButton('Поддержка 🛎')
ban_button = KeyboardButton('🚫')
kb.add(button,button1,button2,button3)
kb_ban.add(ban_button)

roulette = InlineKeyboardButton('🔴⚫ Рулетка' , callback_data = 'roulette')
slots = InlineKeyboardButton('🎰 Слоты' , callback_data = 'slots')
dice = InlineKeyboardButton('🎲 Кости' , callback_data = 'dice')
shell = InlineKeyboardButton('📦 Наперстки' , callback_data = 'shell')
basketball = InlineKeyboardButton('🏀 Баскетбол' , callback_data = 'basketball')
darts = InlineKeyboardButton('🎯 Дартс' , callback_data = 'darts')
bowling = InlineKeyboardButton('🎳 Боулинг' , callback_data = 'bowling')
football = InlineKeyboardButton('⚽ Футбол' , callback_data = 'football')
apple = InlineKeyboardButton('🍏 Яблочки' , callback_data = 'apples')
coin = InlineKeyboardButton('🪙 Монетка' , callback_data = 'coin')
jackpot = InlineKeyboardButton('7⃣  Джекпот' , callback_data = 'jackpot')
blackjack = InlineKeyboardButton('🃏 Блекджек' , callback_data = 'blackjack')

b8 = InlineKeyboardButton('✅' , callback_data = '+')
b9 = InlineKeyboardButton('❌' , callback_data = '-')

repeat_roulette = InlineKeyboardButton('🔄', callback_data = 'repeat_roulette')
repeat_basketball = InlineKeyboardButton('🔄', callback_data = 'repeat_basketball')
repeat_football = InlineKeyboardButton('🔄', callback_data = 'repeat_football')
repeat_dice = InlineKeyboardButton('🔄', callback_data = 'repeat_dice')
repeat_bowling = InlineKeyboardButton('🔄', callback_data = 'repeat_bowling')
repeat_darts = InlineKeyboardButton('🔄', callback_data = 'repeat_darts')
repeat_shell = InlineKeyboardButton('🔄', callback_data = 'repeat_shell')
repeat_slots = InlineKeyboardButton('🔄', callback_data = 'repeat_slots')
repeat_coin = InlineKeyboardButton('🔄', callback_data = 'repeat_coin')

apple_bt_1 = InlineKeyboardButton('1', callback_data = 'apple:first')
apple_bt_2 = InlineKeyboardButton('1', callback_data = 'apple:second')
apple_bt_3 = InlineKeyboardButton('🧰', callback_data = 'apple:third')
apple_bt_4 = InlineKeyboardButton('🧰', callback_data = 'apple:four')
apple_bt_5 = InlineKeyboardButton('🧰', callback_data = 'apple:five')
apple_bt_6 = InlineKeyboardButton('🧰', callback_data = 'apple:six')
apple_bt_7 = InlineKeyboardButton('🧰', callback_data = 'apple:seven')
apple_bt_8 = InlineKeyboardButton('🧰', callback_data = 'apple:eight')
apple_bt_9 = InlineKeyboardButton('🧰', callback_data = 'apple:nine')
apple_bt_10 = InlineKeyboardButton('🧰', callback_data = 'apple:ten')

coeffi_bt_1 = InlineKeyboardButton('1.24', callback_data = 'coeffi:first')
coeffi_bt_2 = InlineKeyboardButton('1.55', callback_data = 'coeffi:second')
coeffi_bt_3 = InlineKeyboardButton('1.93', callback_data = 'coeffi:three')
coeffi_bt_4 = InlineKeyboardButton('2.42', callback_data = 'coeffi:four')
coeffi_bt_5 = InlineKeyboardButton('4.03', callback_data = 'coeffi:five')
coeffi_bt_6 = InlineKeyboardButton('6.71', callback_data = 'coeffi:six')
coeffi_bt_7 = InlineKeyboardButton('11.19', callback_data = 'coeffi:seven')
coeffi_bt_8 = InlineKeyboardButton('27.97', callback_data = 'coeffi:eight')
coeffi_bt_9 = InlineKeyboardButton('69.94', callback_data = 'coeffi:nine')
coeffi_bt_10 = InlineKeyboardButton('349.68', callback_data = 'coeffi:ten')
apple_ok = InlineKeyboardButton('✅', callback_data = 'apple_ok')

apple_keyboard = InlineKeyboardMarkup(row_width = 6).add(apple_bt_1, apple_bt_1, apple_bt_1,apple_bt_1, apple_bt_1, coeffi_bt_1,
                                                         apple_bt_2, apple_bt_2, apple_bt_2,apple_bt_2, apple_bt_2, coeffi_bt_2,
                                                         apple_bt_3, apple_bt_1, apple_bt_1, apple_bt_1,apple_bt_1, coeffi_bt_3,
                                                         apple_bt_4, apple_bt_1, apple_bt_1,apple_bt_1, apple_bt_1, coeffi_bt_4,
                                                         apple_bt_5, apple_bt_1, apple_bt_1,apple_bt_1, apple_bt_1, coeffi_bt_1,
                                                         apple_bt_6, apple_bt_2, apple_bt_2,apple_bt_2, apple_bt_2, coeffi_bt_2,
                                                         apple_bt_7, apple_bt_1, apple_bt_1, apple_bt_1,apple_bt_1, coeffi_bt_3,
                                                         apple_bt_8, apple_bt_1, apple_bt_1,apple_bt_1, apple_bt_1, coeffi_bt_4,
                                                         apple_bt_7, apple_bt_1, apple_bt_1, apple_bt_1,apple_bt_1, coeffi_bt_3,
                                                         apple_bt_8, apple_bt_1, apple_bt_1,apple_bt_1, apple_bt_1, coeffi_bt_4,
                                                         apple_ok
                                                        )

b13 = InlineKeyboardButton('⬆' , callback_data = 'shell_first')
b14 = InlineKeyboardButton('⬆' , callback_data = 'shell_second')
b15 = InlineKeyboardButton('⬆' , callback_data = 'shell_third')


back_menu = InlineKeyboardButton('⬅' , callback_data = 'back_menu')
back_admin_panel = InlineKeyboardButton('⬅' , callback_data = 'back_admin_panel')
back_profile = InlineKeyboardButton('⬅' , callback_data = 'back_profile')
back_users = InlineKeyboardButton('⬅' , callback_data = 'back_users')
back_promocode = InlineKeyboardButton('⬅' , callback_data = 'back_promocode')
back_voucher = InlineKeyboardButton('⬅' , callback_data = 'back_voucher')
back_balance = InlineKeyboardButton('⬅' , callback_data = 'back_balance')

deposit = InlineKeyboardButton('➕ Пополнить', callback_data='deposit')
withdrawal = InlineKeyboardButton('➖ Вывести', callback_data='withdrawal')
demo_balance = InlineKeyboardButton('🕹 Демобаланс', callback_data = 'demobalance_get')
demo_balance_on = InlineKeyboardButton('Вкл реал баланс 💵', callback_data = 'demobalance_on')
demo_balance_off = InlineKeyboardButton('Вкл демобаланс 🕹', callback_data = 'demobalance_off')
balance = InlineKeyboardButton('🏦 Баланс', callback_data='balance_menu')
activate_promo = InlineKeyboardButton('🎫 Ввести промо', callback_data='activate_promo')
activate_voucher = InlineKeyboardButton('🎟 Ввести ваучер', callback_data='activate_voucher')
admin_panel = InlineKeyboardButton('⚙ Панель администратора', callback_data = 'admin_button')

bet_increase = InlineKeyboardButton('➕', callback_data='bet_increase')
bet_decrease = InlineKeyboardButton('➖', callback_data='bet_decrease')
create_room = InlineKeyboardButton('➕ Создать игру', callback_data='create_room')
join_room = InlineKeyboardButton('👉 Зайти в игру', callback_data = 'join_room')

bet_confirm_roulette = InlineKeyboardButton('✅' , callback_data = 'bet_confirm_roulette')
bet_confirm_bowling = InlineKeyboardButton('✅' , callback_data = 'bet_confirm_bowling')
bet_confirm_darts = InlineKeyboardButton('✅' , callback_data = 'bet_confirm_darts')
bet_confirm_dice = InlineKeyboardButton('✅' , callback_data = 'bet_confirm_dice')
bet_confirm_slots = InlineKeyboardButton('✅' , callback_data = 'bet_confirm_slots')
bet_confirm_football = InlineKeyboardButton('✅' , callback_data = 'bet_confirm_football')
bet_confirm_basketball = InlineKeyboardButton('✅' , callback_data = 'bet_confirm_basketball')
bet_confirm_shell = InlineKeyboardButton('✅' , callback_data = 'bet_confirm_shell')
bet_confirm_coin = InlineKeyboardButton('✅' , callback_data = 'bet_confirm_coin')

sending_bt = InlineKeyboardButton('Рассылка 📲', callback_data = 'mail')
statistics = InlineKeyboardButton('Статистика 📊', callback_data = 'statistics')
users = InlineKeyboardButton('Пользователи 👥', callback_data = 'users')
output_on = InlineKeyboardButton('Автовывод ✅', callback_data = 'output_on')
output_off = InlineKeyboardButton('Автовывод ❌', callback_data = 'output_off')
promocode = InlineKeyboardButton('Промокод 🎫', callback_data = 'promocode')
voucher = InlineKeyboardButton('Ваучер 🎟', callback_data = 'voucher')
add_admin_kb = InlineKeyboardButton('➕ админ', callback_data = 'add_admin')
delete_admin_kb = InlineKeyboardButton('➖ админ', callback_data = 'delete_admin')
forms = InlineKeyboardButton('Заявки 🗂', callback_data = 'forms')

half_money = InlineKeyboardButton('Вывести часть средств 🌓' , callback_data = 'half_money')
all_money = InlineKeyboardButton('Вывести все средства 🌕', callback_data = 'all_money')

b52 = InlineKeyboardButton('Попробовать еще раз 🔄' , callback_data = 'bt52')
b53 = InlineKeyboardButton('⬅ Меню' , callback_data = 'bt53')

red = InlineKeyboardButton('🔴' , callback_data = 'red')
black = InlineKeyboardButton('⚫' , callback_data = 'black')
even = InlineKeyboardButton('Чётное' , callback_data = 'even')
odd = InlineKeyboardButton('Нечётное' , callback_data = 'odd')
one_twelve = InlineKeyboardButton('1️⃣ ➖ 1️⃣2️⃣', callback_data = '112')
thirteen_twentyfour = InlineKeyboardButton('1️⃣3️⃣ ➖ 2️⃣️4️⃣', callback_data = '1324')
twentyfive_thirtysix = InlineKeyboardButton('2️⃣5️⃣ ➖ 3️⃣6️⃣', callback_data = '2536')
one_eighteen = InlineKeyboardButton('1️⃣ ➖ 1️⃣8️⃣', callback_data = '118')
nineteen_thirtysix = InlineKeyboardButton('1️⃣9️⃣ ➖ 3️⃣6️⃣', callback_data = '1936')

zero = InlineKeyboardButton('0️⃣', callback_data = 'zero')

coin_1 = InlineKeyboardButton('Орел 🦅', callback_data = 'coin_eagle')
coin_2 = InlineKeyboardButton('Решка 🌰', callback_data = 'coin_tail')

coin_kb = InlineKeyboardMarkup(row_width = 1).add(coin_1, coin_2)

card = InlineKeyboardButton('💳 Карта | 1%' , callback_data = 'card')
qiwi = InlineKeyboardButton('🥝 QIWI | 0%', callback_data = 'qiwi')
youmoney = InlineKeyboardButton('🟣 ЮМани | 0%', callback_data = 'youmoney')
bitcoin = InlineKeyboardButton('₿ Bitcoin | 0%', callback_data = 'bitcoin')
crystal = InlineKeyboardButton('💎 CrystalPay | 1-5%', callback_data = 'crystalpay')

cancel_button = InlineKeyboardButton('❌', callback_data = 'cancel_payment')
cancel_user = InlineKeyboardButton('❌', callback_data = 'cancel_user')
cancel_admin = InlineKeyboardButton('❌', callback_data = 'cancel_admin')
cancel_promo = InlineKeyboardButton('❌', callback_data = 'cancel_promo')
cancel_voucher = InlineKeyboardButton('❌', callback_data = 'cancel_voucher')
cancel_promo1 = InlineKeyboardButton('❌', callback_data = 'cancel_promo_activation')
cancel_voucher1 = InlineKeyboardButton('❌', callback_data = 'cancel_voucher_activation')

old = InlineKeyboardButton('Предыдущая 📦', callback_data = 'old')
new = InlineKeyboardButton('Создать новую 📲', callback_data = 'new')

user_ban = InlineKeyboardButton('🚫 Забанить ', callback_data = 'user_ban')
user_unban = InlineKeyboardButton('✅ Разбанить', callback_data = 'user_unban')
decrease_balance = InlineKeyboardButton('➖ баланс', callback_data = 'user_decrease_balance')
increase_balance = InlineKeyboardButton('➕ баланс', callback_data = 'user_increase_balance')

promocode_create_bt = InlineKeyboardButton('Создать промокод 🍾', callback_data = 'promocode_create')
voucher_create_bt = InlineKeyboardButton('Создать ваучер 🏹', callback_data = 'voucher_create')
promocode_delete_bt = InlineKeyboardButton('Отключить промокод 🗑', callback_data = 'promocode_delete')
voucher_delete_kb = InlineKeyboardButton('Отключить ваучер 🪃', callback_data = 'voucher_delete')

voucher_kb = InlineKeyboardMarkup(row_width = 1).add(voucher_create_bt, voucher_delete_kb, back_admin_panel)
promocode_kb = InlineKeyboardMarkup(row_width = 1).add(promocode_create_bt, promocode_delete_bt, back_admin_panel)

balance_menu_on = InlineKeyboardMarkup(row_width = 2).add(deposit, withdrawal, demo_balance, demo_balance_on, back_profile)
balance_menu_off  = InlineKeyboardMarkup(row_width = 2).add(deposit, withdrawal, demo_balance, demo_balance_off, back_profile)
reject_ban = InlineKeyboardButton('❌', callback_data = 'reject_ban')
confirm_ban = InlineKeyboardButton('✅', callback_data='confirm_ban')

confirm_ban_kb = InlineKeyboardMarkup(row_width = 2).add(confirm_ban, reject_ban)
user_actions_kb = InlineKeyboardMarkup(row_width = 2).add(user_ban, user_unban, increase_balance, decrease_balance, back_admin_panel)

confirm = InlineKeyboardMarkup(row_width = 2).add(b8, b9)

games = InlineKeyboardMarkup(row_width = 3).add(roulette, slots, dice, shell, basketball, darts, bowling, football, coin)

admin_kb_off = InlineKeyboardMarkup(row_width = 2).add(sending_bt, statistics, users,  output_off, promocode, voucher, forms, back_profile)
admin_kb_on = InlineKeyboardMarkup(row_width = 2).add(sending_bt, statistics, users, output_on, promocode, voucher, forms, back_profile)

creator_kb_off = InlineKeyboardMarkup(row_width = 2).add(sending_bt, statistics, users,  output_off, promocode, voucher, add_admin_kb, delete_admin_kb, forms, back_profile)
creator_kb_on = InlineKeyboardMarkup(row_width = 2).add(sending_bt, statistics, users, output_on, promocode, voucher, add_admin_kb, delete_admin_kb, forms, back_profile)

roulette_kb = InlineKeyboardMarkup(row_width = 1).row(red, zero, black)
roulette_kb.row(odd, even)
roulette_kb.row(one_twelve, thirteen_twentyfour)
roulette_kb.row(twentyfive_thirtysix)
roulette_kb.row(one_eighteen, nineteen_thirtysix)
roulette_kb.row(back_menu)

bet_roulette_kb = InlineKeyboardMarkup(row_width = 2).add(bet_increase, bet_decrease)
bet_bowling_kb = InlineKeyboardMarkup(row_width = 2).add(bet_increase, bet_decrease)
bet_darts_kb = InlineKeyboardMarkup(row_width = 2).add(bet_increase, bet_decrease)
bet_dice_kb = InlineKeyboardMarkup(row_width = 2).add(bet_increase, bet_decrease)
bet_slots_kb = InlineKeyboardMarkup(row_width = 2).add(bet_increase, bet_decrease)
bet_football_kb = InlineKeyboardMarkup(row_width = 2).add(bet_increase, bet_decrease)
bet_basketball_kb = InlineKeyboardMarkup(row_width = 2).add(bet_increase, bet_decrease)
bet_shell_kb = InlineKeyboardMarkup(row_width = 2).add(bet_increase, bet_decrease)
bet_coin_kb = InlineKeyboardMarkup(row_width = 2).add(bet_increase, bet_decrease)
bet_jackpot_kb = InlineKeyboardMarkup(row_width = 2).add(create_room, join_room)

bet_roulette_kb.row(bet_confirm_roulette)
bet_roulette_kb.row(back_menu)
bet_bowling_kb.row(bet_confirm_bowling)
bet_bowling_kb.row(back_menu)
bet_darts_kb.row(bet_confirm_darts)
bet_darts_kb.row(back_menu)
bet_dice_kb.row(bet_confirm_dice)
bet_dice_kb.row(back_menu)
bet_slots_kb.row(bet_confirm_slots)
bet_slots_kb.row(back_menu)
bet_football_kb.row(bet_confirm_football)
bet_football_kb.row(back_menu)
bet_basketball_kb.row(bet_confirm_basketball)
bet_basketball_kb.row(back_menu)
bet_shell_kb.row(bet_confirm_shell)
bet_shell_kb.row(back_menu)
bet_coin_kb.row(bet_confirm_coin)
bet_coin_kb.row(back_menu)
bet_jackpot_kb.row(back_menu)

slots_kb = InlineKeyboardMarkup(row_width = 1).add(repeat_slots, back_menu)
dice_kb = InlineKeyboardMarkup(row_width = 1).add(repeat_dice, back_menu)
basketball_kb = InlineKeyboardMarkup(row_width = 1).add(repeat_basketball, back_menu)
football_kb = InlineKeyboardMarkup(row_width = 1).add(repeat_football, back_menu)
shell_kb = InlineKeyboardMarkup(row_width = 1).add(repeat_shell, back_menu)
darts_kb = InlineKeyboardMarkup(row_width = 1).add(repeat_darts, back_menu)
bowling_kb = InlineKeyboardMarkup(row_width = 1).add(repeat_bowling, back_menu)
roulette_kb1 = InlineKeyboardMarkup(row_width = 1).add(repeat_roulette, back_menu)
coin_kb_1 = InlineKeyboardMarkup(row_width = 1).add(repeat_coin, back_menu)

admin_profile = InlineKeyboardMarkup(row_width = 2).add(balance)

admin_profile.row(activate_promo, activate_voucher)
admin_profile.row(admin_panel)

creator_profile = InlineKeyboardMarkup(row_width = 2).add(balance)

creator_profile.row(activate_promo, activate_voucher)
creator_profile.row(admin_panel)

admin_profile.row(admin_panel)

user_profile = InlineKeyboardMarkup(row_width = 2).add(balance)
user_profile.row(activate_promo, activate_voucher)

method_payment = InlineKeyboardMarkup(row_width = 2).add(card, qiwi, youmoney, bitcoin)

method_payment.row(crystal)
method_payment.row(back_balance)

shell_buttons = InlineKeyboardMarkup(row_width = 3).add(b13, b14, b15 , back_menu)

cancel_payment = InlineKeyboardMarkup(row_width = 1).add(cancel_button)
cancel_user_kb = InlineKeyboardMarkup(row_width = 1).add(cancel_user)
cancel_admin_kb = InlineKeyboardMarkup(row_width = 1).add(cancel_admin)
cancel_voucher_kb = InlineKeyboardMarkup(row_width = 1).add(cancel_voucher)
cancel_promo_kb = InlineKeyboardMarkup(row_width = 1).add(cancel_promo)
cancel_voucher_kb1 = InlineKeyboardMarkup(row_width = 1).add(cancel_voucher1)
cancel_promo_kb1 = InlineKeyboardMarkup(row_width = 1).add(cancel_promo1)

back_admin_panel_kb = InlineKeyboardMarkup(row_width = 1).add(back_admin_panel)
back_menu_kb = InlineKeyboardMarkup(row_width = 1).add(back_menu)
back_profile_kb = InlineKeyboardMarkup(row_width = 1).add(back_profile)
back_users_kb = InlineKeyboardMarkup(row_width = 1).add(back_users)
back_promocode_kb = InlineKeyboardMarkup(row_width = 1).add(back_promocode)
back_voucher_kb = InlineKeyboardMarkup(row_width = 1).add(back_voucher)

sending_kb = InlineKeyboardMarkup(row_width = 2).add(new, old, back_admin_panel)

output_money = InlineKeyboardMarkup(row_width = 1).add(half_money, all_money, back_balance)