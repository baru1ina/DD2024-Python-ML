import pandas as pd
import numpy as np

# Из списка
s1 = pd.Series([10, 20, 30])

# Из массива NumPy
s2 = pd.Series(np.array([1, 2, 3]))

# Из скалярного значения
s3 = pd.Series(5, index=['a', 'b', 'c'])

# Из словаря
s4 = pd.Series({'a': 100, 'b': 200, 'c': 300})

print(s1, s2, s3, s4, sep="\n\n")

# Из Series
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['a', 'b', 'c'])
df1 = pd.DataFrame({'col1': s1, 'col2': s2})

# Из списка словарей
df2 = pd.DataFrame([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}])

# Из словаря Series
df3 = pd.DataFrame({'one': s1, 'two': s2})

# Из двумерного массива NumPy
df4 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]), columns=['A', 'B', 'C'])

# Из структурированного массива NumPy
dtype = [('A', 'int32'), ('B', 'float32')]
data = np.array([(1, 2.5), (3, 4.5)], dtype=dtype)
df5 = pd.DataFrame(data)

print(df1, df2, df3, df4, df5, sep="\n\n")

s1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s2 = pd.Series([40, 50], index=['b', 'd'])

# Объединение с заполнением NaN значением 1
s_combined = s1.add(s2, fill_value=1)
print(s_combined)

df = pd.DataFrame(np.arange(9).reshape(3, 3), columns=['A', 'B', 'C'])
print("Исходный DataFrame:\n", df)

# Вычитаем значения первой строки из всех остальных строк (по столбцам)
df_subtracted = df.sub(df.iloc[0], axis=1)
print("Результат вычитания по столбцам:\n", df_subtracted)

df = pd.DataFrame({'A': [1, np.nan, 3, np.nan, 5], 'B': [np.nan, 2, np.nan, 4, 5]})
print("Исходный DataFrame:\n", df)

# Прямое заполнение вперед (forward fill)
df_ffill = df.ffill()
print("После ffill():\n", df_ffill)

# Обратное заполнение назад (backward fill)
df_bfill = df.bfill()
print("После bfill():\n", df_bfill)
