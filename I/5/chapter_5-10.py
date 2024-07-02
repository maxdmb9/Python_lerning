#Проверка имен пользователей на уникальность.
current_users = ['Yana','vika','maria','lena','katya','nina','galya','lida']

new_users = ['vera','yana','olya','Maria','kristina','dasha','mitra','leya']

copy_current_users = [name.lower() for name in current_users]
copy_new_users = [name.lower() for name in new_users]

for name in copy_new_users:
    if name not in copy_current_users:
        print("You can use this name " + name + ".")
    else:
        print("This name " + name + " is busy")    