import plotly.express as px
import pandas as pd
import os

# Определение пути к CSV-файлу
path = "data_country.csv"

# Проверка существования файла
if not os.path.exists(path):
    print('Файл не найден!')
    exit()

# Открытие файла в режиме чтения
with open(path) as file:
    # Проверка размера файла (пуст ли он)
    if os.fstat(file.fileno()).st_size:
        df = pd.read_csv(path, delimiter=',')  # Чтение данных из CSV в DataFrame
    else:
        print('Файл пуст!')
        exit()

# Переименование столбцов DataFrame для понятности
df.columns = ['Country', 'Health Expenditure', 'Income', 'Inflation', 'Life Expectancy']

# Транспонирование данных (меняем местами строки и столбцы)
data_transposed = df.iloc[:, 1:].T  # Выбираем все столбцы кроме первого и транспонируем

# Создание тепловой карты с помощью plotly.express
fig = px.imshow(data_transposed,
                y=df.columns[1:],  # Ось Y - названия показателей (кроме первого столбца)
                x=df['Country'],  # Ось X - названия стран
                labels={  # Названия осей и значений
                    "x": "Country",
                    "y": "Indicator",
                    "color": "Value"
                },
                title="Тепловая карта стран и их показателей",  # Заголовок тепловой карты
                width=800,  # Ширина тепловой карты
                height=600,  # Высота тепловой карты
                text_auto=True  # Автоматическое отображение значений в ячейках
                )

# Настройка поведения при наведении курсора (отключение подсветки промежутков)
fig.update_traces(hoverongaps=False)

# Режим наведения: отображение ближайшего значения
fig.update_layout(hovermode="closest")

# Отображение тепловой карты
fig.show()
