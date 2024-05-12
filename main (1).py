import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random
from telebot.types import InputMediaPhoto

bot = telebot.TeleBot(token="7080782203:AAGoQtGtoUKc6QaLicWJmrSd0JMImYwxp_E")

kb = types.ReplyKeyboardMarkup(True)
kb.add(KeyboardButton('Теория'))
kb.add(KeyboardButton('Тест'))
keyboard = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton(text="Пабло Пикассо", callback_data="button1")
button2 = types.InlineKeyboardButton(text="Анри Матисс", callback_data="button2")
keyboard.row(button1, button2)
keyboard_remove = types.ReplyKeyboardRemove()
new_kb = types.ReplyKeyboardMarkup(True)
new_kb.add(KeyboardButton('Вернуться к теории'))
picasso_kb = types.InlineKeyboardMarkup()
matiss_kb = types.InlineKeyboardMarkup()
picasso_but = types.InlineKeyboardButton(text="Картины Пабло Пикассо", callback_data="but1")
matiss_but = types.InlineKeyboardButton(text="Картины Анри Матисса", callback_data="but2")
picasso_kb.row(picasso_but)
matiss_kb.row(matiss_but)

vodni_text = 'Анри Матисс (1869–1954) и Пабло Пикассо (1881–1973) - два величайших художника ХХ века. Возникшее между ними соперничество не только подстегнуло их индивидуальные успехи, но и изменило курс современного искусства. Никто не был более внимателен и осведомлен об искусстве Матисса, чем Пикассо, и наоборот. Оба исследовали вопросы пространства, движения, формы, цвета фигуративного и абстрактного искусства, а затем вдохновлялись работами друг друга для улучшения своего искусства.'
pablo_text = 'Пабло Пикассо родился в Малаге (Испания) в 1881 году. Пикассо с детства рос вундеркиндом, воспитанным и поддерживаемым его творческой семьей. В молодости юноша переехал в Париж, чтобы достичь славы и признания в столице мира искусства. Пикассо был вдохновлен образами Эдгара Дега и Анри де Тулуз-Лотрека (насыщенная жизнь внутри кабаре, сцены публичных домов и любопытные сюжеты с женщинами в баре или прачечной). Но затем в 1901 по 1904 год из-за смерти друга последовал его «Голубой период», пропитанный мрачными оттенками синего. Тематика этого периода отражает бедность, которую многие люди пережили в то непростое время. Пикассо считают одним из основоположников стиля кубизма, в то время, в 1907 году он вдохновился скульптурами безымянных африканских мастеров.'
matiss_text = 'Анри Матисс родился в замке Камбрези во Франции в 1869 году. Получил консервативное воспитание на севере Франции. До того, как Матисс нашел свое призвание, он изучал юридическое право в Париже и работал чиновником. Но мир Матисса кардинально изменился, когда в его 20 лет мать подарила ему коробку с красками. Обнаружив необычайную страсть и талант к искусству, Матисс оставил юридическую карьеру и решил учиться искусству в Париже. Уже в 1901 году Матисс стал лидером новейшего художественного движения фовистов. Под влиянием постимпрессионистов в фовизме преобладали твердые формы и яркие цвета, которые вызывали насыщенные и сильные эмоции и отражали абстрактное пространство.'
vopros1 = ['Где родился Пикассо:\n1. Франция\n2. Испания\n3. Португалия', 'Где родился Матисс:\n1. Франция\n2. Испания\n3. Португалия']
vopros2 = ['Основоположником какого стиля считают Пикассо:\n1. Абстракционизм\n2. Сюрреализм\n3. Кубизм\n4. Фовизм', 'Основоположником какого стиля считают Матисса:\n1. Абстракционизм\n2. Сюрреализм\n3. Кубизм\n4. Фовизм']
vopros3 = ['matisstest.jpg', 'picassotest.jpg']
vopros4 = ['matisstest1.jpg', 'picassotest1.jpg']
vopros5 = ['matisstest2.jpg', 'picassotest2.jpg']
vopros6 = ['matisstest3.jpg', 'picassotest3.jpg']
vopros7 = ['matisstest4.jpg', 'picassotest4.jpg']
test = {'Где родился Пикассо:\n1. Франция\n2. Испания\n3. Португалия': 2, 'Где родился Матисс:\n1. Франция\n2. Испания\n3. Португалия': 1, 'Основоположником какого стиля считают Пикассо:\n1. Абстракционизм\n2. Сюрреализм\n3. Кубизм\n4. Фовизм': 3, 'Основоположником какого стиля считают Матисса:\n1. Абстракционизм\n2. Сюрреализм\n3. Кубизм\n4. Фовизм': 4, 'matisstest.jpg': 2, 'matisstest1.jpg': 2, 'matisstest2.jpg': 2, 'matisstest3.jpg': 2, 'matisstest4.jpg': 2, 'picassotest.jpg': 1, 'picassotest1.jpg': 1, 'picassotest2.jpg': 1, 'picassotest3.jpg': 1, 'picassotest4.jpg': 1}
test_pic_text = "Правильный ответ. Теперь попоробуйте предположить, кто написал эту картину\n1. Пабло Пикассо\n2. Анри Матисс"
vpr1 = vopros1[random.randint(0,1)]
vpr2 = vopros2[random.randint(0,1)]
vpr3 = vopros3[random.randint(0,1)]
vpr4 = vopros4[random.randint(0,1)]
vpr5 = vopros5[random.randint(0,1)]
vpr6 = vopros6[random.randint(0,1)]
vpr7 = vopros7[random.randint(0,1)]
picassot = ['picassot.jpg', 'picassot1.jpg', 'picassot2.jpg', 'picassot3.jpg', 'picassot4.jpg']
matisst = ['matisst.jpg', 'matisst1.jpg', 'matisst2.jpg', 'matisst3.jpg', 'matisst4.jpg']

