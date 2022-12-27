# курс https://stepik.org/course/68343/


# задачка на поиск наибольшего колличества одинаковых символов подряд
coin = input() + 't'
counter = 1
counterMax = []
for i in range(len(coin) - 1):
    if coin[i] == coin[i + 1]:
        counter += 1
    else:
        counterMax.append(counter)
        counter = 1
print(max(counterMax))


# 2.2 шаг 10
# https://stepik.org/lesson/415554/step/10?auth=login&unit=405083
# вывести номера строк, которые содержат комбинация букв a n t o n
n = int(input())

position = []
for i in range(1, n+1):
    counter = 0
    temp = ' '.join(input())
    s = [i for i in temp.split() if i in 'anton']
    for j in 'anton':
        if j in s:
            s = s[s.index(j) + 1:]
            counter += 1
    if counter >= 5:
        position.append(i)

print(*position, sep=' ')


# 2.2 шаг 11
# https://stepik.org/lesson/415554/step/11?auth=login&unit=405083
# поочередно удалять из строки буквы алфавита
s = input()
alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
s1 = '{0} запретил букву'.format(s)
for i in alph:
    if i in s1:
        print(s1.strip(), i)
        s1 = s1.replace(i, '')
        s1 = s1.replace('  ', ' ')


# bool тип данных
#   False = 0, True = 1
#   оператор and - умножение
#   оператор or - сложение
#   not - отрицание
#   Пример логических выражение:
#   False and True == False, True and True == True, True or False == True, not True == False

# функция bool() приводит типы данных к булевуму по следующей логике:
#   строки: пустая строка — ложь (False), непустая строка — истина (True)
#   числа: нулевое число — ложь (False), ненулевое число (в том числе и меньшее нуля) — истина (True)
#   списки: пустой список — ложь (False), непустой — истина (True)


# Вложенные списки, двойная/тройная индексация
# Работа с вложенными списками принципиально ничем не отличается от работы со списками
# к элементам вложенных списков/самим вложенными спискам можно так - же обращаться по индексам
my_list = ['Python', [10, 20, 30], ['Beegeek', 'Stepik!']]

print(my_list[0][2])       # индексирование строки 'Python', двойная индексация
print(my_list[1][1])       # индексирование списка [10, 20, 30], двойная индексация
print(my_list[2][-1])      # индексирование списка ['Beegeek', 'Stepik!'], двойная индексация
print(my_list[2][-1][-1])  # индексирование строки 'Stepik!', тройная индексация


# при использовании max() на вложенных списках списки сравниваются поэлементно
list1 = [[1, 7], [1, 7, 90], [1, 10]]  # max(list1) == [1, 10]
list2 = [['a', 'b'], ['a', 'b', 'c'], ['c', 'b']]  # max(list2) == [c, b]


# двойная/тройная индексация для обращения к вложенному списку и добавления в него элемента/другого списка
# двойная
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

# тройная
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']
list1[2][1][2].extend(sub_list)
print(list1)



# 4.2 шаг 12
# https://stepik.org/lesson/416752/step/16?auth=login&unit=406260
# пример задания на работу с вложенными списками
# вывести число: сумму всех чисел списка list1 разделённую на общее количество всех чисел.
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0

for li in list1:
    counter += len(li)
    for i in li:
        total += i
print(total/counter)


# В Python списки – ссылочный тип данных. Конструкция [0] * m возвращает ссылку на список из m нулей.
# Повторение этого элемента n раз создает список из n ссылок на один и тот же список.
# То есть если изменить любой список созданный через подобную конструкцию - изменятся все и остальные
# https://stepik.org/lesson/416753/step/1?auth=login&unit=406261
# 4.3 шаг 1
n, m = int(input()), int(input())

my_list = [[0] * m] * n
my_list[0][0] = 17

print(my_list)


# пример создания вложенного списка с помощью генераторов
n = int(input())
lst = [[i for i in range(1, n + 1)] for i in range(3)]
lst[0][0] = 5
print(lst)



# 4.3 шаг 10
# https://stepik.org/lesson/416753/step/10?auth=login&unit=406261
# Треугольник Паскаля 1
import math
n = int(input())


