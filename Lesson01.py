
import math

def main():
    answer = ''
    print("\n Lesson 01.")
    while answer != 'Q':
        print("\n Решим задачи:")
        print("\n [1] - EASY 1: Вывод цифр произвольного целого числа")
        print("\n [2] - EASY 2: Замена исходных значений двух переменных")
        print("\n [3] - EASY 3: Запрос доступа по возрасту")
        print("\n [4] - Normal 1: Нахождение наибольшей цифры в числе с помощью арифметики и while")
        print("\n [5] - Normal 1: Нахождение наибольшей цифры в числе с помощью for")
        print("\n [6] - Normal 2: Замена исходных значений двух переменных")
        print("\n [7] - Normal 3: Вычисление корней квадратного уравнения")
        print("\n [8] - Hard 1: Определение простого числа")
        print("\n [9] - Hard 2: Определение n-го числа Фибоначчи")
        print("\n [10] - Hard 3: AAA и BBB")
        print("\n [Q] - Выход")
        answer = input("\n Какое задачу выбираешь?")

        if answer == "1": # Easy 1
            a = str(input("\n Введите любое целое число: "))

            while answer != 'Q':
                print("\n [1] - EASY 1: Решение через арифметику и while")
                print("\n [2] - EASY 1: Решение через длину числа и for")
                print("\n [3] - EASY 1: Решение через длину числа и while")
                print("\n [Q] - Выход")
                answer = input("\n Какое решение выбираешь? (1/2/3/Q)")

                if answer == "1":
                    print("\n Решение через арифметику и while")
                    b = int(a)
                    i = 0
                    y = 0
                    while b - y > 0:
                        x = ((b - (b % 10 ** i)) // 10 ** i) % 10
                        print(x)
                        y = y + x * 10 ** i
                        i = i + 1

                elif answer == "2":
                    print("\n Решение через длину числа и for")
                    for i in range (len(a)):
                        print(a[i])

                elif answer == "3":
                    print("\n Решение через длину числа и while")
                    b = 0
                    while b < len(a):
                        print(a[b])
                        b = b + 1
                else:
                    print("\n Неизвестный ответ, попробуйте еще раз")

        elif answer == "2": # Easy 2
            print("\n Замена исходных значений")
            a = input("\n Введите любое число или слово: ")
            print("\n a =", a)
            b = input("\n Введите любое другое число или слово: ")
            print("\n b =", b)
            c = a
            a = b
            b = c
            print("\n Меняем значения:")
            print("\n a =", a)
            print("\n b =", b)
            input("\n Введите любой символ для продолжения...")

        elif answer == "3": # Easy 3
            print("\n Запрос доступа по возрасту")
            ageanswer = int(input("\n Введите Ваш возраст (количество полных лет цифрами): "))
            if ageanswer >= 18:
                print("\n Доступ разрешен")
            else:
                print("\n Извините, пользование данным ресурсом только с 18 лет")
            input("\n Введите любой символ для продолжения...")

        elif answer == "4": # Normal 1
            print("\n Нахождение наибольшей цифры в числе с помощью арифметики и while")
            a = input("\n Введите произвольное целое число:")
            b = int(a)
            i = 0
            y = 0
            x2 = 0
            while b - y > 0:
                x = ((b - (b % 10 ** i)) // 10 ** i) % 10
                y = y + x * 10 ** i
                if x2 < x:
                    x2 = x
                    i = i + 1
                else:
                    i = i + 1
            print("\n Максимальная цифра в данном числе ", x2)
            input("\n Введите любой символ для продолжения...")

        elif answer == "5": # Normal 1
            print("\n Нахождение наибольшей цифры в числе с помощью for")
            a = input("\n Введите произвольное целое число:")
            x2 = 0
            for b in range(len(a)):
                c = int(a[b])
                if x2 < c:
                    x2 = c
                else:
                    continue
            print("\n Максимальная цифра в данном числе ", x2)
            input("\n Введите любой символ для продолжения...")

        elif answer == "6": # Normal 2
            print("\n Замена исходных значений двух переменных")
            a = input("\n Введите любое число или слово: ")
            print("\n a =", a)
            b = input("\n Введите любое другое число или слово: ")
            print("\n b =", b)
            print("\n Было: ", a,b)
            a,b = b,a
            print("\n Меняем значения:")
            print("\n Стало: ", a,b)
            input("\n Введите любой символ для продолжения...")

        elif answer == "7": # Normal 3
            print("\n Вычисление корней квадратного уравнения типа: ax² + bx + c = 0")
            a = int(input("\n Введите число a: "))
            b = int(input("\n Введите число b: "))
            c = int(input("\n Введите число c: "))
            d = b ** 2 - 4 * a * c
            print("\n Вычисляем D = b² - 4ac =", d)
            if d > 0:
                x1 = (b * (-1) + math.sqrt(d)) / (2 * a)
                x2 = (b * (-1) - math.sqrt(d)) / (2 * a)
                print("\n D > 0, получаем 2 корня: ")
                print("\n x1 =", x1)
                print("\n x2 =", x2)
            elif d == 0:
                x1 = b / 2 * a * (-1)
                print("\n D = 0, получаем 2 одинаковых корня: ")
                print("\n x1 = x2 = ", x1)
            else:
                print("\n D < 0, следовательно, урованение не имеет решения")

            input("\n Введите любой символ для продолжения...")

        elif answer == "8":  # Hard 1
            print("\n Определение простого числа")
            a = int(input("\n Введите любое число: "))
            y = 0
            for i in range(2, int(math.sqrt(a)) + 1):
                x = a % i
                if x == 0:
                    y = 1
                    break
            if y == 1:
                print("\n Число", a, "не является простым, так как делится на", i)
            else:
                print("\n Число", a, "простое")
            input("\n Введите любой символ для продолжения...")

        elif answer == "9":  # Hard 2
            print("\n Определение n-го числа Фибоначчи")
            n = int(input("\n Введите n: "))
            x = [0, 1]
            for i in range(2, n):
                x.insert(i, x[i - 1] + x[i - 2])
            print("\n", n, "-ое число Фибоначчи =", x[i])
            input("\n Введите любой символ для продолжения...")

        elif answer == "10":  # Hard 3
            print("\n AAA и BBB")
            n = int(input("\n Введите n (количество строк): "))
            m = int(input("\n Введите m (количество ячеек ААА): "))
            x = []
            for i in range(1, m + 1):
                x.insert(i, "AAABBB" * i)
            for y in range(1, n + 1):
                print(x[m - 1])
            input("\n Введите любой символ для продолжения...")

        else:
            print("\n Неизвестный ответ")

if __name__ == "__main__":
	main()
