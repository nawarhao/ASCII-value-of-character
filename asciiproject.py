# Ask the user to enter a character
char = input("Enter a character: ")

# Only continue if the character is in a known string of characters
if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    ascii_value = ord(char)

    # Identity operator - to show how it works
    check = ascii_value is ascii_value  
    # Bitwise operator - just for learning (not needed but used for practice)
    even_check = ascii_value & 1  

    print("The ASCII code of", char, "is", ascii_value)
    print("Identity check passed:", check)
    print("The ASCII value is", "even" if even_check == 0 else "odd")

else:
    print("Please enter a valid English alphabet (A-Z or a-z).")