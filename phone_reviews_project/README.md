# Анализ Telegram-канала @meduzalive

## Описание
Проект исследует активность, тематику и вовлечённость аудитории Telegram-канала @meduzalive. Данные собраны напрямую с помощью Telegram API и библиотеки Telethon. Проведена очистка, анализ и визуализация данных, а также реализован интерактивный дашборд.

## Структура проекта
```
.
├── README.md              <- описание проекта
├── requirements.txt       <- список библиотек
├── notebooks/
│   └── template.ipynb     <- основной ноутбук с анализом
├── scripts/
│   └── data_collector.py  <- парсер данных из Telegram
├── data/
│   └── raw/
│       └── meduzalive.csv <- собранные данные
├── dashboard/
│   └── app.py             <- интерактивный дашборд на Streamlit
```

## Установка и запуск

1. Установите зависимости:
pip install -r requirements.txt

2. (Опционально) Соберите данные:
python scripts/data_collector.py

3. Запустите дашборд:
cd dashboard
streamlit run app.py

## Автор 
**Чернышев Артём**

**ИСУ:467996**
