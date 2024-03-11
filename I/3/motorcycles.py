motorcycles = ['honda', 'yamaha', 'ducati']
print(motorcycles)

motorcycles[0] = 'suzuki'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

moto = []

moto.append('honda')
moto.append('yamaha')
moto.append('suzuki')

print(moto)

moto_2 = ['izh','ural','oppozit']
moto_2.insert(1,'yava')
print(moto_2)

motorcycles = ['honda','yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['yava','izh','ural']

last_owned =  motorcycles.pop()
print("The last motorcycle i owned was a " + last_owned.title() + ".")

motorcycles = ['dnepr', 'oppozit','harley_davidson']

first_owned = motorcycles.pop(1)
print("The first motocycle i owned was a " + first_owned.title() + ".")

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove("ducati")
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")