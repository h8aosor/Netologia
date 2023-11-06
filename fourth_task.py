import re


def func(car_id):
    number_car = re.findall(r'^\D\d{3}\D{2}', car_id)  # Определяем номер машины через регулярное выражение
    region_car = re.findall(r'\d{2,3}$', car_id)  # Определяем регион машины через регулярное выражение
    if len(number_car) == 1 and len(region_car) == 1:  # Проверяем наличие правильности введенных данных и выводим
        # соответствующий результат
        return f'Номер {number_car[0]} валиден. Регион: {region_car[0]}.'
    else:
        return f'Номер не валиден'


print(func('А222BС16'))
