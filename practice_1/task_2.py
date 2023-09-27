"""
Есть список значений list_v, выведите список без дубликатов значения
"""

list_v = [2, 2, 3, 4, 5, 0, 0]
list_v = set(list_v)
list_v = list(list_v)
print(list_v)
