#Whitespace removing is defi
# Prefixes removed is used to remove specific characters from the beginning of a string.
# It is similar to lstrip(), but instead of removing whitespace, it removes the characters specified in the argument.
# Define a string with specific characters at the beginning
text = "http://www.google.com"
# Print the original string
print(f"Original string: '{text}'")
# Remove the "http://" prefix using lstrip()
cleaned_text = text.lstrip("http://")
# Print the cleaned string without the prefix
print(f"Cleaned string: '{cleaned_text}'")
# Remove the "http://" prefix using removeprefix() method (available in Python 3.9+)
remove_prefix = text.removeprefix("http://")
print(f"String after removing prefix using removeprefix(): '{remove_prefix}'")  
