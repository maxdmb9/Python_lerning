#Возведение в степень
squares = [] #просто пустой список
for value in range(1,11): #в value поместим значения от 1 до 10
    square = value**2 #значения в value возведем во 2 степень и сохраним в square
    squares.append(square) #присоединение к списку squares
print(squares) #вывод