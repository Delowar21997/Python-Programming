car_list = ["Audi", "Honda", "Toyota", "Ford", "BMW"]
choice_car = ["Toyota", "Audi", "Mercedes"]

print(f"The value of car_list is: \033[1;92m{car_list}\033[0m")
print(f"The value of choice_car is: \033[1;92m{choice_car}\033[0m\n")
for car in choice_car:
    if car in car_list:
        print(f"\033[1;92m{car}\033[0m is available.")
    else:
        print(f"\033[1;91mSorry, {car}\033[0m is not available for now.")

print("\n"+"\033[1;92m!"*15+ f" Dear customer, we will try to collect the car as you choose."+"!"*15+"\033[0m\n")
