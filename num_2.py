import plotly.express as px
import pandas as pd
import os

path = "udemy_courses_extended.csv"

# Проверяем, существует ли файл
if not os.path.exists(path):
    print('Файл не найден!')
    exit()

# Открываем файл в режиме чтения
with open(path) as file:
    if os.fstat(file.fileno()).st_size:
        df = pd.read_csv(path, sep=",")
    else:
        print('Файл пуст!')
        exit()

# (1) Создание гистограммы с использованием функции count
fig = px.histogram(df, x="is_paid", y="num_subscribers",  # Определяем оси X и Y
                   color='is_paid', barmode='group',  # Настройка цвета и группировки столбцов
                   height=400,  # Высота графика
                   histfunc="count",  # Функция агрегирования данных (подсчет)
                   text_auto=True,  # Автоматическое отображение значений на столбцах
                   title="Количество платных и бесплатных курсов",  # Заголовок графика
                   )

# Отображение гистограммы
fig.show()

# (2) Создание гистограммы с использованием функции max
fig2 = px.histogram(df, x="is_paid", y="num_subscribers",
                    color='is_paid', barmode='group',
                    height=400,
                    histfunc="max",
                    text_auto=True,
                    title="Максимальное количество подписчиков"
                    )

fig2.show()

# (3) Создание гистограммы с использованием функции avg
fig3 = px.histogram(df, x="is_paid", y="num_subscribers",
                    color='is_paid', barmode='group',
                    height=400,
                    histfunc="avg",
                    text_auto=True,
                    title="Среднее количество подписчиков"
                    )

fig3.show()

# (4) Создание гистограммы с использованием функции min
fig4 = px.histogram(df, x="is_paid", y="num_subscribers",
                    color='is_paid', barmode='group',
                    height=400,
                    histfunc="min",
                    text_auto=True,
                    title="Минимальное количество подписчиков"
                    )

fig4.show()

# (5) Анализ платных курсов
paid = df[df["is_paid"] == True]  # Отбираем только платные курсы

# Создание гистограммы платных курсов по уровням
fig4 = px.histogram(paid, x="level", y="course_title",
                    color='level', barmode='group',
                    height=400,
                    histfunc="count",
                    text_auto=True,
                    title="Количество курсов по уровням (Только платные)"
                    )

fig4.show()

# (6) Анализ бесплатных курсов
unpaid = df[df["is_paid"] == False]  # Отбираем только бесплатные курсы

# Создание гистограммы бесплатных курсов по уровням
fig5 = px.histogram(unpaid, x="level", y="course_title",
                    color='level', barmode='group',
                    height=400,
                    histfunc="count",
                    text_auto=True,
                    title="Количество курсов по уровням (Только бесплатные)"
                    )

fig5.show()
