import PySimpleGUI as sg
from main import *
import sys
if sys.platform == 'win32':
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
main_layout = [[sg.Button('Создание папки (с указанием имени)'), sg.Button('Удаление папки по имени'), sg.Button('Перемещение между папками')],
               [sg.Button('Создание пустых файлов с указанием имени'), sg.Button('Запись текста в файл'), sg.Button('Просмотр содержимого текстового файла')],
               [sg.Button('Удаление файлов по имени'), sg.Button('Копирование файлов из одной папки в другую'), sg.Button('Перемещение файлов'), sg.Button('Переименование файлов')]]
window = sg.Window('Файловый менеджер', main_layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event in ['Создание папки (с указанием имени)', 'Удаление папки по имени', 'Перемещение между папками']:
        var = 1 if event == 'Создание папки (с указанием имени)' else 2 if event == 'Удаление папки по имени' else 3
        dir_layout = [[sg.Text('Введите папку'), sg.InputText('', key='path'), sg.Button('Ок')]]
        dir_window = sg.Window('', dir_layout,size=(500, 100))
        while True:
            event, values = dir_window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Ок':
                for_interface('папки', str(var), name=values['path'])
                dir_window.close()
                sg.popup('Операция выполнена')
    elif event in ['Создание пустых файлов с указанием имени', 'Просмотр содержимого текстового файла','Удаление файлов по имени']:
        var = 4 if event == 'Создание пустых файлов с указанием имени' else 6 \
            if event == 'Просмотр содержимого текстового файла' else 7
        file_layout = [[sg.Text('Введите файл'), sg.InputText('', key='path'), sg.Button('Ок')]]
        file_window = sg.Window('', file_layout, size=(500, 100))
        while True:
            event, values = file_window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Ок':
                for_interface('файла', str(var), name=values['path'])
                file_window.close()
                sg.popup('Операция выполнена')
    else:
        var = 5 if event == 'Запись текста в файл' else 8 if event == 'Копирование файлов из одной папки в другую' else 9 \
        if event == 'Перемещение файлов' else 10
        file_d_layout = [[sg.Text('Введите первый путь/название'), sg.InputText('', key='path')],
                         [sg.Text('Введите второй путь/название'), sg.InputText('', key='path2')],
                         [sg.Button('Ок')]]
        file_d_window = sg.Window('', file_d_layout, size=(500, 100))
        while True:
            event, values = file_d_window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Ок':
                for_interface('файла', str(var), name=values['path'], name2=values['path2'])
                file_d_window.close()
                sg.popup('Операция выполнена')