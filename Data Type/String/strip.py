# whitespace removing methods: strip, rstrip, lstrip, removeprefix, removesuffix. which are used to remove unwanted whitespace or specific characters from strings.
# Whitespace removing is defined as the process of eliminating unnecessary spaces, tabs, or newline characters from the beginning and/or end of a string.
# strip, rstrip, and lstrip are methods used to remove whitespace from strings in Python.
# strip() removes whitespace from both the beginning and end of a string.
name = "   md.delowar hossain   "
cleaned_name = name.strip()
print(f"Original name: '{name}'")
print(f"Cleaned name: '{cleaned_name.title()}'")    
# rstrip() removes whitespace from the end of a string.
trailing_name = name.rstrip()
print(f"Trailing whitespace removed: '{trailing_name}'")
# lstrip() removes whitespace from the beginning of a string.
leading_name = name.lstrip()
print(f"Leading whitespace removed: '{leading_name}'")
# removeprefix() method (available in Python 3.9+) removes a specified prefix from the beginning of a string.
url = "https://www.example.com"
cleaned_url = url.removeprefix("https://")
print(f"Original URL: '{url}'")
print(f"URL after removing prefix: '{cleaned_url}'")
# removesuffix() method (available in Python 3.9+) removes a specified suffix from the end of a string.
filename = "document.txt"
cleaned_filename = filename.removesuffix(".txt")
print(f"Original filename: '{filename}'")
print(f"Filename after removing suffix: '{cleaned_filename}'")
# These methods are useful for cleaning up strings and preparing them for further processing or display.