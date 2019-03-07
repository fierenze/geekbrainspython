
import random
from collections import Counter


def print_menu(menu):
    for i,m in enumerate(menu, start=1):
        print (f"{i}. {m}")

def get_command(menu):
    command = int(input("Choose command: "))
    if 1<= command <= len(menu):
        return command
    else:
        return -1

def easy1():
    c = []
    a = input("Ведите любые числа через запятую: ")
    b = a.split(",")
    print(b)
    for i in b:
        c.append(int(i)**2)
    print(c)


def easy2():
    a = ["яблоко", "виноград", "киви", "малина", "клубника", "ананас", "мед", "сельдерей", "морковь"]
    b = ["мед", "виноград", "малина", "картофель", "молоко", "яица", "сельдерей", "сметана", "творог"]
    с = list(set(a) & set(b))
    print("\n Первый список: ", a)
    print("\n Второй список: ", b)
    print("\n Пересекающийся список: ", с)
    print("\n")


def easy3():
    a = []
    b = []
    for i in range(50):
        a.append(random.randint(-100,100))
    print(a)
    for j in a:
        if (j % 3) == 0 and j >= 0 and (j % 4) != 0:
            b.append(j)
    print(b)

# Normal 1

def findnum():
    a = []
    for i in range(2500):
        a.append(random.randint(0, 9))
    z = ''.join(map(str, a))
    return z

def findint():
    global file_name
    count = 0
    count_max = 0
    k_max = 0
    y = []
    countdict = {}
    with open(file_name, "r") as f:
        k = list(f.read())
        for i in range(len(k)):
            countdict.setdefault(k[i], 0)
            if k[i] == k[i-1]:
                count += 1
            else:
                count = 0
            if countdict[k[i]] <= count:
                countdict[k[i]] = count
                if count_max < count:
                    count_max = count
                    k_max = k[i]
        for i in range(count_max):
            y.append(k_max)
        print("\n Самая длинная серия повторов: ", "".join(y))
        # проверка
        # print(z)
        # print(k)
        # print(count_max)
        # print(k_max)
        # print(countdict)
        # print(len(k))

def normal1():
    global file_name
    file_name = "int2500.txt"
    with open(file_name, "w") as f:
        f.write(findnum())
    findint()
    f.close()

def normal2():
    a = int(input("\n Введите размер матрицы: "))
    matrix = []
    for i in range(a):
        count = 0
        row = []
        while True:
            for j in range(a):
                element = random.randint(0, 9)
                row.append(element)
                if element == 0:
                    count += 1
            if count == 1:
                break
            else:
                row = []
                count = 0
        matrix.append(row)

    for i in range(len(matrix)):
        for j in range(a):
            print(matrix[i][j], end = " ")
        print()
    print("\n")

def hard1():

    pass

def hard2():
    pwds = []
    with open(r"C:\Users\User\Desktop\Python\GeekBrainsPython\pwd.txt", "r") as f:
        for line in f.readlines():
            a = []
            a.append(line.split(";"))
            pwds.append(a[0][1][:-1])
        for i, m in enumerate(Counter(pwds).most_common(10), start=1):
            print(f"{i}. Пароль {m[0]} {m[1]} раз")
        print("\n")
    f.close()


menu = ["Easy 1. Список квадратов", "Easy 2. Сравнение списков продуктов", "Easy 3. Списки с произвольными числами", "Normal 1. Число с 2500 цифр", "Normal 2. Матрица с 0 в строке", "Не сделано - Hard 1. Куб на просвет", "Hard 2. Пароли", "Не сделано - Hard 3. Спиральная матрица", "Quit"]
commands = [easy1, easy2, easy3, normal1, normal2, hard1, hard2, exit]

while True:
    print_menu(menu)
    command = get_command(menu)
    if command == -1:
        print("Wrong command!")
        continue
    commands[command-1]()