def pascal(numOfString):
    psclString = [int(math.factorial(numOfString)/(math.factorial(elem)*(math.factorial(numOfString-elem)))) for elem in range(numOfString+1)]
    return psclString


print(pascal(n))



# 4.3 шаг 12
# https://stepik.org/lesson/416753/step/12?auth=login&unit=406261
# упаковка дубликатов, все повторяющиеся символы должны быть записаны как вложенные списки
# основной список - содержит в себе списки с последовательностями одинаковых элементов
def createList(lst):
    lst = lst.split()
    temp = []
    fin = []
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            temp.append(lst[i+1])
        else:
            temp.append(lst[i])
            fin.append(temp.copy())
            temp.clear()

    for i in lst[-1:]:
        for j in lst[lst.index(i) - 1:]:
            if i == j:
                temp.append(j)
            else:
                temp.append(i)
                fin.append(temp.copy())
                temp.clear()
                break
        break
    if len(temp) != 0:
        fin.append(temp)
    return fin


s = input()


print(createList(s))


# МАТРИЦЫ/методы s.rjust(width, fillchar) и ljust(width, fillchar)
# rjust - выравнивание по правому краю
# width - минимальная длина строки,
# fillchar - символ, которым будет заполняться строка, если len(s) < width

# ljust() - выравнивание по левому краю, парметры как у rjust() параметры
# при выравнивании по левому краю символы строки сдвигаются к левому краю а справа строка заполняется символами fillchar до len(s) == width



# 4.4 шаг 9
# https://stepik.org/lesson/416754/step/9?auth=login&unit=406262
# матрицы, вывести матрицу, потом поменять местами строки со столбцами и вывести
n = int(input())  # кол-во строк
m = int(input())  # кол-во столбцов
matrix = [[input() for i in range(m)] for _ in range(n)]  # создаю матрицу с n строк и m столбцов (вложенный список с n элементов и m элементов внутри самих списков)

# вывожу матрицу
for i in range(len(matrix)):  # запускаю цикл по всем строкам матрицы (элментам верхнего списка)
    print()
    for j in range(len(matrix[i])):  # запускается цикл по всем столбцам (по всем элементам вложенного списка)
        print(matrix[i][j], end=' ')

print()



# инвертирование строк и столбцов
# так - как надо поменять строк и столбцы местами - вывести сначала все первые элементы каждого вложенного списка на одной строке,
# потом все вторые элементы каждого вложенного списка на новой строке и тд
# поэтому при двойной индексации увеличивает первое число - элемент верхнего списка до окончания всех элементов верхнего списка
# потом только начинает увеличиваться второй индекс - номер элемента внутри вложенного цикла (для матриц: увеличивается номер строки до окончания строк, потом номер столбца)
for i in range(len(matrix[0])):  # запускается цикл длиной элемента (длина всех вложенных списков одинаковая)
    print()
    for j in range(len(matrix)):  # запускается цикл по всей матрице
        print(matrix[j][i], end= ' ')  # в двойной индексации увеличиваются сначала элементы верхнего списка до их окончания, потом увеличивается номер выводимого элемента внутри вложенного списка

# в контексте матриц это значит, что мы двигаемся по строкам, выводя сначла первый столбец, пройдя все строки начинается выводить второй столбец и так далее
# и первой строкой новой матрицы будет - первый столбец старой матрицы, так как мы выводим все из первого столбца, потом
# переходим на новую строку и выводим все из второго столбца и так далее



# 4.5 шаг 2
# https://stepik.org/lesson/416755/step/2?auth=login&unit=406263
# Программа должна вывести два числа: номер строки (вложенного списка) и номер столбца (номер элемента вложенного спиcка),
# в которых стоит наибольший элемент таблицы (верхнего списка).

n = int(input())  # кол-во строк
m = int(input())  # кол-во столбцов
matrix = [[int(i) for i in input().split()] for _ in range(n)]  # создаю матрицу (список с глубиной 2)

# записываю в максимум первый элемент первого вложенного списка (первый элемент матрицы)
maximum = max(matrix[0])  # запоминаю максимум из первого вложенного списка (строки матрицы)
ind = 0  # номер элемента внутри верхнего списка (в каком вложенном списке максимум)

