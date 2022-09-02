from string import ascii_uppercase

plain_text = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"


def cipher_caesar(plaintext, shift):
    """Take str input, and shift, returns encrypted string"""
    alphabet = [x for x in ascii_uppercase]
    numbers = [x for x in range(len(alphabet))]
    letters = {key: val for key, val in zip(numbers, alphabet)}

    cipher_text = ""
    for char in plaintext.upper():
        if char.isalpha():
            shifted_letter = ((ord(char) - 65) + shift) % 26
            cipher_text += letters[shifted_letter]
        else:
            cipher_text += char
    return cipher_text
