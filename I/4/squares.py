#Возведение в степень
squares = [] #1)просто пустой список
for value in range(1,11): #2)в value поместим значения от 1 до 10
    square = value**2 #3)значения в value возведем во 2 степень и сохраним в square
    squares.append(square) #4)присоединение к списку squares
print(squares) #5)вывод

squares = [] #1)просто пустой список
for value in range(1,22): #2)в value поместим значения от 1 до 10
    #square = value**2 #3)значения в value возведем во 2 степень и сохраним в square
    squares.append(value**3) #4)присоединение к списку squares
print(squares) #5)вывод