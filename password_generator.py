# Python Projects for beginners
# https://www.codementor.io/ilyaas97/6-python-projects-for-beginners-yn3va03fs

import random
import string
import sys

letters = string.ascii_letters
numbers = ''.join(map(str, range(0, 10)))
special_characters = '.,/?!@£$%^&*()\\;:{}[]-_=+~`#'

print(""" \\ \\        / / | |                          | |
  \\ \\  /\\  / /__| | ___ ___  _ __ ___   ___  | |
   \\ \\/  \\/ / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | |
    \\  /\\  /  __/ | (_| (_) | | | | | |  __/ |_|
     \\/  \\/ \\___|_|\\___\\___/|_| |_| |_|\\___| (_)
                                                
                                                """)
print("Enter how many letters, numbers and special characters you want and a random password will be generated for you!")


def get_length(input_text):
    try:
        len = int(input("\nnumber of %s: >>" % input_text))
        return len
    except ValueError:
        print("please choose a full number")
        return get_length(input_text)


number_of_letters = get_length("letters")
number_of_numbers = get_length("numbers")
number_of_special_characters = get_length("special characters")

if (number_of_letters + number_of_numbers + number_of_special_characters) < 6:
    sys.exit("Password should be greater than 6 characters, sorry!")

pass_list = []
dictionary = {letters: number_of_letters, numbers: number_of_numbers,
              special_characters: number_of_special_characters}

for gen, num in dictionary.items():
    for i in range(0, num):
        char = random.choice(gen)
        pass_list.append(char)

random.shuffle(pass_list)
password = ''.join(pass_list)

print(password)
