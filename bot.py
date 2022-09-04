#!venv/bin/python
import logging
from aiogram import Bot, Dispatcher, executor, types
import random
from config import TOKEN

# Объект бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

raw_data = open('slovaraffirmacii.txt', 'r')
modern_data = raw_data.readlines()

raw_data1 = open('slovar_predskazanii.txt', 'r')
modern_data1 = raw_data1.readlines()


# Хэндлер на команду /test1

# from aiogram import types
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1, button_2, button_3 = types.KeyboardButton(text="Хочу аффирмацию!"), "Хочу предсказание из печеньки!", "❓ Контакты разработчика"
    keyboard.add(button_1)
    keyboard.add(button_2)
    keyboard.add(button_3)
    await message.answer("Привет, {0.first_name}! Я Могу прислать тебе аффирмацию, которая сделает твой день лучше и продуктивнее! Скорее воспользуйся мной!".format(
                         message.from_user), reply_markup=keyboard)

@dp.message_handler(content_types='text')
async def commands(message: types.Message):
    if message.text == "привет":
        await message.answer('Привет')

    elif message.text == "Хочу аффирмацию!":
        await message.answer(random.choice(modern_data))

    elif message.text == "Хочу предсказание из печеньки!":
        await message.answer(random.choice(modern_data1))

    elif message.text == "❓ Контакты разработчика":
        keyboard = types.ReplyKeyboardMarkup()
        types.ReplyKeyboardRemove()
        btn1, btn2, btn3 = types.KeyboardButton(
            text="Телеграм"), "Гитхаб", "Вернуться назад"
        keyboard.add(btn1, btn2)
        keyboard.add(btn3)
        await message.answer("какой именно контакт вам нужен?", reply_markup=keyboard)

    elif message.text == "Телеграм":
        await message.answer("@Grasmurr")

    elif message.text == "Гитхаб":
        await message.answer("https://github.com/Grasmurr")

    elif message.text == "Вернуться назад":
        keyboard = types.ReplyKeyboardMarkup()
        types.ReplyKeyboardRemove()
        button_1, button_2, button_3 = types.KeyboardButton(
            text="Хочу аффирмацию!"), "Хочу предсказание из печеньки!", "❓ Контакты разработчика"
        keyboard.add(button_1)
        keyboard.add(button_2)
        keyboard.add(button_3)
        await message.answer("Возвращаюсь обратно..", reply_markup=keyboard)

    else:
        await message.answer("На такую комманду я не запрограммировал..")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



#!venv/bin/python
import logging
from aiogram import Bot, Dispatcher, executor, types
import random

# Объект бота
bot = Bot(token="5767877240:AAEtty-bIkAhtqv3-VYRQHDrqPsToR1TBfM")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

raw_data = open('slovaraffirmacii.txt', 'r')
modern_data = raw_data.readlines()

raw_data1 = open('slovar_predskazanii.txt', 'r')
modern_data1 = raw_data1.readlines()


# Хэндлер на команду /test1

# from aiogram import types
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1, button_2, button_3 = types.KeyboardButton(text="Хочу аффирмацию!"), "Хочу предсказание из печеньки!", "❓ Контакты разработчика"
    keyboard.add(button_1)
    keyboard.add(button_2)
    keyboard.add(button_3)
    await message.answer("Привет, {0.first_name}! Я Могу прислать тебе аффирмацию, которая сделает твой день лучше и продуктивнее! Скорее воспользуйся мной!".format(
                         message.from_user), reply_markup=keyboard)

@dp.message_handler(content_types='text')
async def commands(message: types.Message):
    if message.text == "привет":
        await message.answer('Привет')

    elif message.text == "Хочу аффирмацию!":
        await message.answer(random.choice(modern_data))

    elif message.text == "Хочу предсказание из печеньки!":
        await message.answer(random.choice(modern_data1))

    elif message.text == "❓ Контакты разработчика":
        keyboard = types.ReplyKeyboardMarkup()
        types.ReplyKeyboardRemove()
        btn1, btn2, btn3 = types.KeyboardButton(
            text="Телеграм"), "Гитхаб", "Вернуться назад"
        keyboard.add(btn1, btn2)
        keyboard.add(btn3)
        await message.answer("какой именно контакт вам нужен?", reply_markup=keyboard)

    elif message.text == "Телеграм":
        await message.answer("@Grasmurr")

    elif message.text == "Гитхаб":
        await message.answer("https://github.com/Grasmurr")

    elif message.text == "Вернуться назад":
        keyboard = types.ReplyKeyboardMarkup()
        types.ReplyKeyboardRemove()
        button_1, button_2, button_3 = types.KeyboardButton(
            text="Хочу аффирмацию!"), "Хочу предсказание из печеньки!", "❓ Контакты разработчика"
        keyboard.add(button_1)
        keyboard.add(button_2)
        keyboard.add(button_3)
        await message.answer("Возвращаюсь обратно..", reply_markup=keyboard)

    else:
        await message.answer("На такую комманду я не запрограммировал..")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



