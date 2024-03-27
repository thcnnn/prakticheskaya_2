import sys
import os
import PySimpleGUI as pg

def valid_path(config_path, path):
    # if len(path.split(r'/')) == 1:
    #     return True
    # elif config_path.split()
    pass
def create_directory():
    try:
        name = input('Введите название папки: ')
        os.mkdir(name)
    except FileNotFoundError:
        print('Ошибка названия')
        create_directory()

def delete_directory():
    try:
        name = input('Введите название папки: ')
        os.rmdir(name)
    except FileNotFoundError:
        print('Ошибка названия')
        delete_directory()
def change_directory():
    try:
        name = input('Введите название папки: ')
        os.chdir(name)
    except FileNotFoundError:
        print('Ошибка названия')
        change_directory()
def main():
    with open("config.txt", 'r') as file:
        path = file.readline()
        os.chdir(path)
    while True:
        print('Рабочий каталог:', os.getcwd())

        print('Доступны команды:')
        print("1. Создание папки (с указанием имени)")
        print("2. Удаление папки по имени")
        print("3. Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх")
        print('4. Создание пустых файлов с указанием имени')
        print('5. Запись текста в файл')
        print('6. Просмотр содержимого текстового файла')
        print('7. Удаление файлов по имени')
        print('8. Копирование файлов из одной папки в другую')
        print('9. Перемещение файлов')
        print('10. Переименование файлов')
        print('11. Выйти из выполнения кода')
        a = input('Введите цифру нужной операции: ')
        if a == '1':
            create_directory()
        if a == '2':
            delete_directory()
        if a == '3':
            change_directory()
        if a == '11':
            break

if __name__ == "__main__":
    main()