@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, "Этот бот поможет вам ознакомиться с творчеством Пабло Пикассо и Анри Матисса", reply_markup = kb)

@bot.message_handler(content_types = ['text'])
def start(message):
  if message.text == 'Теория':
    bot.send_message(message.chat.id, vodni_text,  reply_markup=kb)
    bot.send_message(message.from_user.id, 'Узнайте о каждом поподробнее',  reply_markup=keyboard)
  if message.text == 'Тест':
    bot.send_message(message.from_user.id, 'Для каждого вопроса отправляйте ТОЛЬКО цифру с правильным ответом', reply_markup=keyboard_remove)
    input1 = bot.send_message(message.chat.id, vpr1, reply_markup = new_kb)
    bot.register_next_step_handler(input1, point1)

def point1(message):

  if message.text == str(test[vpr1]):
    answer = bot.send_message(message.chat.id, f"Правильный ответ. Второе задание\n{vpr2}", reply_markup = new_kb)
    bot.register_next_step_handler(answer, point2)
  elif message.text == 'Вернуться к теории':
    bot.send_message(message.chat.id, vodni_text,  reply_markup=kb)
    bot.send_message(message.from_user.id, 'Узнайте о каждом поподробнее',  reply_markup=keyboard)
  else:
    answer = bot.send_message(message.chat.id, "Нет, попробуйте еще раз", reply_markup = new_kb)
    bot.register_next_step_handler(answer, point1)

def point2(message):

  if message.text == str(test[vpr2]):
    vpr = open(vpr3, 'rb')
    answer = bot.send_photo(message.chat.id, vpr, test_pic_text, reply_markup = new_kb)
    bot.register_next_step_handler(answer, point3)
  elif message.text == 'Вернуться к теории':
    bot.send_message(message.chat.id, vodni_text,  reply_markup=kb)
    bot.send_message(message.from_user.id, 'Узнайте о каждом поподробнее',  reply_markup=keyboard)
  else:
    answer = bot.send_message(message.chat.id, "Нет, попробуйте еще раз", reply_markup = new_kb)
    bot.register_next_step_handler(answer, point2)

def point3(message):

  if message.text == str(test[vpr3]):
    vpr = open(vpr4, 'rb')
    answer = bot.send_photo(message.chat.id, vpr, test_pic_text, reply_markup = new_kb)
    bot.register_next_step_handler(answer, point4)
  elif message.text == 'Вернуться к теории':
    bot.send_message(message.chat.id, vodni_text,  reply_markup=kb)
    bot.send_message(message.from_user.id, 'Узнайте о каждом поподробнее',  reply_markup=keyboard)
  else:
    answer = bot.send_message(message.chat.id, "Нет, попробуйте еще раз", reply_markup = new_kb)
    bot.register_next_step_handler(answer, point3)

