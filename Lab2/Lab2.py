from csv import reader
import os
import random
import xml.dom.minidom as minidom


def get_table():
    try:
        with open('books.csv', 'r') as csvfile:
            table = list(reader(csvfile, delimiter=";"))
            return table
    except FileNotFoundError:
        print("Нет файла")
        return 0

def title_count(table):
    count = 0
    for line in table:
        if len(line[1]) > 30:
            count += 1
    print(count)
    input()
    return

def book_search(table):
    searchline = input("Введите автора: ")
    flag = 0
    for line in table:
        if searchline.lower() in line[3].lower() and float(line[7]) < 150:
            print(line[1])
            flag = 1
    if flag == 0:
        print("Таких авторов нет")
    input()

def gen(table):
    numbers = [random.randint(1, len(table) - 1) for x in range(20)]
    with open("out.txt", "w") as outfile:
        for number in numbers:
            line = table[number]
            outfile.write(f"{line[3]}. {line[1]} - {line[6]}\n")

def parsing():
    with open("currency.xml", "r") as xmlf:
        data = xmlf.read()
    dom = minidom.parseString(data)
    elements = dom.getElementsByTagName("Valute")
    valute_dict = {}
    for node in elements:
        for child in node.childNodes:
            if child.tagName == "Name":
                Name = child.firstChild.data
            if child.tagName == "Value":
                Value = child.firstChild.data
        valute_dict[Name] = Value
    for k in valute_dict.keys():
        print(k, valute_dict[k])
    input()

def tags(table):
    tags = set()
    for line in table[1:]:
        a = line[12].split("#")
        for i in a:
            tags.add("#" + i)
    for i in tags:
        print(i)
    input()

def popular(table):
    a = set()
    for line in table[1:]:
        a.add(int(line[8]))
    books = []
    a = sorted(a, reverse=True)
    for line in table[1:]:
        if int(line[8]) == a[0]: books.append(line[1])
    for i in range(20): print(books[i])
    input()

while True:
    os.system("cls")
    if get_table() == 0:
        input()
        break
    print(f"Меню:\n1 - кол. название больше 30 символов\n2 - Поиск по Автору\n3 - Генерация в файл\n"
          f"4 - Парсинг xml\n5 - Перечень тегов\n6 - популярные 20 книг")
    menu = input("Введите пункт меню: ")
    match menu:
        case "1":
            title_count(get_table())
        case "2":
            book_search(get_table())
        case "3":
            gen(get_table())
        case "4":
            parsing()
        case "5":
            tags(get_table())
        case "6":
            popular(get_table())
        case _:
            os.system("cls")
            break