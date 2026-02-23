#values() method is used to return a view object that displays a list of all the values in the dictionary.
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print(f"My dictionary: \033[1;97m{favourite_languages}\033[0m\n")
for language in favourite_languages.values():
    print(f"The value of the dictionary: \033[1;92m{language.capitalize()}\033[0m")