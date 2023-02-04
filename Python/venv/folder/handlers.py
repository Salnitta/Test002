from aiogram import types
from loader import dp
from random import randint as RI

max_total = 150
total = 0
game = False

@dp.message_handler(commands = ['start', 'старт'])
async def mes_start(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f'{name}, привет!\n'
                         f'Сыграем в конфеты?\n'
                         f'Узнать больше: /help\n' 
                         f'Играть: /game\n')


@dp.message_handler(commands = ['help'])
async def mes_help(message: types.Message):
    await message.answer(f'На столе лежит заданное количество конфет. '
                         f'Играют два игрока, делая ход друг после друга. '
                         f'Первый ход определяется жеребьёвкой. '
                         f'За один ход можно взять от 1 до 28 конфет. '
                         f'Выигрывает тот, кто сделал последний ход.\n'
                         f'Чтобы задать конфеты, набери:\n'
                         f"/set 'количество'\n"
                         f'(например, /set 200)\n'
                         f'Чтобы начать игру, набери:\n'
                         f'/game')


@dp.message_handler(commands=['game'])
async def mes_new_game(message: types.Message):
    global total
    global max_total
    global game
    game = True
    total = max_total
    name = message.from_user.first_name
    first_turn = RI(0, 1)
    if first_turn:
        await message.answer(f'Игра началась. На столе {total} конфет. '
                             f'По жребию первым ходит {name}.\n'
                             f'{name}, возьми конфеты:')
    else:
        await message.answer(f'Игра началась. На столе {total} конфет. '
                             f'По жребию первым ходит Бот.')
        await bot_turn(message)


@dp.message_handler(commands=['set'])
async def mes_set(message: types.Message):
    global max_total
    global game
    name = message.from_user.first_name
    number = message.text.split()[1]
    if not game:
        if number.isdigit():
            max_total = int(number)
            await message.answer(f'Задано новое количество конфет - {max_total}.\n'
                                 f'Чтобы начать игру, нажми /game')
        else:
            await message.answer(f'{name}, напишите цифрами')
    else:
        await message.answer(f'{name}, нельзя менять правила во время игры, возьми конфеты:') 
    

@dp.message_handler()
async def mes_candy(message: types.Message):
    global total
    global game
    name = message.from_user.first_name
    number = message.text
    if game:
        if number.isdigit() and 0 < int(number) < 29:
            total -= int(number)
            if total <= 0:
                await message.answer(f'{name} взял {number} конфет. '
                                     f'На столе осталось {total} и {name} победил!\n'
                                     f'Чтобы играть снова, нажми /game')
                game = False
            else:
                await message.answer(f'{name} взял {number} конфет. '
                                    f'На столе осталось {total}.')
                await bot_turn(message)
        else:
            await message.answer(f'{name}, укажи цифрами количество конфет от 1 до 28')
    else:
        await message.answer(f'{message.from_user.first_name}, это бот для игры в конфеты.\n'
                             f'Чтобы начать игру, нажми /game')


async def bot_turn(message):
    global total
    global game
    bot_take = 0
    if 0 < total < 29:
        bot_take = total
        total -= bot_take
        await message.answer(f'Бот взял {bot_take} конфет. '
                         f'На столе осталось {total} и Бот победил!\n'
                         f'Чтобы играть снова, нажми /game')
        game = False
    else:
        remainder = total % 29
        bot_take = remainder if remainder != 0 else RI(1, 28)
        total -= bot_take
        await message.answer(f'Бот взял {bot_take} конфет. '
                             f'На столе осталось {total}.\n'
                             f'{message.from_user.first_name}, возьми конфеты:')







