import requests


def rate():
    index = 0  # Объявляем переменную, с помощью которой будем отлавливать индекс максимального курса
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    a = requests.get(url)
    valuates = list(a.json()['Valute'].keys())  # Собираем все ключи валют из словаря
    max_rate = a.json()['Valute'][valuates[0]][
        "Value"]  # Объявляем переменную с максимальный курсом и присваимваем значение первой валюты из списка

    for i in range(len(valuates)):  # Перебираем в цикле значение всех валют
        if float(max_rate) <= float(
                a.json()['Valute'][valuates[i]]["Value"]):  # С помощью перебора находим валюту с максимальным значением
            max_rate = a.json()['Valute'][valuates[i]]["Value"]
            index = i  # Находим индекс максимальной валюту
    return a.json()['Valute'][valuates[index]]["Name"]  # Возвращаем название валюты с максимальным курсом


print(rate())
