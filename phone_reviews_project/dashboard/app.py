import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


st.title("Анализ Telegram-канала @meduzalive")


df = pd.read_csv("../data/raw/meduzalive.csv", parse_dates=["date"])
df["length"] = df["text"].apply(lambda x: len(str(x)))
df["date_only"] = df["date"].dt.date
df["hour"] = df["date"].dt.hour


st.sidebar.header("Фильтры")

start_date = st.sidebar.date_input("Начальная дата", df["date_only"].min())
end_date = st.sidebar.date_input("Конечная дата", df["date_only"].max())

min_length, max_length = st.sidebar.slider("Длина текста", 0, int(df["length"].max()), (0, 2000))

keyword = st.sidebar.text_input("Ключевое слово")


filtered_df = df[(df["date_only"] >= start_date) & (df["date_only"] <= end_date)]
filtered_df = filtered_df[(filtered_df["length"] >= min_length) & (filtered_df["length"] <= max_length)]

if keyword:
    filtered_df = filtered_df[filtered_df["text"].str.contains(keyword, case=False, na=False)]


st.subheader("Общая статистика")
st.write(f"Количество постов: {len(filtered_df)}")
st.write(f"Диапазон дат: {filtered_df['date_only'].min()} — {filtered_df['date_only'].max()}")


st.subheader("Активность по часам")
hourly_counts = filtered_df["hour"].value_counts().sort_index()
fig, ax = plt.subplots()
hourly_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Час дня")
ax.set_ylabel("Количество постов")
st.pyplot(fig)


st.subheader("Облако слов")
text = " ".join(filtered_df["text"].dropna())
if text:
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
else:
    st.write("Недостаточно текста для генерации облака слов.")


st.subheader("Топ-10 постов по просмотрам")
st.dataframe(filtered_df.sort_values("views", ascending=False)[["date", "views", "text"]].head(10))
