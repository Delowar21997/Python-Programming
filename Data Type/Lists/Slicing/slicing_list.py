fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
# Slicing the list to get a subset of fruits
# Get the first three fruits
first_three_fruits = fruits[0:3]
print("First three fruits:", first_three_fruits)
#Get the fruits from start to index 4 omitting index 0
fruits_from_start_to_index_4 = fruits[:5]
print("Fruits from start to index 4:", fruits_from_start_to_index_4)
# Get the index 2 to 5 fruits
middle_fruits = fruits[2:6]
print("Fruits from index 2 to 5:", middle_fruits)
# Get the last three fruits
last_three_fruits = fruits[4:] 
print("Last three fruits:", last_three_fruits)
#get the last two fruits
last_two_fruits = fruits[-2:]
print("Last two fruits:", last_two_fruits)
# Get every fruit except the first and last one
fruits_except_first_and_last = fruits[1:-1]
print("Fruits except first and last:", fruits_except_first_and_last)
number = [1, 2, 3, 4, 5, 6]
# Get every second number from the list
every_second_number = number[0::2]
print("Every second number:", every_second_number)
# Get the numbers in reverse order
numbers_in_reverse = number[::-1]
print("Numbers in reverse order:", numbers_in_reverse)
# Get the numbers from index 1 to 5 with a step of 2
numbers_with_step = number[1:6:2]
print("Numbers from index 1 to 5 with a step of 2:", numbers_with_step)
# Get the last three numbers in reverse order
last_three_numbers_reverse = number[-1:-4:-1]
print("Last three numbers in reverse order:", last_three_numbers_reverse)
# Get the first five numbers in reverse order
first_five_numbers_reverse = number[4::-1]
print("First five numbers in reverse order:", first_five_numbers_reverse)
# Get the numbers from index 2 to the end with a step of 3
numbers_from_index_2_with_step = number[2::3]
print("Numbers from index 2 to the end with a step of 3:", numbers_from_index_2_with_step)
# Get the numbers from index 1 to index 4 with a step of 2 in reverse order
numbers_from_index_1_to_4_reverse = number[4:0:-2]
print("Numbers from index 1 to index 4 with a step of 2 in reverse order:", numbers_from_index_1_to_4_reverse)
