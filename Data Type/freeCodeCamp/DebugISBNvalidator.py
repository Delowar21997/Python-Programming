def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    main_digits = isbn[:length-1]
    given_check_digit = isbn[length-1]


    try:
        #non-numeric chars in ISBN.
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print('Invalid ISBN code. Please enter only digits.')
        return



    # Calculate expected check digit
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    # Compare
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    digits_sum = 0

    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11

    if result == 11:
        return '0'
    elif result == 10:
        return 'X'
    else:
        return str(result)


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0

    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3

    result = 10 - digits_sum % 10

    if result == 10:
        return '0'
    else:
        return str(result)


def main():
    user_input = input('Enter ISBN and length: ')


    try:
#missing comma or non-integer length.
        values = user_input.split(',')
        isbn = values[0].strip()
        length = int(values[1])
    except: #IndexError for missing comma, ValueError for non-integer length.
        print('Invalid input format. Please enter in the format: ISBN, length')
        return
    try:
        #non-numeric chars in length. 
        length = int(length)
    except ValueError:
        print('Invalid length. Please enter a numeric value for length.')
        return
    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')


main()