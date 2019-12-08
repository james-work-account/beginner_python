# Python Projects for beginners
# https://www.codementor.io/ilyaas97/6-python-projects-for-beginners-yn3va03fs

from random import randint
import sys

rock = "rock"
paper = "paper"
scissors = "scissors"
draw = "draw"
win = "win"
lose = "lose"

available_guesses = [rock, paper, scissors]
rps_dict = {}

"""add guesses to dict for computer_guess"""
for num, guess in enumerate(available_guesses, 0):
    rps_dict[num] = guess

print(""" \\ \\        / / | |                          | |
  \\ \\  /\\  / /__| | ___ ___  _ __ ___   ___  | |
   \\ \\/  \\/ / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ | |
    \\  /\\  /  __/ | (_| (_) | | | | | |  __/ |_|
     \\/  \\/ \\___|_|\\___\\___/|_| |_| |_|\\___| (_)
                                                
                                                """)
print("The computer has guessed either rock, paper or scissors. Try to beat it!\n")


computer_guess = rps_dict[randint(0, 2)]
player_input = input("rock, paper or scissors? >>").lower()

"""player makes an invalid guess"""
if not player_input in available_guesses:
    sys.exit("You didn't make a valid guess!")

outcome = {
    (rock, rock): draw,
    (rock, paper): lose,
    (rock, scissors): win,
    (paper, rock): win,
    (paper, paper): draw,
    (paper, scissors): lose,
    (scissors, rock): lose,
    (scissors, paper): win,
    (scissors, scissors): draw
}


# \033[1m = BOLD, \033[0m = END. See https://stackoverflow.com/a/17303428
sys.exit("You guessed \033[1m%s\033[0m and computer guessed \033[1m%s\033[0m. You \033[1m%s\033[0m!" %
         (player_input, computer_guess, outcome[(player_input, computer_guess)]))
