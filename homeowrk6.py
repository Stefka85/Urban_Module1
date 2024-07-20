# Работа со словарями
my_dict = {"Stepa": 1985, "Natali": 1988, "Mir": 2013, "Svyat": 2017}
print(my_dict)
print(my_dict.get("Natali"))  # одно значение по существующему ключу
print(my_dict.get("Vasya"))  # одно значение по отсутствующему из словаря
my_dict.update({"Vasya": 1981, "Masha": 1981})  # Добавление двух произвольных пар того же формата в словарь
print(my_dict)
a = my_dict.pop("Mir")  # удаление одной из пар в словаре по существующему ключу из словаря
print(my_dict)
print(a)  # вывдение значения из этой удаленной пары на экран.

# Работа с множествами

my_set = {111, 222, 333, 444, "Moscow", "Russia", "Federal", 333, 444, 111, 222, "Federal", "Moscow", "Russia"}  # создание переменной и множеств,с разными типами данных с повторяющимися значениями
print(my_set)
my_set.add(555)  # добавления 2-х множеств
my_set.add(777)
my_set.remove(333)
print(my_set)
