#Урок 10. Лекция. Функции высшего порядка, работа с файлами

# def f(x):
#     return x * x
# a = f
# print(a(5))
# print(f(5))


#Создание калькулятора
# def calk1(a, b):
#     return a+b
# def calk2(a, b):
#     return a*b
# def math(op, x, y):
#     print(op(x, y))
# math(calk2, 5, 45)


# Лямдо функция
# def calk2(a, b):
#     return a*b
# def math(op, x, y):
#     print(op(x, y))

# math(lambda a,b: a + b, 5, 45)


# Задача №1
# В списке хранится числа. Нужно выбрать только чётный числа и составить список пар (число; квадрат числа):
# Прмер: 1 2 3 5 8 15 23 38
# Получить: [(2,4), (8,64), (38,1444)]

# Решение №1:
# Создаем список чисел
# numbers = [1, 2, 3, 5, 8, 15, 23, 38]
# # Создаем пустой список для хранения пар
# pairs = []
# # Проходим по всем числам в списке
# for number in numbers:
#   # Проверяем, является ли число четным
#   if number % 2 == 0:
#     # Вычисляем квадрат числа
#     square = number ** 2
#     # Добавляем пару (число, квадрат) в список
#     pairs.append((number, square))
# # Выводим список пар на экран
# print(pairs)

# Решение №2:
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# for i in data:
#   if i % 2 == 0:
#     res.append((i, i**2))
# print(res)

# Решение №3 (с лямдой функцией):
# def select(f, col):
#   return [f(x) for x in col]
# def where(f, col):
#   return [x for x in col if f(x)] 
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)



#Функция map
#Пример
# list_1 = [x for x in range(1, 20)]
# print(list_1)
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# Задача: С клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?
# Решение:
# data = '15 156 96 3 5 8 52 5'
# data = list(map(int, data.split()))
# print(data)



#Функция filter
#Пример №1:
# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

#Пример №2:
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)



# # Пример 1:
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

# Конструкция with:
# with open('file.txt', 'w') as data:
#   data.write('line 1\n')
#   data.write('line 2\n')
# print(56)

#Режим чтения
# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#   print(line)
# data.close()