from string import ascii_lowercase
import glob
import os

alphabet = ascii_lowercase


def generate_charFiles():
    for char in alphabet:
        try:
            os.mkdir("C:/Users/Magus/Desktop/KodeHode/projects/PythonReview/letters")
        except:
            with open(f"letters/{char}.txt", "w") as file:
                file.write(char + "\n")


# generate_charFiles()

def letter_extractor():
    letters = []
    for char in alphabet:
        with open(f"letters/{char}.txt", "r") as file:
            content = file.read().strip("\n")
            letters.append(content)
    print(letters)


def letter_extractor_glob():
    letters = []
    # use glob til add files from path and filter name and type
    file_list = glob.glob("letters/*.txt")
    for filename in file_list:
        with open(filename, "r") as file:
            letters.append(file.read().strip("\n"))
    print(letters)


def conditioned_letter_extractor():
    check = "python"
    letters = []

    file_list = glob.glob("letters/*.txt")
    for filename in file_list:
        with open(filename, "r") as file:
            content = file.read().strip("\n")
        if content in check:
            letters.append(content)

    print(letters)


conditioned_letter_extractor()
