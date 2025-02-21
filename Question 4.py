# Here is a function that determines if a number is palindrome or not:
def palindrome(word):
    word = str(word)  # Convert input to string
    if word == word[::-1]:  # Check if it is a palindrome
        return True
    else:
        return False

num = int(input("Enter a number: "))
if palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is NOT a palindrome.")