for i in range(len(matrix)):  # запускаю цикл по всем вложенным элементам верхнего списка (по всем строкам матрицы)
    if maximum < max(matrix[i]):  # если максимум во вложенном списке (строке матрицы) > чем имеющийся
        maximum = max(matrix[i])  # ставлю максимум найденный элемент
        ind = i  # запоминаю номер вложенного списка, в котором находится элемент (номер строки матрицы)
print(ind, matrix[ind].index(maximum))  # вывожу номер вложенного списка (номер строки матрицы) и первое вхождение этого максимума во вложенный список

matrix[ind].index(maximum)  # конструкция по поиску первого вхождения максимума во вложенном списке (в строке матрицы)



# 4.5 шаг 3
# https://stepik.org/lesson/416755/step/3?auth=login&unit=406263
# Напишите программу, которая меняет местами столбцы в матрице. (поменять во всех вложенных списках пары элементов местами)
n = int(input())
m = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

i, j = [int(s) for s in input().split()]  # множественное присваивание по элементам списка, список [1, 2], i = 1, j = 2

for l in range(len(matrix)):
    matrix[l][i], matrix[l][j] = matrix[l][j], matrix[l][i]

for k in matrix:
    print(*k)


# 4.5 шаг 8
# https://stepik.org/lesson/416755/step/8?auth=login&unit=406263

# На вход программе подаются координаты коня на шахматной доске в шахматной нотации
# (то есть в виде e4, где сначала записывается номер столбца (буква от a до h, слева направо),
# затем номеру строки (цифра от 11 до 88, снизу вверх)).

# Программа должна вывести на экран изображение доски, разделяя элементы пробелами.

possible_columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # возможные значения столбца на шахматной доске
deck = [['.' for _ in range(8)] for _ in range(8)]  # создаю шахматную доску (список глубиной 2, где вложенный список - строка доски)

column, row = [i for i in ' '.join(input()).split()]  # получаю позицию коня на доске (множественное присваивание)
column = possible_columns.index(column)  # номер столбца перевожу из буквенного значения в численное

row = 8 - int(row)  # строки на доске идут снизу вверх, то есть в обратном порядке (вложенные списки идут от 6 до 1)

# print(column, row)

for i in range(len(deck)):  # цикл по всем строка доски (по всем элементам верхнего списка)
    for j in range(len(deck[i])):  # цикл по всем столбцам полученной строки (по всем элементам вложенного списка)
        # print(i, j)
        if i == row and j == column:  # если найденная строка и найденный столбец доски равны позиции коня на доске
            # print(i, j)
            deck[i][j] = 'N'  # ставлю коня в найденную позицию

        if (i == row + 2 or i == row - 2) and (j == column + 1 or j == column - 1):  # нахожу позиции, в которые конь может ходить
            deck[i][j] = '*'

        if (j == column + 2 or j == column - 2) and (i == row + 1 or i == row - 1):  # нахожу позиции, в которые конь может ходить - 2
            deck[i][j] = '*'

for i in range(8):  # вывод доски с найденной позицией коня и ячейками, в которые он может ходить
    print(*deck[i])



# 4.5 шаг 9
# https://stepik.org/lesson/416755/step/9?auth=login&unit=406263
# Задание
# Магическим квадратом порядка nn называется квадратная таблица размера n×n, составленная из всех чисел 1, 2, 3, ... n**2
# так, что суммы по каждому столбцу,
# каждой строке
# и каждой из двух диагоналей равны между собой.
# Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.

# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы: n строк, по n чисел в каждой, разделённые пробелами.

n = int(input())  # получаю число n - размер матрицы

matrix = [[int(i) for i in input().split()] for _ in range(n)]  # создаю матрицу размером n

flag = True  # по умолчанию считаем, что матрица - магический квадрат

