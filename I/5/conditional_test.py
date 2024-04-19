cat = 'muska'
print(cat == 'muska')
print(cat != 'muska')

cats = ['murka', 'PESTRUCHA', 'SERAYA', 'chernaya']

for one_cat in cats:
    if one_cat == 'SERAYA':
        print(one_cat.lower())
    else: 
        print(one_cat.title())   
