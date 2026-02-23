#set() is a collection in which each item is unique.

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print(f"My dictionary: \033[1;97m{favourite_languages}\033[0m\n")
for language in set(favourite_languages.values()):
    print(f"The value of the dictionary: \033[1;92m{language.capitalize()}\033[0m")