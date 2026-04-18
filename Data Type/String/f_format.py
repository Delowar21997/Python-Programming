# Using f-strings to format names and demonstrate string methods
# Define first and last names
# doubl
# Combine them into a full name using an f-string
# Print the full name in various formats
first_name = "md.Delowar"
last_name = "hossain"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
greeting = "Welcome to Python programming!"
print(full_name)
print(full_name.title())
print(full_name.upper())
print(full_name.lower())
print(message)
print(f"Hi, {full_name.title()}.{greeting}")


print(f"{full_name.title()}.{greeting} Have a great day!")