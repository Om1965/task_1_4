#Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"
#Цель: Написать программу на языке Python, используя Pycharm, для работы с неизменяемыми и изменяемыми объектами

#2. Задайте переменные разных типов данных:
#Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных
varable_ = 24.5
# Назначим кортежу элементы типа: Строка, Целое, Булево, Переменная
immutable_var = 'Шелк', 45, True, varable_
#Выполните операции вывода кортежа immutable_var на экран
# Выведем весь кортеж на экран
print('Immutable tuple:', immutable_var)
# Выведем третий элемент кортежа
print('Immutable tuple, element 3:', immutable_var[2])

#3. Изменение значений переменных:
#Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа
#immutable_var[1] = 7
# Попытка изменить второй элемент кортежа приводит к ошибке: 'tuple' object does not support item assignment,
# т.к. кортежи не поддерживают изменение значений элементов

#4. Создание изменяемых структур данных:
# Создайте переменную mutable_list и присвойте ей список из нескольких элементов
mutable_list = (['Начало', 25], 'Середина', varable_, False)
print('Mutable list:', mutable_list)
# Измените элементы списка mutable_list
mutable_list[0][1] = 'Элемент списка изменен'
print('Mutable list:', mutable_list)