def encrypt_text(shift1, shift2):
    # [1] How to read a file in Python using open() and read()
    try:
        with open("raw_text.txt", "r") as file:
            text = file.read()
    except FileNotFoundError:
        print("Error: 'raw_text.txt' not found. Please ensure the file exists.")
        return

    encrypted = ""

    # [4] Loops and conditionals for processing each character
    for ch in text:
        # [5] String manipulation: checking lowercase characters
        if 'a' <= ch <= 'z':
            # [6] Character shifting logic using ASCII values (ord and chr)
            pos = ord(ch) - ord('a')
            # [7] Numeric calculations using modulo arithmetic
            pos = (pos + shift1) % 26
            encrypted += chr(pos + ord('a'))

        # [5] String manipulation: checking uppercase characters
        elif 'A' <= ch <= 'Z':
            pos = ord(ch) - ord('A')
            pos = (pos + shift2) % 26
            encrypted += chr(pos + ord('A'))

        else:
            encrypted += ch

    # [2] How to write into a file in Python using write()
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted)
    print("Encryption completed. Check 'encrypted_text.txt'.")

def decrypt_text(shift1, shift2):
    # [1] Reading a file using open() and read()
    try:
        with open("encrypted_text.txt", "r") as file:
            text = file.read()
    except FileNotFoundError:
        print("Error: 'encrypted_text.txt' not found. Run encryption first.")
        return

    decrypted = ""

    # [4] Looping through characters with conditionals
    for ch in text:
        if 'a' <= ch <= 'z':
            pos = ord(ch) - ord('a')
            pos = (pos - shift1) % 26
            decrypted += chr(pos + ord('a'))
        elif 'A' <= ch <= 'Z':
            pos = ord(ch) - ord('A')
            pos = (pos - shift2) % 26
            decrypted += chr(pos + ord('A'))
        else:
            decrypted += ch

    # [2] Writing decrypted output to a file
    with open("decrypted_text.txt", "w") as file:
        file.write(decrypted)
    print("Decryption completed. Check 'decrypted_text.txt'.")

def verify_decryption():
    # [8] Comparing files or strings in Python
    try:
        with open("raw_text.txt", "r") as file1:
            original = file1.read()
        with open("decrypted_text.txt", "r") as file2:
            decrypted = file2.read()
    except FileNotFoundError:
        print("Error: Required files not found. Run encryption and decryption first.")
        return

    if original == decrypted:
        print("Decryption successful. Files match.")
    else:
        print("Decryption failed. Files do not match.")

def main():

    # [3] Taking user input using input()
    try:
        shift1 = int(input("Enter shift1: "))
        shift2 = int(input("Enter shift2: "))
    except ValueError:
        print("Error: Shifts must be integers.")
        return

    encrypt_text(shift1, shift2)
    decrypt_text(shift1, shift2)
    verify_decryption()
# [9] Printing special characters (Unicode support in Python)
if __name__ == "__main__":
    main()
