from datetime import datetime

datas = ["The Moscow Times - Wednesday, October 2, 2002",
         "The Guardian - Friday, 11.10.13",
         "Daily News - Thursday, 18 August 1977"]  # Входные данные

FORMATS = ['%A, %B %d, %Y', '%A, %d.%m.%y', '%A, %d %B %Y']  # Заданные форматы времени


def parse_data(data):  # Функция для перевода в объект datetime
    for format in FORMATS:
        try:
            return datetime.strptime(data, format)
        except:
            pass


for data in datas:
    data = data.split(' - ')  # Разделям строку на на список
    print(parse_data(data[1]))  # Выводим результат
