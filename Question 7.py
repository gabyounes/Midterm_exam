import random

# Create an empty list to store random numbers
random_numbers = []

# Generate 10 random numbers between 1 and 100 and store them in the list
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Iterate through the list and modify elements based on conditions
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        # Replace numbers greater than 50 with a random number between 20 and 30
        random_numbers[i] = random.randint(20, 30)
    elif random_numbers[i] < 50:
        # Replace numbers lower than 50 with "XX"
        random_numbers[i] = "XX"

# Print the modified list to see the final result
print(random_numbers)
