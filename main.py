#!/usr/bin/env python3

import glob
import sys
import os


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def symbol():
    if os.name == 'nt':
        return '\\'
    if os.name == 'posix':
        return '/'


def mk_file_list():
    file_list_dir = []
    file_types = sys.argv[-1]
    print(file_types)
    for target_path in sys.argv[1:-1]:
        if target_path[-1] != smbl:
            target_path += smbl  # добавляем в конец пути к директории слеш - будет искать во всех подпапках
        # print(target_path + '**' + smbl + '*' + file_types)
        file_list_dir.extend(glob.glob(target_path + '**' + smbl + '*' + file_types, recursive=True))
    set_fl_lst_dr = set(file_list_dir)  # исключаю повторы путей файлов
    return list(set_fl_lst_dr)


def mk_dict_equal_names(unic_name_list, name_list, file_list_dir):
    result = dict()
    for file_name in unic_name_list:
        # первое вхождение file_name в списке
        first_indx = name_list.index(file_name)
        if file_name in name_list[first_indx + 1:]:
            result_set = set()
            result_set.add(file_list_dir[first_indx])
            first_indx += 1
            while file_name in name_list[first_indx:]:
                first_indx = name_list.index(file_name, first_indx)
                result_set.add(file_list_dir[first_indx])
                first_indx += 1
            result[file_name] = result_set
            # print(result_set)

    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    smbl = symbol()
    sys.argv = ['~/PycharmProjects/EqualFilesNameHash/main.py', '/media/me/data/doc-i/', '.jpg']
    # получаю список путей файлов
    file_list_dir = mk_file_list()
    name_list = []  # только имена файлов

    for file_name in file_list_dir:
        name_list.append(file_name.split(smbl)[-1])

    unic_name_list = []  # список с уникальными/неповторимыми именами файлов
    unic_name_list = list(set(name_list))
    # получить словарь: ключ - имя файла, и полные пути до файлов с одинаковыми именами
    result = mk_dict_equal_names(unic_name_list, name_list, file_list_dir)

    print(*result)
