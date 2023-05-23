import telebot 
from telebot import types

TOKEN = '5626590025:AAFnpw4A_-fbARG3X7XgAAYviLzAja9ildE'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start (message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('🌐Информация')
    item2 = types.KeyboardButton('🎻Культурные мероприятия')
    item3 = types.KeyboardButton('🎮Для молодежи')
    item4 = types.KeyboardButton('🎉Концерты')
    markup.add(item1, item2, item3, item4)

   
    bot.send_message(message.chat.id, 'hey bro!, {0.first_name}!'.format(message.from_user), reply_markup = markup)
@bot.message_handler(content_types=['text']) 
def bot_message(message):
    if message.chat.type == 'private':
         if message.text == '🌐Информация':
            bot.send_message(message.chat.id, 'Это начальная версия бота , которая будет дорабатываться и автоматизироваться в будущем, в дальнейшем он научиться сам собирать информацию с источников , фильтровать ее и отправлять пользователям. В настоящий момент бот способен отправлять информацию о различных мероприятиях пользователям , но информация которую он отправляет , собирается в ручную разработчиком .')

    if message.text == '🎻Культурные мероприятия':   
        bot.send_message(message.chat.id, 'Вот список самых интересных культурных мероприятий: \n 1) Экскурсия по выставке «И кажется, что храм поет застывшей красотою» \n Подробная информация: https://www.culture.ru/events/2944175/ekskursiya-po-vystavke-i-kazhetsya-chto-khram-poet-zastyvshei-krasotoyu?location=respublika-kareliya  \n 2) Выставка «И кажется, что храм поет застывшей красотою» \n Подробная информация: https://www.culture.ru/events/2568305/vystavka-i-kazhetsya-chto-khram-poet-zastyvshei-krasotoyu?location=respublika-kareliya  \n 3) Экскурсия «Тайная сила пояса» \n Подробная информация: https://www.culture.ru/events/2861123/ekskursiya-tainaya-sila-poyasa?location=respublika-kareliya \n 4) Интерактивная программа «Полеты над островом Кижи» \n Подробная информация: https://www.culture.ru/events/1939408/interaktivnaya-programma-polety-nad-ostrovom-kizhi?location=respublika-kareliya \n 5) Ночь в музее Кижи. Акция, посвященная Международному дню музеев. \n Подробная информация: https://www.culture.ru/events/3125870/noch-v-muzee-kizhi-akciya-posvyashennaya-mezhdunarodnomu-dnyu-muzeev?location=respublika-kareliya \n ')
    if message.text == '🎮Для молодежи':
        bot.send_message(message.chat.id, 'Захватывающие мероприятия для молодежи: \n 1) Компьютерный клуб MARS \n Подробная информация: https://langame.ru/799450431_computerniy_club_mars-petrozavodsk_petrozavodsk \n 2) Хоррор квесты в Петрозаводске \n Подробная информация: https://ptrzvd.mir-kvestov.ru/categories/horror \n 3) Ночной клуб "SOLO" \n Подробная информация: https://solodancesing.vsite.biz/ \n 4) Прыгнуть с парашютом \n Подробная информация: https://localway.ru/petrozavodsk/poi/dobrolet_313869 \n 5) Кинотеатр "Mirage" \n Подробная информация: https://www.mirage.ru/ptz/ ')
    if message.text == '🎉Концерты':
        bot.send_message(message.chat.id, 'Концерты знаменитых артистов в Карелии: \n 1) Концерт "Shaman" \n Подробная информация: https://ptz.kassir.ru/koncert/ledovyiy-dvorets-oao-kondopoga/shaman1_2023-06-18 \n 2) Концерт Ивана Абрамова \n Подробная информация: https://ptz.kassir.ru/koncert/ivan-abramov-ptz \n 3) Концерт группы "Анимация" \n Подробная информация: https://ptz.kassir.ru/koncert/animatsiya-18 4) Концерт группы "Ария" \n Подробная информация: https://ptz.kassir.ru/koncert/ariya-11 5) Выступление Гарика Сукачева \n Подробная информация: https://ptz.kassir.ru/koncert/garik-sukachev-7 ')
        

    

bot.polling(none_stop=True)
 