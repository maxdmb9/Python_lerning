#Проверка имен пользователей на уникальность.
current_users = ['Yana','vika','Maria','lena','katya','nina','galya','lida']

new_users = ['vera','yana','olya','maria','kristina','dasha','mitra','leya']


for current_user in current_users:
    if current_user.lower() not in new_users:
        print("You can use this name " + current_user + ".")
    else:
        print("This name " + current_user + " is busy")    