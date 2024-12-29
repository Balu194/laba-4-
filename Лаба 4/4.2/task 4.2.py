import csv
import json
from collections import OrderedDict

input_filename = "C:/Users/magan/Desktop/Политех ДЗ/Питон/лаб 4/4.2/input.csv"
output_filename = "C:/Users/magan/Desktop/Политех ДЗ/Питон/лаб 4/4.2/output.json"

def task() -> None:
    # Считываем содержимое CSV файла
    with open(input_filename, mode='r', newline='', encoding='utf-8') as csvfile:
        #  DictReader для чтения CSV и преобразования его в словари
        reader = csv.DictReader(csvfile)

        # Преобразуем строки в список словарей
        data = [OrderedDict(row) for row in reader]

    # Сериализуем данные в JSON формате с отступами 4
    with open(output_filename, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

if __name__ == '__main__':
    # Выполняем задачу
    task()

    # Читаем и печатаем содержимое JSON файла для проверки
    with open(output_filename) as output_f:
        for line in output_f:
            print(line, end="")
