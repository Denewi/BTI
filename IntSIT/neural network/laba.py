"""Нейросеть, которая распознает введенные символы."""
from random import uniform
import numpy as np

# Константы
N_LAYER = 3  # Число слоев
N_MAX_NEURON = 30  # Максимальное число нейронов в слое (нулевой слой)
N_MIN_NEURON = 4  # Минимальное число нейронов в слое (выходной слой)
N_TEMPLATE = 10  # Число шаблонов
N_SPEED = 1  # Коэффициент скорости обучения
E_THRESHOLD = 0.01  # Пороговое значение ошибки обучения
N_ITERATION = 10000  # Максимальное количество итераций в цикле обучения

struc = (N_MAX_NEURON, 30, 25, N_MIN_NEURON)  # Структура сети

# Вещественные занчения
net = float()  # Величина NET для нейронов
eror = float()  # Ошибка обратного распространения
outs = [[0] * N_MAX_NEURON] * (N_LAYER + 1)  # Массив выходов нейронов
# Массив весов
weight = [[[uniform(-1, 1)] * N_MAX_NEURON] * N_MAX_NEURON] * (N_LAYER + 1)
pattern = [[0] * N_MAX_NEURON] * N_TEMPLATE  # Массив входных шаблонов
target = [[0] * N_MIN_NEURON] * N_TEMPLATE  # Массив целевых значений
d_value = [[0] * N_MAX_NEURON] * (N_LAYER + 1)


def main():
    """Главная функция."""
    key = None
    while key != '5':
        key = show_menu()
        if key == '1':
            load_patterns()
        elif key == '2':
            calc_pattern()
        elif key == '3':
            educate()
        elif key == '4':
            set_struc()
        elif key != '5':
            print('Wround item!')


def show_menu():
    """Вывод в консоль меню и запрос ключа."""
    print('\nMenu:')
    print('1: Load patterns')
    print('2: Calc output')
    print('3: Educate')
    print('4: Set structure')
    print('5: Exit')
    key = input('Select menu item: ')

    return key


def load_patterns():
    """Загрузка шаблонов из файла."""
    print('Запустилась load_patterns')


def calc_pattern():
    """Расчет выхода нейросети."""
    print('Запустилась calc_pattern')


def educate():
    """Обучение нейросети."""
    count = 0
    m = 0
    sum = 0
    d_sum = 1

    while d_sum > E_THRESHOLD and count < N_ITERATION:
        for i in range(N_MAX_NEURON):
            outs[0][i] = pattern[m][i]
        neuro_calc()
        sum += pow(calc_err(m), 2)
        go_back()

        if m == N_TEMPLATE - 1:
            d_sum = np.sqrt(sum/N_TEMPLATE)
            m = 0
            sum = 0
        else:
            m += 1

        count += 1


def set_struc():
    """Изменение структуры ИНС."""
    print('Запустилась set_struc')


def neuro_calc():
    """Проход вперед."""
    for k in range(1, N_LAYER + 1):
        for i in range(struc[k]):
            net = 0
            for j in range(struc[k-1]):
                net += outs[k-1][j] * weight[k][j][i]
            outs[k][i] = 1/(1 + np.exp(-net))


def calc_err(m):
    """Расчет ошибки для шаблона m."""
    sum = 0
    for i in range(N_MIN_NEURON + 1):
        sum += pow(target[m][i] - outs[N_LAYER, i], 2)

    return np.sqrt(sum/N_MIN_NEURON)


def go_back():
    """Проход назад."""
    pass


if __name__ == '__main__':
    main()
