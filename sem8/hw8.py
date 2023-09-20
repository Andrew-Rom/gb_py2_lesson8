"""
HW 8
Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.
"""
import csv
import json
import os
import pickle


def get_file_list(sourse_dir: str):
    sourse_dir_content = []
    for dir_path, dirs_name, files_name in os.walk(sourse_dir):

        if dirs_name and not os.path.dirname(dir_path):
            for dir_name in dirs_name:
                sourse_dir_content.append([dir_name,
                                           dir_path,
                                           'dir',
                                           get_dir_size(os.path.join(sourse_dir, dir_name))])

        elif dirs_name and os.path.dirname(dir_path):
            for dir_name in dirs_name:
                sourse_dir_content.append([dir_name,
                                           os.path.basename(dir_path),
                                           'dir',
                                           get_dir_size(os.path.join(dir_path, dir_name))])

        for file_name in files_name:
            sourse_dir_content.append([file_name,
                                       os.path.basename(dir_path),
                                       'file',
                                       os.path.getsize(os.path.join(dir_path, file_name))])

    return sourse_dir_content


def get_dir_size(explore_dir: str):
    dir_size = 0
    for path, dirs, files in os.walk(explore_dir):
        for file in files:
            dir_size += os.path.getsize(os.path.join(path, file))
    return dir_size


def create_json_file(data):
    with open('dir_content.json', mode='w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def create_csv_file(data):
    with open('dir_content.csv', mode='w', encoding='UTF-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for line in data:
            writer.writerow(line)


def create_pickle_file(data):
    with open('dir_content.pickle', 'wb') as file:
        pickle.dump(data, file)


def create_dir_content(path: str = 'gb_react'):
    lst = get_file_list(path)
    create_json_file(lst)
    print(f'The content of directory {path} was saved in dir_content.json')
    create_csv_file(lst)
    print(f'The content of directory {path} was saved in dir_content.csv')
    create_pickle_file(lst)
    print(f'The content of directory {path} was saved in dir_content.pickle')


if __name__ == '__main__':
    create_dir_content()
