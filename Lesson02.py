
import math
import random
import re

def date_enter():
    global list5
    enter5 = input("\n Введите дату в формате dd.mm.yyyy: ")
    list5 = enter5.split(".")
    date_check()

    return list5

def date_check():
    global list5
    if int(list5[0]) not in range(1, 32):
        print("\n Неверно указан день")
        date_enter()
    else:
        if int(list5[1]) not in range(1, 13):
            print("\n Неверно указан месяц")
            date_enter()
        else:
            if int(list5[2]) not in range(0, 3000):
                print("\n Неверно указан год")
                date_enter()
    return True

def main():
    answer = ''
    print("\n Lesson 02.")
    while answer != 'Q':
        print("\n Решим задачи:")
        print("\n [1] - EASY 1: Список по правой стороне")
        print("\n [2] - EASY 2: Вычитание одного списка из другого")
        print("\n [3] - EASY 3: Возврат числового списка через фильтр с расчетами")
        print("\n [4] - Normal 1: Извлечение корней из элементов списка с фильтром")
        print("\n [5] - Normal 2: Дата в текстовом формате")
        print("\n [6] - Normal 3: Список из произвольных чисел")
        print("\n [7] - Hard 1: Статистика по тексту")
        print("\n [8] - Hard 2: Разница между текстами")
        print("\n [Q] - Выход")
        answer = input("\n Какое задачу выбираешь? ")

        if answer == "1": # Easy 1
            print("\n EASY 1: Список по правой стороне")

            m = ["яблоко", "банан", "киви", "арбуз"]
            for i in range(len(m)):
                print(i + 1, ".", '{:>10}'.format(m[i]), sep='')
            input("\n Введите любой символ для продолжения...")

        elif answer == "2":  # Easy 2
            print("\n EASY 2: Вычитание одного списка из другого")

            a = ["яблоко", "банан", "киви", "арбуз", "сосиски", "вино", "вишня"]
            b = ["вишня", "виноград", "сосиски", "банан"]
            c = []

            for i in a:
                if i not in b:
                    c.append(i)
            print("\n Первый список: ", a)
            print("\n Второй список: ", b)
            print("\n Вычитание второго списка из первого", c)

            input("\n Введите любой символ для продолжения...")

        elif answer == "3":  # Easy 3
            print("\n EASY 3: Возврат числового списка через фильтр с расчетами")
            b = []
            a = [45, 98, 5552, 7, 8, 6565, 87, 323, 898, 555, 4578, 456421, 4, 0]

            for i in range(len(a)):
                if a[i] % 2 > 0:
                    b.append(a[i] * 2)
                else:
                    b.append(a[i] / 4)
            print("\n Исходный произвольный список: ", a)
            print("\n Четные элементы делим на 4, нечетные умножаем на 2")
            print("\n Итоговый список: ", b)

            input("\n Введите любой символ для продолжения...")

        elif answer == "4":  # Normal 1
            print("\n Normal 1: Извлечение корней из элементов списка с фильтром")
            a = [121, -98, 1225, 7, -9, 9801, 87, 323, 898, 169, 4578, 456421, 4, 0]
            b = []

            for i in range(len(a)):
                if a[i] >= 0:
                    b1 = math.sqrt(a[i])
                    if b1.is_integer():
                        b.append(int(b1))
            print("\n Исходный произвольный список: ", a)
            print("\n Список целых квадратных корней")
            print("\n Итоговый список: ", b)

            input("\n Введите любой символ для продолжения...")

        elif answer == "5":  # Normal 2
            print("\n Normal 2: Дата в текстовом формате")

            day = ["первое", "второе", "третье", "четвертое", "пятое", "шестое", "седьмое", "восьмое", "девятое",
                   "десятое", "одиннадцатое", "двенадцатое", "тринадцатое", "четырнадцатое", "пятнадцатое",
                   "шестнадцатое", "семнадцатое", "восемнадцатое", "девятнадцатое", "двадцатое", "двадцать первое", "двадцать второе",
                   "двадцать третье", "двадцать четвертое", "двадцать пятое", "двадцать шестое", "двадцать седьмое", "двадцать восьмое", "двадцать девятое", "тридцатое", "тридцать первое"]
            month = ("января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря")
            date_enter()
            if  date_check() == True:
                print("\n Вы ввели дату: ", day[int(list5[0]) - 1], month[int(list5[1]) - 1], list5[2], "года.")
            else:
                date_enter()

            input("\n Введите любой символ для продолжения...")

        elif answer == "6":  # Normal 3
            print("\n Normal 3: Список из произвольных чисел")

            c = []
            a = int(input("\n Введите количество элементов списка: "))
            for i in range(a):
                c.append(random.randint(-100, 100))
            print("\n Новый список: ", c)

            input("\n Введите любой символ для продолжения...")

        elif answer == "7":  # Hard 1
            print("\n Hard 1: Статистика по тексту")

            alphabet1 = []
            count = 0
            # Проверка для безграмотных, кто не ставит пробелы после знаков препинания
            text = input("\n Введите любой текст: ")
            word_list = re.findall('\w+', text) # \w+ ключ - все буквы. регулярные выражения

            alphabet = "abcdefghijklmnopqrstuvwxyz"
            for char1 in alphabet:
                alphabet1.append(char1)
            for word in word_list:
                for char2 in word:
                    if char2 in alphabet1:
                        count += 1
            print("\n Количество слов в тексте: ", int(len(word_list)))
            print("\n Количество букв латинского алфавита: ", count)

            input("\n Введите любой символ для продолжения...")

        elif answer == "8":  # Hard 2
            print("\n Hard 2: Разница между текстами")

            text1 = input("\n Введите первый текст: ")
            text2 = input("\n Введите второй текст: ")
            x = {}
            word_list1 = set(re.findall('\w+', text1))
            word_list2 = set(re.findall('\w+', text2))
            x = word_list1.intersection(word_list2)
            print("\n В обоих текстах встречаются эти слова: ", *x) # распаковка контейнера на составляющие

            input("\n Введите любой символ для продолжения...")


        else:
            print("\n Неизвестный ответ")

if __name__ == "__main__":
    main()