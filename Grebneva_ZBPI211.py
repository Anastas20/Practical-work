# Задание 1

def fact(x):
    if x <= 0:
        return 1
    else:
        return x * fact(x - 1)


print(fact(int(input("Введите число факториал, которого хотите узнать"))))


# Задание 2

def filter_even(li):
    func = filter(lambda x: x % 2 == 0, li)
    list1 = list(func)
    return list1

string = (input("Введите цифры через пробел")).split()
string = [int(x) for x in string]

print(filter_even(string))


# Задание 3

def square(li):
  li = list(map(lambda x: x*x, li))
  return li


lst = list(map(int, input("Введите цифры через пробел").split()))


print(square(lst))


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


lst = list(map(int, input("Введите цифры через пробел").split()))
# если ввели неотсортированный список и имеются повторяющиеся элементы
lst = list(set(lst))
lst.sort()

el = int(input("Введите элемент, индекс которого необходимо найти"))

print(bin_search(lst, el))


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


print(is_palindrome(input("Введите строку ")))


# Задание 6

import re

def calculate(path2file):
    print(path2file)
    global file_lines
    list_values = []

    for i in file_lines:
        digits = re.findall(r"[-\s]\d{1,6}", i)
        print(digits)
        digit1 = int(digits[0])
        digit2 = int(digits[1])
        if i[0] == "+":
            value = digit1 + digit2
        elif i[0] == "-":
            value = digit1 - digit2
        elif i[0] == "%":
            value = digit1 % digit2
        elif i[0] ==  "*" and i[1] == "*":
            value = digit1 ** digit2
        elif i[0] == "*" and i[1] != "*":
            value = digit1 * digit2
        elif i[0] == "/" and i[1] == "/":
            value = digit1 // digit2
        list_values.append(value)

    list_values = map(str, list_values)
    list_values = ",".join(list_values)
    return list_values




file = open("6.1", "r")

file_lines = file.readlines()
file.close()

with open("6.1") as file:
    print(calculate(file.read()))



# Задание 7

import re


def substring_slice(path2file_1, path2file_2):
    global lst1, lst2
    list_numbers = []
    # преобразуем числа из файла №2
    for i in lst2:
        list_numbers.append(re.findall(r"\d{1,101}", i))
    list1 = []
    for i in list_numbers:
        j = list(map(int, i))
        list1.append(j)

    new_string = []
    i = 0
    for string in lst1:
        digit1 = list1[i][0]
        digit2 = list1[i][1] + 1
        s = string[digit1:digit2]
        new_string.append(s)
        i += 1

    new_string = ' '.join(new_string)
    return new_string


with open("7.1") as lst1:
    lst1 = lst1.readlines()  # список строк
with open("7.1") as file1:
    file1 = file1.read()

with open("7.2") as lst2:
    lst2 = lst2.readlines()  # список строк чисел
with open("7.2") as file2:
    file2 = file2.read()

print(substring_slice(file1, file2))


# Задание 8

import json
import re

def decode_ch(sting_of_elements):
    global periodic_table  # словарь соответствий
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




periodic_table = json.load(open('periodic_table.json', "r", encoding="utf-8"))
print(periodic_table)

string = input("Введите названия элементов без разделителей")

print(decode_ch(string))


# Задание 9


class Student:


    def __init__(self, name, surname, *args):
        self.name = name
        self.surname = surname
        self.fullname = name + " " + surname
        self.grades = args
        if self.grades == ():
            self.grades = [3, 4, 5]



    def greeting(self):
        return "Hello, I am Student"


    def mean_grade(self):
        result = sum(self.grades) / len(self.grades)
        return result

    def is_otlichnik(self):
        if self.mean_grade() >= 4.5:
            return "YES"
        else:
            return "NO"

    def print(self):
        return self.fullname



st = Student("Ivan", "Ivanov", 4, 5)
print(st)
print(st.__dict__)
print(st.name)
print(st.greeting())
print(st.mean_grade())
print(st.is_otlichnik())
print(st.print())

st2 = Student("Denis", "Denisov", 2, 3, 4)
print(st2)
print(st2.__dict__)
print(st2.name)
print(st2.greeting())
print(st2.mean_grade())
print(st2.is_otlichnik())
print(st2.print())


