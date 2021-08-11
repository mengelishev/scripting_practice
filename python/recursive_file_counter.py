#!/usr/bin/env python

# Рекурсивно считает количество файлов в директории принимая на вход
# Путь к директории. Например: "/home/user/"

import os

# Рекурсивный подсчет количества файлов в директории
def get_num_files(path):
    num_files = 0
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            num_files += 1
        if os.path.isdir(full_path):
            num_files += get_num_files(full_path)
    return num_files

# Альтернативная реализация используя модуль os.walk()
def get_subdir(path):
    for full_path, directory, file in os.walk(path):
        print("\n")
        print("Full path: " + str(full_path))
        print("Directory: " + str(directory))
        print("Name of file: " + str(file))
        print("Количество файлов: " + str(len(file)))
        print("\n")

if __name__ == '__main__':
    path = input("Введите путь к директории: ")
    print("\nВ директории: {} = {} файлов".format(path, get_num_files(path)))
    get_subdir(path)