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

print("Hear")
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)