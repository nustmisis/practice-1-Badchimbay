"""
Есть размеры ширина (a) и длина комнаты(b) и высота стен (c)
Вывести объём комнаты в м3 c плавающей точкой
"""


def volume(a, b, c):
    return float(a * b * c)


print(f'Полученный объём комнаты: {volume(3, 4, 3):.3f}')
