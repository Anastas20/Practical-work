# Задание 1
from statistics import mean


def fact(x):
    if x <= 0:
        return 1
    else:
        return x * fact(x - 1)


# print(fact(int(input("Введите число факториал, которого хотите узнать"))))


# Задание 2

def filter_even(li):
    func = filter(lambda x: x % 2 == 0, li)
    list1 = list(func)
    return list1

# string = (input("Введите цифры через пробел")).split()
# string = [int(x) for x in string]

# print(filter_even(string))


# Задание 3

def square(li):
  li = list(map(lambda x: x*x, li))
  return li


# print(square(lst))


# Задание 4

def bin_search(li, element):
  first = 0
  last = len(li) - 1
  index = -1
  while index == -1 and first <= last:
    mid = (last + first) // 2
    if li[mid] == element:
      index = mid
    else:
      if element < li[mid]:
        last = mid - 1
      else:
        first = mid + 1
  return index


# lst = list(map(int, input("Введите цифры через пробел").split()))
# если ввели неотсортированный список и имеются повторяющиеся элементы
# lst = list(set(lst))
# lst.sort()

# el = int(input("Введите элемент, индекс которого необходимо найти"))

# print(bin_search(lst, el))


# Задание 5

def is_palindrome(string):
    string_copy = ""
    string = string.strip()
    string = string.lower()
    for i in range(len(string)):
        if string[i].isalpha():
            string_copy += string[i]
    len_str = len(string_copy)
    for i in range(len(string_copy)):
        if string_copy[i] != string_copy[len_str - 1 - i] and (i < len_str - 1 - i):
            return "NO"
        return "YES"


# print(is_palindrome(input("Введите строку ")))


# Задание 6


def calculate(path2file):
    operations={
        '+':lambda a,b:a+b,
        '-':lambda a,b:a-b,
        '*':lambda a,b:a*b,
        '//': lambda a,b:a//b,
        '%':lambda a,b:a%b,
        '**':lambda a,b:a**b
        }
    listout=[]
    with open(path2file, 'r') as finput:
        for expr in finput:
            expr = expr.strip().split('    ')
            if expr[0] in operations:
                listout.append(str(operations[expr[0]](int(expr[1]),int(expr[2]))))
    return ','.join(listout)



# Задание 7

import re


def substring_slice(path2file_1,path2file_2):
    with open(path2file_1, 'r') as text1:
        text1_lines = text1.readlines()
    with open(path2file_2, 'r') as text2:
        text2_lines = text2.readlines()
    outlist=[]
    t1_len = len(text1_lines)
    for i in range(t1_len):
        substrt2 = text2_lines[i].strip().split()
        outlist.append(text1_lines[i][int(substrt2[0]):int(substrt2[1])+1])
    return ' '.join(outlist)


# Задание 8



def decode_ch(sting_of_elements):
    import json
    import re
    periodic_table = json.load(open('periodic_table.json', "r", encoding="utf-8"))
    list1 = list(periodic_table.keys())  # список названий элементов
    print(list1)
    print(sting_of_elements)

    # разбиваем строку названий элементов
    list_elements = re.findall(r"[A-Z][a-z]?", sting_of_elements)
    print(list_elements)
    reduce_string = ""

    for i in list_elements:
        if i in list1:
            reduce_string = reduce_string + periodic_table[i]
    return reduce_string




# Задание 9


class Student:

    def __init__(self, name, surname, grades=[3, 4, 5]):
        self.name = name
        self.surname = surname
        self.fullname = name + ' ' + surname
        self.grades = grades

    def greeting(self):
        return 'Hello, I am Student'

    def mean_grade(self):
        return mean(self.grades)

    def is_otlichnik(self):
        return 'YES' if self.mean_grade() >= 4.5 else 'NO'

    def __add__(self, other):
        return self.name + ' is friends with ' + other.name

    def __str__(self):
        return self.fullname




# Задание 10

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)


