dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#Будет ошибка вывода, нельзя изменять кордеж
#print[0] = 250 Кортеж закомменчен из за будет выходить ошибка
for dimension in dimensions:
    print(dimension)
#Замена кортежа
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)