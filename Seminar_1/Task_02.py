import math

n = int(input('Введите трехзначное чиcло: '))
res = math.ceil(((n - n % 100)/100) + ((n%100 - n % 10)/10) + n % 10)
print(res)