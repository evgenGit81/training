# -*- coding: utf-8 -*-
immutable_var = ("tank", 2, 5, 6, 7) # Кортеж является неизменяемым объектом,
                                    # Однак, если содержит в себе список, то список изменяться может, а сам кортеж - нет
print("Кортеж: ", immutable_var)
#immutable_var[0] = "plane" - такая попытка выдаст ошибку " 'tuple' object does not support item assignment "
#print(immutable_var)

print("------")
immutable_var_2 = ("tank", 2, 5, 6, 7, [4, 6])
print("Кортеж 2:", immutable_var_2)

print("------")
immutable_var_2[5][1] = 234
print("Кортеж 2 с измененным внутри списком:", immutable_var_2)

print("------")
mutable_list = ["tank", 2, 5, 6, 7]
print("Исходный список: ", mutable_list)

print("------")
mutable_list[0] = "plane"
mutable_list.append("sgdfr23")
mutable_list.extend("23gold")
mutable_list.extend(["23gold"]) # в extend должны передаваться итерируемые объект в виде строки или списка или кортежа
print("Измененный список: ", mutable_list)