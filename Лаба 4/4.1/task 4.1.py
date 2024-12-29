import json

def task() -> float:
    # Замените этот путь на актуальный путь к вашему JSON-файлу
    json_file_path = "C:/Users/magan/Desktop/Политех ДЗ/Питон/Лаба 4/data.json"

    # Инициализируем переменную для итоговой суммы
    total_sum = 0.0

    # Чтение данных из JSON файла
    with open(json_file_path, 'r') as file:
        data = json.load(file)

        # Вычисляем сумму произведений
        for entry in data:
            score = entry.get("score", 0)  # Получаем значение `score`, по умолчанию 0
            weight = entry.get("weight", 0)  # Получаем значение `weight`, по умолчанию 0
            total_sum += score * weight  # Суммируем произведения

    # Возвращаем сумму, округленную до 3 знаков после запятой
    return round(total_sum, 3)

# Пример вызова функции и печать результата
print(task())
