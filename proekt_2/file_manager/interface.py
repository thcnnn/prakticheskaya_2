import PySimpleGUI as sg
from main import *
#import ctypes
#ctypes.windll.shcore.SetProcessDpiAwareness(1)
main_layout = [[sg.Button('Создание папки (с указанием имени)'), sg.Button('Удаление папки по имени')]]
window = sg.Window('Файловый менеджер', main_layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break