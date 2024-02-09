# import openai

# from aiogram import Bot, types , Dispatcher

# # from aiogram  import Dispatcher

# from aiogram.utils import executor

# token = '6979929059:AAHN931FGWveWWkEcrgVBNZG_ocRIx0Eaok'

# openai.api_key = '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'

# bot = Bot(token)
# dp = Dispatcher(bot)

# @dp.message_handler()
# async def send(message: types.Message):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo-16k-0613",
#         messages=[{"role": "system", "content":  + message.text}],
#         temperature=0.9,
#         max_tokens=1000,
#         top_p=1.0,
#         frequency_penalty=0.0,
#         presence_penalty=0.6,
#         stop=["You:"]
#     )
#     await message.answer(response['choices'][0]['text'])

# executor.start_polling(dp, skip_updates=True)


# import openai
# from aiogram import Bot, types, Dispatcher
# from aiogram.utils import executor

# # Токен Telegram бота
# telegram_token = '6979929059:AAHN931FGWveWWkEcrgVBNZG_ocRIx0Eaok'

# # Токен OpenAI
# openai.api_key = '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'

# bot = Bot(telegram_token)
# dp = Dispatcher(bot)

# @dp.message_handler()
# async def send(message: types.Message):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo-16k-0613",
#         messages=[{"role": "system", "content": "You:" + message.text}],
#         temperature=1,
#         max_tokens=1000,
#         top_p=1.0,
#         frequency_penalty=0.0,
#         presence_penalty=0.6
#     )
#     await message.answer(response['choices'][0]['message']['content'])

# executor.start_polling(dp, skip_updates=True)

import openai
from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor


telegram_token = '6979929059:AAHN931FGWveWWkEcrgVBNZG_ocRIx0Eaok'

openai.api_key = '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'

bot = Bot(telegram_token)
dp = Dispatcher(bot)

chat_history = {}

@dp.message_handler()
async def send(message: types.Message):
    if message.chat.id in chat_history:
        prev_message = chat_history[message.chat.id]
        chat_history[message.chat.id] = message.text
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k-0613",
            messages=[
                {"role": "system", "content": f"You: {prev_message}"},
                {"role": "user", "content": f"Bot: {message.text}"}
            ],
            temperature=1,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.6
        )
    else:
        chat_history[message.chat.id] = message.text
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k-0613",
            messages=[{"role": "user", "content": f"Bot: {message.text}"}],
            temperature=1,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.6
        )

    await message.answer(response['choices'][0]['message']['content'])

executor.start_polling(dp, skip_updates=True)
