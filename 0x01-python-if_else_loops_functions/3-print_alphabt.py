#!/usr/bin/python3
for code in range(97, 123):  # ASCII codes for lowercase letters
    if code != 101 and code != 113:  # Excluding 'e' (101) and 'q' (113)
        print(chr(code), end='')  # Convert ASCII code to character and print without a new line

