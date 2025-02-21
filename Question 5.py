def find_cjeb_patterns(text):
    count = 0  # Counter for matches
    words = text.split()  # Split text into words

    for word in words:  # Iterate through each word
        if word.startswith("C") and word.endswith("jeb"):  # Check pattern
            count += 1  # Increment count if match found

    return count  # Return total matches


# Example usage
text = "Cabcjeb is a word, but Cxyzjeb and Cotherjeb are too. Cwrong does not count."
print(find_cjeb_patterns(text))  # Should return 3
