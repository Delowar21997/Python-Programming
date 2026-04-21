def sum_list(numbers):
    total = 0
    for num in numbers:
        try:
            int(num)  # Attempt to convert to integer
        except:
            print(f"\033[91mWarning: '{num}' is not a valid number and will be skipped.\033[0m")
        else:
            total += int(num)
    return total
# Example usage
my_list = [1, 2, 'three', 4, 'five']
print(f"\033[96mThe total is: {sum_list(my_list)}\033[0m")