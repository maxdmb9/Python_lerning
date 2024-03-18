#Список 
town_list = ['красный яр','алейск','шипуново','кашино','нечунаево','сентелек']
print(town_list)
print(town_list[2])
print(town_list[2].title())
print(town_list[-1])
message = "My first city was a " + town_list[2].title() + "."
print(message)
#Изменение списка
town_list_2 = ['красный яр','алейск','шипуново','кашино','нечунаево','сентелек']
print(town_list_2)
town_list_2[1] = 'вяткино'
print(town_list_2)
town_list_2.append('дружба')
print(town_list_2)
town_list_2.insert(3, 'уржум')
print(town_list_2)
del town_list_2[3]
print(town_list_2)
popped_town_list_2 = town_list_2.pop()
print(town_list_2)
print(popped_town_list_2.title())
print(town_list_2)
town_list_2.remove('вяткино')
print(town_list_2)
town_list_2.sort()
print(town_list_2)
town_list_2[1] = 'вяткино'
print(town_list_2)
print(sorted(town_list_2))
print(town_list_2)
town_list_2.reverse()
print(town_list_2)
print(len(town_list_2))