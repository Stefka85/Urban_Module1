# переменные разных типов данных
immutable_var = tuple = 0, 9, "Восемь", 7, "six", 5, "four", 3, "Ty", 1
print(immutable_var)

# Изменение значений переменных
# immutable_var = tuple [2] = 8 # изменение кортежа не возможно, ввиду отсутствия поддержки изменений

# Создание изменяемых структур данных
mutable_list = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(mutable_list)
mutable_list.extend(["zero"])
print(mutable_list)