def point4(message):
  if message.text == str(test[vpr4]):
    vpr = open(vpr5, 'rb')
    answer = bot.send_photo(message.chat.id, vpr, test_pic_text, reply_markup = new_kb)
    bot.register_next_step_handler(answer, point5)
  elif message.text == 'Вернуться к теории':
    bot.send_message(message.chat.id, vodni_text,  reply_markup=kb)
    bot.send_message(message.from_user.id, 'Узнайте о каждом поподробнее',  reply_markup=keyboard)
  else:
    answer = bot.send_message(message.chat.id, "Нет, попробуйте еще раз", reply_markup = new_kb)
    bot.register_next_step_handler(answer, point4)

def point5(message):
  if message.text == str(test[vpr5]):
    vpr = open(vpr6, 'rb')
    answer = bot.send_photo(message.chat.id, vpr, test_pic_text, reply_markup = new_kb)
    bot.register_next_step_handler(answer, point6)
  elif message.text == 'Вернуться к теории':
    bot.send_message(message.chat.id, vodni_text,  reply_markup=kb)
    bot.send_message(message.from_user.id, 'Узнайте о каждом поподробнее',  reply_markup=keyboard)
  else:
    answer = bot.send_message(message.chat.id, "Нет, попробуйте еще раз", reply_markup = new_kb)
    bot.register_next_step_handler(answer, point5)
    
def point6(message):
  if message.text == str(test[vpr6]):
    vpr = open(vpr7, 'rb')
    answer = bot.send_photo(message.chat.id, vpr, test_pic_text, reply_markup = new_kb)
    bot.register_next_step_handler(answer, point7)
  elif message.text == 'Вернуться к теории':
    bot.send_message(message.chat.id, vodni_text,  reply_markup=kb)
    bot.send_message(message.from_user.id, 'Узнайте о каждом поподробнее',  reply_markup=keyboard)
  else:
    answer = bot.send_message(message.chat.id, "Нет, попробуйте еще раз", reply_markup = new_kb)
    bot.register_next_step_handler(answer, point6)

def point7(message):
  if message.text == str(test[vpr7]):
    answer = bot.send_message(message.chat.id, 'Вы прошли тест', reply_markup = new_kb)
    bot.register_next_step_handler(answer, point8)
  elif message.text == 'Вернуться к теории':
    bot.send_message(message.chat.id, vodni_text,  reply_markup=kb)
    bot.send_message(message.from_user.id, 'Узнайте о каждом поподробнее',  reply_markup=keyboard)
  else:
    answer = bot.send_message(message.chat.id, "Нет, попробуйте еще раз", reply_markup = new_kb)
    bot.register_next_step_handler(answer, point7)

def point8(message):
  if message.text == 'Вернуться к теории':
    bot.send_message(message.chat.id, vodni_text,  reply_markup=kb)
    bot.send_message(message.from_user.id, 'Узнайте о каждом поподробнее',  reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "button1")
def callback_function1(callback_obj):
  photo1 = open('pablo.webp', 'rb')
  bot.send_photo(callback_obj.from_user.id, photo1, pablo_text, reply_markup=picasso_kb)
  bot.answer_callback_query(callback_query_id=callback_obj.id)

@bot.callback_query_handler(func=lambda call: call.data == "button2")
def callback_function2(callback_obj):
  photo2 = open('matiss.jpg', 'rb')
  bot.send_photo(callback_obj.from_user.id, photo2, matiss_text, reply_markup=matiss_kb)
  bot.answer_callback_query(callback_query_id=callback_obj.id)

@bot.callback_query_handler(func=lambda call: call.data == "but1")
def callback_picasso(callback_obj):
  bot.send_media_group(callback_obj.from_user.id, [InputMediaPhoto(open(photo, 'rb')) for photo in picassot])
  bot.answer_callback_query(callback_query_id=callback_obj.id)
  
@bot.callback_query_handler(func=lambda call: call.data == "but2")
def callback_matiss(callback_obj):
  bot.send_media_group(callback_obj.from_user.id, [InputMediaPhoto(open(photo, 'rb')) for photo in matisst])
  bot.answer_callback_query(callback_query_id=callback_obj.id)

bot.polling(none_stop=True)