#Список гостей
guest_list = ['Merilin Monro', 'djesika alba', 'Pamela Anderson', ]
print("Welcome " + guest_list [0] + " you invite for my party")
print("Welcome " + guest_list[1].title() + " you invite for my party")
print("Welcome " + guest_list [2] + " you invite for my party")

not_coming = guest_list.pop()
print("Sorry " + not_coming.title() + " won`t come to the party")

guest_list.append("mia halifa")
print("Welcome " + guest_list [0] + " you invite for my party")
print("Welcome " + guest_list[1].title() + " you invite for my party")
print("Welcome " + guest_list[2].title() + " you invite for my party")