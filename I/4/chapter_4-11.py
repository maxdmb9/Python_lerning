pizzas = ['овощи', 'сыр', 'морепродукты']
friend_pizzas = pizzas[:]
#for pizza in pizzas:
#    print(pizza)
#    print("Я очень люблю " + pizza +" пиццу")
#print("I really love pizza!")

friend_pizzas.append('мясная')
pizzas.append('карбонара')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())
print("My friend`s favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())