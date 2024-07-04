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
for name, language in favorite_languages.items():
    print("Name: " + name.title() + "`s favorite language is " 
          + language.title() + ".")