# числа от 1 до n**2 находятся в матрице
for i in range(1, n**2+1):  # запускается цикл по всем числам, которые должны быть в матрице
    # if str(i) in ''.join(str(k) for k in matrix):  # каждое число проверяется на вхождение в матрицу, через генератор, не совсем понимаю, как работает

    # каждое число проверяется на вхождение в матрицу, создаю новый список генератором на основе списка глубиной 2 (матрицы),
    # запуская цикл по элементам верхнего списка for lst in matrix (типы элементов - list), затем по элементам внутреннего списка for i in lst (типы элементов int)
    # полученный int вношу в свой список
    if i in [int(i) for lst in matrix for i in lst]:
        pass
    else:
        flag = False  # если число не вошло - считаем, что матрица не магический квадрат
        break

if flag:  # если все необходимые числа вошли в матрицу
    matrix_elem_sum = sum(matrix[0])  # переменная хранит суммы элементов вложенных списков
    sub_summ = 0  # суммы элементов побочной диагонали
    main_summ = 0  # суммы элементов главной диагонали

    for i in range(len(matrix)):

        # если суммы строк совпадают
        if matrix_elem_sum == sum(matrix[i]):  # если сумма элементов очередного вложенного списка - совпадает с другими
            pass
        else:
            flag = False  # иначе, считаем, что матрица не магический квадрат

        column_matrix_elem_sum = 0  # счетчик элементов суммы элементов столбца внутри матрицы (i-ых элементов всех вложенных списков)
        for j in range(len(matrix[i])):
            column_matrix_elem_sum += matrix[j][i]  # прохожусь по всем i-м элементам каждого вложенного списка (по элементу каждой строки iго столбца)

            # суммы главной и побочной диагоналей
            if i == j:  # если элемент лежит на главной диагонали
                main_summ += matrix[i][j]  # увеличиваю счетчик
            if j == n - i - 1:  # если элемент лежит на побочной диагонали
                sub_summ += matrix[i][j]

        # если суммы столбцов совпадают
        if i == 0:  # для первого столбца матрицы (для нулевых элементов всех воженных списков) нет столбца для сравнения, делаю исключения на первой итерации цикла
            prev = column_matrix_elem_sum  # запоминаю сумму элементов первого столбца (суммы iых элемнтов всех вложенных списков)
        if column_matrix_elem_sum == prev:  # на следующих итерациях сравниваю суммы остальных столбцов с суммой первого (суммых iых элементов с суммой нулевых элементов всех вложенных списков)
            pass
        else:
            flag = False

    if flag and main_summ == sub_summ:  # если считаем матрицу магическим квадратом и суммы элементов основной и побочной диагонали - равны
        print('YES')  # выводим, что матрица магический квадрат
    else:
        print('NO')

else:
    print('NO')



# 5.1 шаг 3
# https://stepik.org/lesson/416759/step/3?unit=406267
# Задание из экзамена
# Траспонированная матрица (столбцы поменены местами со строками)
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

temp = [[matrix[j][i] for j in range(len(matrix[i]))] for i in range(len(matrix))]

for li in temp:
    print(*li)

# КОРТЕЖИ
# Списки – изменяемые коллекции, строки – неизменяемые последовательности Unicode символов.
# В Python имеются и неизменяемые последовательности содержащие,
# в отличие от строк, абсолютно произвольные данные. Такие коллекции называются кортежами (tuple, читается "тюпл").

# Кортежи поддерживают те же операции, что и списки, за исключением изменяющих содержимое.
numbers = (1, 2, 3)

# index()
numbers.index(1)  # 0

# count()
numbers.count(2)  # 1

# len()
len(numbers)  # 3

# sum()
sum(numbers)  # 6

# min()
min(numbers)  # 1

# min()
max(numbers)  # 3

# Кортежи поддердивают срезы и индексирование
print(numbers[0])  # 1
print(numbers[1:2])  # 2, 3

# распаковка кортежа
print(*numbers)

# str()
print(str(numbers))  # (1, 2, 3)


# join()
numbers = ('First', 'Second', 'Third')
print('-'.join(numbers))  # First-Second-Third

# сравнение кортежей
print((1, 8) == (1, 8))  # True
print((1, 8) != (1, 10))  # True
print((1, 9) < (1, 2))  # False
print((2, 5) < (6,))  # True
print(('a', 'bc') > ('a', 'de'))  # False


# Встроенная функция list() может применяться для преобразования кортежа в список.
number_tuple = (1, 2, 3, 4, 5)
number_list = list(number_tuple)  # [1, 2, 3, 4, 5]

