favourite_languages = {
    'john': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
friends = ['sarah', 'phil']
for name in favourite_languages.keys():
    print(f"Hi \033[1;92m{name.title()}\033[0m.")
    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t\033[1;92m{name.title()}\033[0m, I see you love \033[1;92m{language}\033[0m!")