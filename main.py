# telegramBot6

# Телеграм-бот из библиотеки python-telegram-bot
# https://github.com/python-telegram-bot/v13.x-wiki/wiki/Introduction-to-the-API
# Получаем учетные данные бота, пользователя, посылаем сообщение пользователю

import telegram
from config import token

bot = telegram.Bot(token)

# Получение учетных данных бота (для проверки):
print(bot.get_me())  # Получим ответ в виде:
# {'can_join_groups': True, 'first_name': 'Test_bot', 'id': 1234567890, 'username': 'O**************_bot',
# 'supports_inline_queries': False, 'can_read_all_group_messages': False, 'is_bot': True}

# Отправим сообщение боту. Получаем данные пользователя (т.е мои)
updates = bot.get_updates()
print(updates[0])  # Получим ответ в виде:
# {'message': {'new_chat_members': [], 'supergroup_chat_created': False, 'entities': [], 'channel_chat_created': False,
# 'date': 1671134012, 'message_id': 33, 'photo': [], 'delete_chat_photo': False,
# 'chat': {'id': 123456*****, 'first_name': 'Александр', 'type': 'private'},
# 'group_chat_created': False, 'caption_entities': [], 'text': 'Анекдот', 'new_chat_photo': [],
# 'from': {'is_bot': False, 'language_code': 'ru', 'id': 123*********, 'first_name': 'Александр'}}, 'update_id': 12345*}

# Мы копируем id пользователя и посылаем ему сообщение
bot.send_message(text='Hi!', chat_id=112****78)

