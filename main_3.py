#2023/09/21 00:00|Практическое задание по теме "Переменные".
#Напишите 4 переменных которые буду обозначать следующие данные:
#1. Количество выполненных ДЗ (запишите значение 12)
count_dz = 12
#2. Количество затраченных часов (запишите значение 1.5)
count_hours = 1.5
#3. Название курса (запишите значение 'Python')
name_kurs = 'Python'
#4. Время на одно задание (вычислить используя 1 и 2 переменные)
time_one_dz = count_hours / count_dz
#Выведите на экран(в консоль), используя переменные, следующую строку:
print('Курс:', name_kurs,', всего задач:', count_dz,', затрачено часов:',count_hours, ', среднее время выполнения ', time_one_dz,' часа', sep='')