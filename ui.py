# !/user/bin/env python3

""" 
        Notes
added remove function for man add and pick list
separated files for better readability
cleaned up code pep8 updating

for add item manual
    display list up top above input
    clear screen each time, update list

"""

# user interface / the executable

__author__ = "Kamaren McCord"
import sys
sys.path.insert(0, './source/')
from source import logicpy
import time

void2 = 0


def cheat_coder(a_int):
    if a_int == 0:
        return 1
    elif a_int == 1:
        return 0


void2 = logicpy.intro()

cheat_codes = ["made"]
list_ops = ["[1] dinner randomized", "[2] dinner selection", "[3] manually add items to shop list",
            "[4] usually forgotten items QnA", "[end] to exit"]
escape = ["end", "exit", "quit", "stop"]

while True:

    # give the user options
    print("input a number to select option: ")
    for x in list_ops:
        print(" ", x)

    void = input("\n> ")

    # check what the user decided
    if void.lower() == "cheats":
        for x in cheat_codes:
            print(x)
        continue

    if void.lower() in cheat_codes:
        void2 = cheat_coder(void2)

    if void.lower() in escape:
        logicpy.clear_screen()
        print("\n\n\t\tThank you for using the grocery system")
        print("\t\tGoodbye")
        time.sleep(2)
        logicpy.clear_screen()
        exit()

    if void == "1" and void2 == 1:
        print("\nThis list was already created!")
    elif void == "1" and void2 != 1:  # dinner randomized
        void2 = logicpy.randomizer()
    elif void == "2" and void2 == 1:
        print("\nThis list has already been created!")
    elif void == "2" and void2 == 0:  # dinner selection
        void2 = logicpy.dinner_select()
    elif void == "3" and void2 == 0:  # notify user that a list has not yet been made
        print("Try making a list first and then try this again!")
    elif void == "3" and void2 == 1:  # add items to shopping list manually
        logicpy.manual_adder()
    elif void == "4" and void2 == 0:
        print("the list has not yet been created!")
    elif void == "4" and void2 == 1:  # asks for common items that may be forgotten otherwise
        logicpy.item_check()
    else:
        logicpy.clear_screen()
        print("\nThe input was not recognized, please try again.\n\n")
