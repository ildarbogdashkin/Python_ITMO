# from csv import reader
# import os
# from datetime import datetime
#
#
# def find_string(searchline, line):
#     lower_case = line.lower()
#     index = lower_case.find(searchline.lower())
#     return index
#
#
# def get_table():
#     try:
#         with open('civic.csv', 'r') as csvfile:
#             table = list(reader(csvfile, delimiter=";"))
#             return table
#     except FileNotFoundError:
#         print("НЕТ ИДИ НАХУЙ")
#         return 0
#
#
# def search(table):
#     searchline = input("Шаблон: ")
#     if searchline in ["0", ""]:
#         return 0
#     output = open("result", "w")
#     flag = 0
#     output.write(f"Поиск от {datetime.today()}\n\n")
#     for line in table:
#         if find_string(searchline, line) != -1:
#             res_line = f'{line[0]}. {line[2]}. S/n: {line[18]}. Цена: {line[8]} руб.'
#             print(res_line)
#             output.write(f'{res_line}\n')
#             flag += 1
#     if flag == 0:
#         print("Нету нихера")
#         output.write(f"Нету нихера")
#     else:
#         print(f"Найдено позиций: {flag}")
#     input()
#     output.close()
#
# def search_ID(table):
#     searchline = input("ID: ")
#     if searchline in ["0", ""]:
#         return 0
#     flag = 0
#     with open('civic.csv', 'r') as csvfile:
#         table = reader(csvfile, delimiter=";")
#         for line in table:
#             if searchline == line[0]:
#                 res_line = f'{line[0]}. {line[2]}. S/n: {line[18]}. Цена: {line[8]} руб.'
#                 print(res_line)
#             else:
#                 print("Нету нихера")
#         input()
#
# while True:
#     os.system("cls")
#     if get_table() == 0:
#         input()
#         break
#     print(f"Меню:\n1 - поиск по названию\n2 - Поиск по ID\n0 - Выход")
#     menu = input("Введите пункт меню: ")
#     match menu:
#         case "1":
#             search(get_table())
#         case "2":
#             search_ID(get_table())
#         case "0":
#             break
#         case _:
#             print("НЕТ ИДИ НАХУЙ")
#             input()


# import xml.dom.minidom as minidom
#
#
# xml_file = open("books.xml")
# xml_data = xml_file.read()
# dom = minidom.parseString(xml_data)
# dom.normalize()
#
# elements = dom.getElementsByTagName("book")
# books_dict = {}
#
# for node in elements:
#     for child in node.childNodes:
#         if child.nodeType == 1:
#             if child.tagName == "author":
#                 if child.firstChild.nodeType == 3:
#                     author = child.firstChild.data
#             if child.tagName == "title":
#                 if child.firstChild.nodeType == 3:
#                     title = child.firstChild.data
#     books_dict[author] = title
#
#
#     if node.getAttribute("id") == "bk105":
#         print(node.getElementsByTagName("author")[0].firstChild.data)


# print(books_dict)
# for key in books_dict.keys():
#     print(key, books_dict[key])

xml_file.close()
