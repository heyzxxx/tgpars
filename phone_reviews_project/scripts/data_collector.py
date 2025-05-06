import pandas as pd
from telethon import TelegramClient
from datetime import datetime
import os
import nest_asyncio
nest_asyncio.apply()

#не понял оставить данные или нет, но решил оставить, для верности. Но вообще можно свои вствить и канал поменять и то же самое будет
api_id = 
api_hash = 
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


    project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
    raw_data_dir = os.path.join(project_root, "data", "raw")
    os.makedirs(raw_data_dir, exist_ok=True)

  
    output_path = os.path.join(raw_data_dir, "meduzalive.csv")
    df.to_csv(output_path, index=False)
    print(f"✅ Сохранено {len(df)} сообщений в:\n{output_path}")


await fetch_messages()
