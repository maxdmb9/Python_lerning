#Новая тема словари

# alien_0 = {'color': 'green', 'points':5}

# print(alien_0['color'])
# print(alien_0['points'])

#Обращение к значниям в словаре
# alien_0 = {'color': 'green', 'points':5}

# new_points = alien_0['points']  
# print("You just earned " + str(new_points) + " points!")

#Добавление новых пар "ключ-значение"
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# Создание пустого словаря
# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['poison'] = 5

# print(alien_0)

# Изменение значений в словаре
# alien_0 = {'color': 'green'}
# print("The alien is " + alien_0['color'] + ".")

# alien_0['color'] = 'yellow'
# print("The alien is now " + alien_0['color'] + ".")

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print("Original x-position: " + str(alien_0['x_position']))
# # Пришелец перемещается вправо
# # Вычисляем величину смещения на основании текущей скорости.

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # Пришелец двигается быстро.
#     x_increment = 3
# # Новая позиция равна сумме старой позиции и приращения.
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print("New x-position: " + str(alien_0['x_position']))

# Удаление пар "ключ-значение"
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)

#________________________________________________
# Вложения
# alien_0 = {'color': 'green', 'points':5}
# alien_1 = {'color': 'yellow', 'points':10}
# alien_2 = {'color': 'red', 'points':15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# Флот пришельцев
# Создание пустого списка для хранения пришельцев.
aliens = []
# Создание 30 зеленых пришельцев.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Вывод первых 5 пришельцев:
for alien in aliens[:7]:
    print(alien)
print("...")

# Вывод колличества созданных пришельцев.
print("Total number of aliens: " + str(len(aliens)))