cat = 'muska'
print(cat == 'muska')
print(cat != 'muska')

cats = ['murka', 'PESTRUCHA', 'SERAYA', 'chernaya']

for one_cat in cats:
    if one_cat == 'SERAYA':
        print(one_cat.lower())
    else: 
        print(one_cat.title())

#Сравнение чисел
a =11
b =26
c =33
if a > b:
    print('true')    
else:
    print('false')    

if a<b:
    print('верно')   

answer = 3
if answer != 15:
    print('this true ')

d=b+c

if d >= c:
    print(d)

if c <= a:
    print(c)   

if d>a or c<=d:
    print('yes')    