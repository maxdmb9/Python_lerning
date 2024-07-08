# Три реки 
rivers = {'angara': 'bratsk', 'ob': 'barnaul', 'goryevka': 'aleysk'}
for city, river in rivers.items():
    print("The " + city + " runs through " + river)
    
# Вывод только реки
for river in rivers.keys():
    print(river.title())  

# Вывод только страны
for city in rivers.values():
    print(city.title())