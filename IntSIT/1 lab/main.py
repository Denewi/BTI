"""Главный файл."""
from math import ceil


def HelloW():
    """Функция вывода."""
    print('Hello, World!')
    print(2+3)


HelloW()
speed = 108
time = 12
distance = speed*time
print(distance)
print('5+2', 5+2)
print('5-2', 5-2)
print('5*2', 5*2)
print('5/2', 5/2)
print('5%2', 5 % 2)
print('5**2', 5**2)
print('5//2', 5//2)
good = 'Hasta la vista'
print(good + ' zzzz')
t = float(input())
print(int(t))
print(ceil(t))
age = 20
print('age: {0}'.format(age))
print('{0:.20}'.format(t))
