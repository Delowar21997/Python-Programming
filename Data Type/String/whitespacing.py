#whitespacing is the process of removing any leading or trailing spaces, tabs, or newline characters from a string.
# This is often necessary when processing user input or reading data from files to ensure that the data is clean and formatted correctly.
# Define a string with leading and trailing whitespace
text = "   Hello, World!   "
# Print the original string with whitespace
print(f"Original string: '{text}'")
# Output the original string with whitespace
print(text)
# Remove leading and trailing whitespace using the strip() method
cleaned_text = text.strip()
# Print the cleaned string without whitespace
print(f"Cleaned string: '{cleaned_text}'")
# You can also use lstrip() to remove leading whitespace and rstrip() to remove trailing whitespace
leading_text = text.lstrip()
trailing_text = text.rstrip()
print(f"Leading whitespace removed: '{leading_text}'")
print(f"Trailing whitespace removed: '{trailing_text}'")
# Output:
# Original string: '   Hello, World!   '
# Cleaned string: 'Hello, World!'
# Leading whitespace removed: 'Hello, World!   '
# Trailing whitespace removed: '   Hello, World!'
