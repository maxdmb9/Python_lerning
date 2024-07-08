# Словарь с однотипными объектами
favorite_languages = {
    'jen': 'python',
    'sarah': 'c++',
    'edward': 'ruby',
    'phil': 'python',
}
print("Sarah`s favorite language is " + 
      favorite_languages['sarah'].title() +
      ".")
# Вывод ключ --> значение с использованием цикла for 
for name, language in favorite_languages.items():
    print("Name: " + name.title() + "`s favorite language is " 
          + language.title() + ".")
    
# Вывод только ключа с использованием цикла for
for name in favorite_languages.keys():
    print(name.title())

# Обращение к выделенному значению в словаре
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + 
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

# Используем keys
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")        

# Упорядоченнный перебор ключей словаря
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

 # Перебор всех значений в словаре
print("The following languages have been mentined:")
for language in favorite_languages.values():
    print(language.title())

# Список без повторений воспользуемся множеством set
print("The following languages have been mentined:")
for language in set(favorite_languages.values()):
    print(language.title())