#Checking multiple conditions with "and" and "or"
# In Python, you can check multiple conditions using 
# the logical operators "and" and "or" to combine boolean expressions.
# The "and" operator returns True if both conditions are true, 
# and False otherwise.
# The "or" operator returns True if at least one of the conditions is true,
# and False if both conditions are false.
# Here are some examples of using "and" and "or" to check multiple conditions:  
# Using "and" to check if a number is between 10 and 20
num = 15
if num > 10 and num < 20:
    print(f"{num} is between 10 and 20.")
# Using "or" to check if a number is outside the range of 10 to 20
num = 25
if num < 10 or num > 20:
    print(f"{num} is outside the range of 10 to 20.")
# Using "and" to check if a string is non-empty and contains the word "Python"
text = "I love Python programming!"
if text and "Python" in text:
    print("The text is non-empty and contains the word 'Python'.")
# Using "or" to check if a list is empty or contains the number 5
my_list = [1, 2, 3, 4, 5]
if not my_list or 5 in my_list:
    print("The list is either empty or contains the number 5.") 


#Maltiple mathematical comparisons
# In Python, you can also check multiple mathematical comparisons in a single expression.   
# For example, to check if a number is between 10 and 20, you can use the following syntax:
num = 15
if 10 < num < 20:
    print(f"{num} is between 10 and 20.")
# You can also check if a number is outside the range of 10 to 20 using:
num = 25
if num < 10 or num > 20:
    print(f"{num} is outside the range of 10 to 20.")
# You can combine multiple comparisons as well. For example, to check if a number is between 10 and 20 or is equal to 25:
num = 25
if (10 < num < 20) or num == 25:
    print(f"{num} is either between 10 and 20 or is equal to 25.")
    