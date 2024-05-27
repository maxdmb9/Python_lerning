#Используем только if

# requested_toppings = ['mushrooms', 'extra cheese']
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'peppironi' in requested_toppings:
#     print("Adding peppironi.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")

# print("\nFinished making your pizza!")

#Используем if elif else
# reguest_toppings = ['muchrooms', 'extra cheese']
# if 'mushrooms' in reguest_toppings:
#     print("Adding mushrooms.")
# elif 'peppironi' in reguest_toppings:
#     print("Adding peppironi.")
# elif 'extra cheese' in reguest_toppings:
#     print("Adding extra cheese.")

# print("\nFinished making your pizza!")

#используем цикл for
# requested_toppings = ['muchrooms', 'extra cheese', 'green peppers']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print("Adding " + requested_topping + ".")

# print("\nFinished making your pizza!")

# requested_toppings = []

# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print("Adding " + requested_topping + ".")
#         print("\nFinished making your pizza!")
#     else:
#         print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms','olives','green peppers' ,
                      'pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don`t have " + requested_topping + ".")

print("\nFinished making your pizza!")