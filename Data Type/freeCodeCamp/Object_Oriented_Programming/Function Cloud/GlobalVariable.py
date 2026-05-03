num=10
def global_variable_example():
    global num  # Declare 'num' as a global variable
    num += 5  # Modify the global variable 'num'
    print(f"Inside the function, num = {num}")

global_variable_example()  # Call the function to see the effect on the global variable
print(f"Outside the function, num = {num}")  # Print the global variable to see the change made by the function