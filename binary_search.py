# Python Projects for beginners
# https://www.codementor.io/ilyaas97/6-python-projects-for-beginners-yn3va03fs

import random
import sys


def createlist():
    k = list()
    for _ in range(0, 100):
        num = random.randrange(0, 101)
        k.append(num)
    return k


print(""" \\ \\        / / | |                          | |
  \\ \\  /\\  / /__| | ___ ___  _ __ ___   ___  | |
   \\ \\/  \\/ / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | |
    \\  /\\  /  __/ | (_| (_) | | | | | |  __/ |_|
     \\/  \\/ \\___|_|\\___\\___/|_| |_| |_|\\___| (_)
                                                
                                                """)
print("The computer is going to perform a binary search to find a number in a list of randomly generated numbers. "
      "It will then split this list in two, choosing which list your number is in and repeating the process until there is only one element left.\n")

guess = int(input("Enter a number between 1 and 100: >>"))

if guess < 0:
    sys.exit("Number must be positive or 0")
if guess > 100:
    sys.exit("Number must be below or equal 100")


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


def find_number(l):
    l1, l2 = split_list(l)
    print(l)
    if len(l2) > 0 and len(l1) == 0 and l2[0] == guess:
        return
    if guess in l1:
        find_number(l1)
    elif guess in l2:
        find_number(l2)
    else:
        print("Cannot find number.")


generated_list = list(set(createlist()))
find_number(generated_list)
