# Опрос
favorite_languages = {
    'jen': 'python',
    'sarah': 'c++',
    'edward': 'ruby',
    'phil': 'python'
}
# Добавил людей в список    
people = ['jon', 'emma', 'sarah', 'jen']
for name in favorite_languages.keys():
    # print("Спасибо что участвовали в опросе " + name.title())

    if name in people:
        print("Спасибо что участвовали в опросе " + name.title())

if 'jon' not in favorite_languages.keys():
        print("Пройдите пожалуйста опрос Jon!")
if 'emma' not in favorite_languages.keys():
        print("Пройдите пожалуйста опрос Emma!")    