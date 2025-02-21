#Please explain what it means that a list is mutable and a string is not mutable (imutable).
#Give some code that shows the difference. Use your own words

# Creating a list
my_list = ["Sushi", "Burger", "Pizza"]
print("Original List:", my_list)

# Changing an element
my_list[1] = "Shawarma"
print("Modified List:", my_list)

# Creating a string
my_string = "Bonjour"
print("Original String:", my_string)

# Trying to change a character (this will cause an error)
try:
    my_string[0] = "L"
except TypeError as e:
    print("Modified String:", e)