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
    # print(file_types)
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

def mk_dict_equal_sizes(result):
    keys = list(result.keys())
    for k in keys:
        counter = list()
        for file_name in result[k]:
            counter.append([os.path.getsize(file_name), file_name])

        #print(counter)
        sizes_lst = list(map(lambda x: x[0], counter))
        # корректирую список оставляю только одинаковые размеры
        for itm in set(sizes_lst):
            if len(counter) == 1:
                counter.clear()
            elif sizes_lst.count(itm) == 1:
                tmp = (list(map(lambda x: x[0], counter))).index(itm)
                counter.pop(tmp)
        #корректирую результирующий словарь
        if len(counter) == 0:
            #result[k].clear()
            del result[k]
        elif len(counter) != len(result[k]):
            result[k] = list(map(lambda x: x[1], counter))
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    smbl = symbol()
    #sys.argv = ['~/PycharmProjects/EqualFilesNameHash/main.py', '/home/me/PycharmProjects/EqualFilesNameHash/samples/',
    #            '.txt']
    #sys.argv = ['F:\home\me\PycharmProjects\EqualFilesNameHash\main.py', 'D:\SERCEL', '.pdf']
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
    # получить словарь: ключ - имя файла, и полные пути до файлов с одинаковыми именами и размерами
    result = mk_dict_equal_sizes(result)
    print(*result)
    # печатаем красиво
    for k in result.keys():
        print(k)
        for n in result[k]:
            print('\t',n,'\t', os.path.getsize(n))
