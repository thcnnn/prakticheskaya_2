import sys
import os
import shutil
class Path_exception(Exception):
    def __init__(self, message='Операция вне рабочей папки'):
        self.message = message
        super().__init__(self.message)
def valid_path(name):
    with open("/home/vboxuser/test_1/proekt_2/file_manager/config.txt", 'r') as file:
        path = file.readline()
    work_dir_abs = os.path.abspath(path)
    file_path_abs = os.path.abspath(name)
    if os.path.commonpath([work_dir_abs, file_path_abs]) != work_dir_abs:
        raise Path_exception
    return True
def operation(type_file, type_operation):
    name = input(f'Введите название {type_file}: ')
    if valid_path(name):
        try:
            if type_file == 'папки':
                if type_operation == '1':
                    os.mkdir(name)
                if type_operation == '2':
                    os.rmdir(name)
                if type_operation == '3':
                    os.chdir(name)
            if type_file == 'файла':
                if type_operation == '4':
                    text_file = open(name, 'w')
                    text_file.close()
                if type_operation == '5':
                    try:
                        fill = input('Введите текст: ')
                        text_file = open(name, 'w')
                        text_file.write(fill)
                        text_file.close()
                    except:
                        print('Ошибка названия')
                        operation(type_file, type_operation)
                if type_operation == '6':
                    text_file = open(name, 'r')
                    print(text_file.read())
                    text_file.close()
                if type_operation == '7':
                    os.remove(name)
                if type_operation == '8':
                    dest = input('Введите папку: ')
                    if valid_path(dest):
                        try:
                            shutil.copy(name, dest)
                        except:
                            print('Ошибка названия')
                            operation(type_file, type_operation)
                if type_operation == '9':
                    dest = input('Введите папку: ')
                    if valid_path(dest):
                        try:
                            shutil.move(name, dest)
                        except:
                            print('Ошибка названия')
                            operation(type_file, type_operation)
                if type_operation == '10':
                    try:
                        new_name = input('Введите новое название файла: ')
                        os.rename(name, new_name)
                    except:
                        print('Ошибка названия')
                        operation(type_file, type_operation)
        except Exception as msg:
            print(msg)
            operation(type_file, type_operation)






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
        if a in ['1', '2', '3']:
            operation('папки', a)
        if a in ['4', '5', '6', '7', '8', '9', '10']:
            operation('файла', a)
        if a == '11':
            break

if __name__ == "__main__":
    main()