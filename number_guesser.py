# Python Projects for beginners
# https://www.codementor.io/ilyaas97/6-python-projects-for-beginners-yn3va03fs

from random import randint

random_number = randint(1, 20)
player_has_guessed_correctly = False
number_of_player_guesses = 0

print(""" \\ \\        / / | |                          | |
  \\ \\  /\\  / /__| | ___ ___  _ __ ___   ___  | |
   \\ \\/  \\/ / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | |
    \\  /\\  /  __/ | (_| (_) | | | | | |  __/ |_|
     \\/  \\/ \\___|_|\\___\\___/|_| |_| |_|\\___| (_)
                                                
                                                """)
print("The computer has generated a random number. Try to guess it!\n")

while not player_has_guessed_correctly:
    current_player_guess_as_str = input("What number will you guess? >>")
    try:
        current_player_guess_as_int = int(current_player_guess_as_str)
    except:
        print("You need to guess a number!")
        current_player_guess_as_int = 0

    if random_number == current_player_guess_as_int:
        print("You win!")
        player_has_guessed_correctly = True
    else:
        number_of_player_guesses += 1
        if number_of_player_guesses == 5:
            print("\n")
            print("You didn't guess correctly in 5 tries 😔\nThe correct number was %d" %
                  random_number)
            break
        if current_player_guess_as_int > random_number:
            print("Too high!")
        elif current_player_guess_as_int != 0 and current_player_guess_as_int < random_number:
            print("Too low!")
        print("\n")
