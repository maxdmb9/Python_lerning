#Проверка присутствия в списке
trees = ['дуб', 'клен','береза','сосна']
if 'клен' in trees:
    print('Это дерево есть в списке')
if 'осина' in trees:
    print('Осина тоже в списке')
else:
    print('Осины нет в списке')    

#Проверка на отсутствие в списке
fruits = ['banana', 'orange', 'apple']
fruit = 'pineapple'
if fruit not in fruits:
    print("Нет в списке " + fruit.title())