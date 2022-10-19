#!/usr/bin/env python3

# Created by: Kaitlyn Ip
# Created on: Oct 2022
# This program lets users guess the number

import random


def main():
    # this function defines the two possibilities

    # input
    user_guess = int(input("Pick a number between 1-100: "))
    random_variable = random.randint(1, 100)  # a number between 1 and 100

    # process
    if user_guess == random_variable:
        print("You guessed the correct number!")

    else:
        print(
            "You guessed the wrong number! The number was " + str(random_variable) + "."
        )

    print("\nDone.")


if __name__ == "__main__":
    main()
