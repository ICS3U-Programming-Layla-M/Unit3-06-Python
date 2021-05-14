#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: May 14, 2021
# This program asks the user to input a number between 0 and 9,
# generates a random number and displays a message depending
# on if the guess is the same as the random number or not
# it also display an error message if the input is not an integer

import random


def main():
    # define variable
    correct_guess = random.randint(0, 9)

    try:
        # get the user guess
        user_guess_as_string = input("Guess what number\
 I am thinking of between 0 and 9: ")
        user_guess_as_int = int(user_guess_as_string)

    except ValueError:
        # error message
        print("{} is not a valid number.". format(user_guess_as_string))

    else:
        # check if guess is correct and display message
        # depending on if it's right or wrong
        if (user_guess_as_int == correct_guess):
            print("You guessed correctly!")
        else:
            print("You guessed wrong. The correct answer was: {}\
            ". format(correct_guess))
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