# Встроенная функция tuple() может применяться для преобразования списка в кортеж.
str_list = ['один', 'два', 'три']
str_tuple = tuple(str_list)  # ('один', 'два', 'три')

# с помощью преобразования кортежа в список можно внести изменения в кортеж
writer = ('Лев Толстой', 1827)
a = list(writer)
a[1] = 1828
writer = tuple(a)  # ('Лев Толстой', 1828)


# 6.2 шаг 14
# https://stepik.org/lesson/444816/step/14?unit=434982
# в переменных city_year, city_name содержится год основания города и его название соответсвенно
# переменная city должна содержать кортеж названия города и даты его основания
city_name = input()
city_year = int(input())
city = (city_name, city_year)  # кортеж можно сделать через (x, y)
print(city)


# чтобы отсортировать список можно воспользовать sorted() - не путать с sorted()
not_sorted_tuple = (34, 1, 8, 67, 5, 9, 0, 23)
sorted_tuple = tuple(sorted(not_sorted_tuple))  # sorted() возвращает отсортрованный список на основании кортежа
print(sorted_tuple)  # (0, 1, 5, 8, 9, 23, 34, 67)


# изменение списков пример
poet_data = ('Пушкин', 1799, 'Санкт-Петербург')  # неизменяемый кортеж с 3мя элементами

poet_data = list(poet_data)  # перевожу кортеж в список
poet_data[2] = 'Москва'  # изменяю элемент в списки, который создан на основании кортежа

print(tuple(poet_data))  # перевожу измененные данные в тип кортежей



# 6.3 шаг 9
# https://stepik.org/lesson/443990/step/9?unit=434154
# На вход программе подается натуральное число nn, далее следует nn строк с фамилией школьника и его оценкой на каждой из них.
# Программа должна вывести сначала все введённые строки с фамилиями и оценками учеников в том же порядке.
# Затем следует пустая строка, а затем выводятся строки с фамилиями и оценками хорошистов и отличников (в том же порядке).

n = int(input())  # получаю кол-во вводимых строк
grades = [tuple(input().split()) for _ in range(n)]  # из каждой строки делаю кортеж из фамилии и оценки, запуская генератор с кол-вом итераций  == кол-во строк

well_grades = [tu for tu in grades if int(tu[1]) >= 4]  # создаю список кортежей с хорошистами/отличниками, на основе списка с кортежами всех оценок


for tu in grades:  # запускаю цикл по всем оценкам
    print(*tu)  # запускаю цикл по списку кортежей со всеми оценками, вывожу распакованный кортеж

print()

for tu in well_grades:  # запускаю цикл по списку кортежей с хорошими оценками
    print(*tu)  # распаковываю полученный кортеж кортеж



# 6.3
# РАСПАКОВКА КОРТЕЖЕЙ
# https://stepik.org/lesson/443990/step/10?unit=434154
# ПРИ РАСПАКОВКЕ КОРТЕЖЕЙ МОЖНО ИСПОЛЬЗОВАТЬ ПЕРЕМЕННУЮ, СОДЕРЖАЩУЮ НЕСКОЛЬКО ЗНАЧЕНИЙ
tup = ('a', 'b', 'c')
a, *any = tup  # *any содержит все значений из кортежа tup, которые не были присвоены после "a" и ЯВЛЯЕТСЯ СПИСКОМ
# такие переменные могут быть пустыми или иметь одно значение и все равно будут спискам

a = 1,  # не распаковка, а просто присвоение
b, = 1,  # распаковка
# распаковываться могут любые последовательности (списки, строки, кортежи)


# строковый метод partition()
# partition() принимает на вход один аргумент sep, разделяет строку при первом появлении sep и возвращает кортеж, состоящий из трех элементов:
#    часть перед разделителем, сам разделитель и часть после разделителя.
# Если разделитель не найден, то кортеж содержит саму строку, за которой следуют две пустые строки.

s1 = 'abc-de'.partition('-')  # ('ab', '-', 'de')
s2 = 'abc-de'.partition('.')  # ('abc-de', '', '')
s3 = 'abc-de-fgh'.partition('-')  # ('abc', '-', 'de-fgh')


