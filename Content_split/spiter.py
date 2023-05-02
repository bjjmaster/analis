import textract
import re


def find_index(ints, item):
    indexes = [i for i, j in enumerate(ints) if j == item]
    return indexes


def splitter_sample(path):
    text = textract.process(path)  # получаем текст по пути
    text = text.decode("utf-8").lower().split()  # превращаем в список и нижний регистр

    content_finder_sample_start = text.index(
        "содержание")  # находит индекс содержания в шаблоне для  вычленения начала  - 203
    content_finder_sample_end = find_index(text, "1.")[1]  # тут я ищу 1. чтобы найти конец содержания
    list_of_content_sample = text[
                             content_finder_sample_start + 1: content_finder_sample_end]  # список с содержанием(сырым)

    digital_dict_content_split = {} # тут значения с разбиты сплитом на буд
    digital_dict_content = {}

    for i in list_of_content_sample:
        if re.search(r"\d", i) != None and "." not in i:
            list_of_content_sample.remove(i)  # это нужно для удлания страниц
    l = ""
    l_list = []
    digital_list_content = []  # лист с цифрами содержания
    for j in list_of_content_sample:
        if re.search(r"\d", j) == None:  # тут надо пофиксить создание списка
            l = l + " " + j
        else:
            l_list.append(l)
            digital_list_content.append(j)
            l = ""
    l_list = l_list[1:]
    for x in range(len(l_list)):
        digital_dict_content_split.setdefault(digital_list_content[x], l_list[x].strip().split()) # если надо будет чтобы добовлялся список то тут добавить split у l_list[x].strip().split()
        digital_dict_content.setdefault(digital_list_content[x], l_list[x].strip())


    return digital_dict_content_split, digital_dict_content


