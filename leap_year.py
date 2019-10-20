#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on October 2019
# This program asks user to enter a year above 0
# and tells them if the year is a leap year or not


def main():
    # This function calculates if a year is a leap year or not

    # input
    number = input("Enter year number above or equal to 0: ")
    print("")

    # process
    try:
        integer = int(number)

        if (integer >= 0):
            if (integer % 4 == 0 and integer % 100 != 0):
                print("This is a leap year.")

            elif (integer % 100 == 0 and integer % 400 == 0):
                print("This is a leap year.")

            else:
                print("This is not a leap year.")

        else:
            print("Invalid input.")

    except ValueError:
        print("Invalid input.")


if __name__ == "__main__":
    main()
