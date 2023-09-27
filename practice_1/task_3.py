# -*- coding: utf-8 -*-
"""
Напишите программу для расчета индекса массы тела (body mass index –
BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы
используете одну из приведенных ниже формул для определения индекса.
BMI = вес/рост**2
"""


def bmi(x, y):
    return x/(y**2)


weight = float(input('Введите вес: '))
height = float(input('Введите рост: '))

print(f'Индекс массы тела: {bmi(weight, height):.3f}')
