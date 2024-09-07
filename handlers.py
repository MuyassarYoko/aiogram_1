import requests
from aiogram import Router, html, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

router = Router()

main_commands = [
    'Menu',
    'lang',
    'Orders history',
    'Тех под'
]


@router.message(CommandStart())
async def start_handler(message: Message):
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Menu'), KeyboardButton(text='lang')],
        [KeyboardButton(text='Orders history')],
        [KeyboardButton(text='Тех под')],
    ])

    await message.answer(f'''
Hello, {html.italic(message.from_user.username)}
Id: {message.from_user.id}
''', reply_markup=kb)


@router.message(Command('do', 'work'))
async def do_handler(message: Message):
    await message.answer(message.text)


# @router.message(F.text == 'Menu')
# async def menu_handler(message: Message):
#     await message.answer("This is your menu: ")

@router.message(F.text.in_(main_commands))
async def main_commands_handler(message: Message):
    if message.text == 'Menu':
        await message.answer("This is your menu: ")
    elif message.text == 'lang':
        await message.answer("ru")
        await message.answer("en")
    else:
        await message.answer("I")


@router.message(Command("users"))
async def message_handler(message: Message):
    data = requests.get('reqres.in/api/users?per_page=12').json()
    # while True:
    #     result = {
    #         'id': data.data.id,
    #         'first_name': data.data.first_name,
    #         'last_name': data.data.last_name
    #     }
    # # print(result)
    #     await message.answer(f'{result}')

    txt = ''

    for i in data['data']:
        txt += i['id'] + i['first_name'] + i['last_name']



