import pandas as pd
from telethon import TelegramClient
from datetime import datetime
import os
import nest_asyncio
nest_asyncio.apply()

# Вставь свои данные
api_id = 27691773
api_hash = '518514bab6ca37d91c944280dd2d60fa'
client = TelegramClient('meduza_session', api_id, api_hash)

async def fetch_messages():
    await client.start()
    messages = []

    async for message in client.iter_messages('meduzalive', limit=3000):
        if message.text:
            messages.append({
                'date': message.date,
                'text': message.text,
                'views': message.views,
                'forwards': message.forwards,
                'replies': message.replies.replies if message.replies else 0
            })

    df = pd.DataFrame(messages)

    # Определяем корень проекта и путь к data/raw
    project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
    raw_data_dir = os.path.join(project_root, "data", "raw")
    os.makedirs(raw_data_dir, exist_ok=True)

    # Сохраняем
    output_path = os.path.join(raw_data_dir, "meduzalive.csv")
    df.to_csv(output_path, index=False)
    print(f"✅ Сохранено {len(df)} сообщений в:\n{output_path}")

# Запуск
await fetch_messages()