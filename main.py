with open("purchase_log.txt", "r", encoding="utf-8") as f:    # Открываем файл с нужной кодировкой
    purchase = {}                                             # Создаем словарь
    for line in f.readlines():                                # Считываем файл
        slovar = eval(line.strip())                           # Инициализирвуем считанные строки
        if slovar['user_id'] != 'user_id':                    # Ставим условия, чтоб не попадал мусор
            purchase[slovar['user_id']] = slovar['category']  # Добавляем в словарь данные

for key, value in purchase.items():                           # Производим вывод данных построчно
    print(key, value)