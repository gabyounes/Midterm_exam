def is_valid_url(url):
    """
    Function to check if a given string is a valid URL.
    A valid URL must start with "http://" or "https://" and contain at least one "." after that.
    """

    # Check if URL starts with valid protocol
    if url.startswith("http://") or url.startswith("https://"):
        # Remove the protocol part
        url = url.split("//", 1)[1]

        # Check if there is at least one "." in the remaining part
        if "." in url:
            return True

    return False


# Example usage
print(is_valid_url("http://example.com"))  # Should return True
print(is_valid_url("https://google.com"))  # Should return True
print(is_valid_url("ftp://invalid.com"))  # Should return False
print(is_valid_url("invalid-url"))  # Should return False