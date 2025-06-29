import numpy as np


# 1. Что надо изменить в последнем примере, чтобы он заработал без ошибок 
# (транслирование)?

# a = np.ones((3, 2))
# b = np.arange(3)

a = np.ones((3, 2))
print(f'a = {a}')
b = np.arange(3)
print(f'b = {b}')

b1 = b[:, np.newaxis]
print(f'b1 = {b1}')
print(f'a + b1 = {a + b1}')

b2 = np.reshape(b, (3, 1))
print(f'b2 = {b2}')
print(f'a + b2 = {a + b2}')

#      a: (3, 2) -> (3, 2)
# b1, b2: (3, 1) -> (3, 2)

# 2. Пример для y. Вычислить количество элементов (по обеим размерностям),
# значения которых больше 3 и меньше 9
y = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])
print(f'y = {y}')

inds = (y > 3) & (y < 9)
print(inds)

print(f'axis=0:\n {(np.sum(inds , axis=0))}')
print(f'axis=1:\n {(np.sum(inds , axis=1))}')
print('Элементы:')
print(y[inds])
