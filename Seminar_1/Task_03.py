# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32
import math

school_class_1 = int(input('Введите количество учеников в 1 классе: '))
school_class_2 = int(input('Введите количество учеников в 1 классе: '))
school_class_3 = int(input('Введите количество учеников в 1 классе: '))

print(math.ceil(school_class_1 / 2) + math.ceil(school_class_2 / 2) + math.ceil(school_class_3 / 2)) # Решение 1
print()
print ((school_class_1 // 2 + school_class_1 % 2) + (school_class_2 // 2 + school_class_2 % 2) + (school_class_3 // 2 + school_class_3 % 2)) # Решение 2
print()
print((school_class_1+1)//2 + school_class_2//2 + (school_class_2 % 2 != 0) + abs(-school_class_3//2)) # Решение 3