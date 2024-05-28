#Проверка на отсутствие пользователей
users = []

if users:
    for user in users:
        print("Welcome " + user + ".")
else:
    print("We need to find some users!")