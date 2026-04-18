language = {'apon': 'python', 'sara': 'c', 'ali': 'ruby', 'zara': 'python'}
user =['apon','era']
for name in language.keys():
    print(f"Hi \033[1;92m{name.title()}\033[0m.")
if "era" not in language.keys():
    print(f"\t\033[1;91mEra\033[0m, please enroll in our poll!")
