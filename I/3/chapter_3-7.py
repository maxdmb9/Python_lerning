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
print("\nGuest list expansion")
guest_list.insert(0, "Robert de`niro")
guest_list.insert(1, 'Cory case')
guest_list.append("Tom besenger")
#print(guest_list)
print("Welcome " + guest_list [0].title() + " you invite for my party")
print("Welcome " + guest_list[1].title() + " you invite for my party")
print("Welcome " + guest_list [2].title() + " you invite for my party")
print("Welcome " + guest_list [3].title() + " you invite for my party")
print("Welcome " + guest_list[4].title() + " you invite for my party")
print("Welcome " + guest_list [5].title() + " you invite for my party")
print("\nSorry invite only 2 guests")

cancel_invitation = guest_list.pop()
print(cancel_invitation.title() + " we regret canceling the invitation")
cancel_invitation = guest_list.pop(1)
print(cancel_invitation.title() + " we regret canceling the invitation")
cancel_invitation = guest_list.pop(2)
print(cancel_invitation.title() + " we regret canceling the invitation")
cancel_invitation = guest_list.pop()
print(cancel_invitation.title() + " we regret canceling the invitation")
#Приглашение в силе
print(guest_list[0].title() + " your invitation is valid")
del guest_list[0]
print(guest_list[0].title() + " your invitation is valid")
del guest_list[0]
print(guest_list)