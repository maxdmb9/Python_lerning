#вывод среза (slice)
players = ['carles', 'martina', 'michael', 'florence', 'ali' ]
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[3:])
print(players[-3:])
#перебор с использованием цикла
print("here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
