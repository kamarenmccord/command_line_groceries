# brain of system
import os
import random
import datetime
import math
import time
import shelve
import sys
sys.path.insert(0, './source/')
from source.list_sort import lst_builder
from source.meals import dinner_meal_list, other_items  # subject to change

version_vari = "1.1.5"
debugger = 1


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def set_up():
    if not os.path.exists('./save_data/recipies'):
        os.makedirs('./save_data')
        f = shelve.open('./save_data/recipies')
        f.close()

    if os.path.exists('./container'):
        os.chdir('./container')
        if debugger == 1:
            print("Path found!")
            print('files stored in: ', os.getcwd())  # remind user where files are
            print('\n\n\n')
    else:
        print("container was not found")
        print("Path was created... ")
        os.makedirs('./container')
        os.chdir('./container')
        print("Files will be saved at: {}\n".format(os.getcwd()))  # show user where files are
        print('\n\n\n')


def list_cleaner(clean_list, shop_list):  # shop list writer
    numsper = 1  # master count of all items in list
    estimate = 0
    clean_list = lst_builder(clean_list)
    for nuts in clean_list:
        for numb, x in enumerate(nuts,0):
            if numb == 0:
                count = x
                numsper += count
            if numb == 1:
                food = x
            if numb == 2:
                isle = x
            if numb == 3:
                price = x * count
                estimate += price
                # will be part the last iteration of matrix
                if count > 1:
                    shop_list.write(str(food) + " x{}\t".format(count) + "\t\t" + str(isle) + "\t\t" + str(price) + "\n")
                else:
                     shop_list.write(str(food) + "\t" + "\t\t" + str(isle) + "\t\t" + str(price) + "\n")
    tax = estimate * 0.08
    shop_list.write("\n\t\t\t\t\tSubtotal: ${0:.2f}".format(float(estimate)))
    shop_list.write("\n\t\t\t\t\tTax: ${0:.2f}".format(float(tax)))
    shop_list.write("\n\n\t\t\t\t\tTotal: ${0:.2f}".format(float(estimate + tax)))
    shop_list.write("\n" + " - "*25 + "\n")
    clear_screen()
    print("Total number of items in shop list ", numsper - 1, "\n\n\n")


def list_adder(list_to_write, list_to_adjust):  # writes list to a file
    numsper = 1  # how many items were adding
    for items in list_to_write:
        list_to_adjust.write(str(numsper) + "  " + str(items) + "\n")
        numsper += 1
    print("total number of items added to shopping list = ", numsper - 1)


def dinner_listseven(seven_meals, dinner_list):  # writes to file meal plan for week
    numsper = 1
    for meal_of_day in seven_meals:
        dinner_list.write(str(numsper) + ")  " + str(meal_of_day) + "\n")
        numsper += 1


# shuffled list is undefined
# seven_meals is a blank list at this point
def write_files(a_list):
    seven_meals = []
    clean_list = []
    for meals in a_list:
        seven_meals.append(meals[0])
        for ingrediants in meals[1:]:
            try:  # price check
                clean_list.append([ingrediants[0], ingrediants[1], ingrediants[3]])
            except IndexError:
                    clean_list.append([ingrediants[0], ingrediants[1], 0])
    clean_list = list_sorter(clean_list)

    # create files that hold plans
    shop_list = open('shopping_list.txt', 'w')
    shop_list.close()
    shop_list = open('shopping_list.txt', 'a')
    dinner_list = open('dinner_list.txt', 'w')
    dinner_list.close()
    dinner_list = open('dinner_list.txt', 'a')
    # set up the headers
    shop_list.write(('   ' * 20) + 'Shopping List')
    shop_list.write('\n\n')
    dinner_list.write((' ' * 20) + 'Meal plan for the week of ' + str(datetime.date.today()))
    dinner_list.write('\n\n')
    # write the lists out
    list_cleaner(clean_list, shop_list)  # writes shopping list
    if debugger == 1:
        print("dinner and shopping list were created\n")
    print("total number of items on the shopping list: ", len(clean_list))
    dinner_listseven(seven_meals, dinner_list)  # writes dinner list
    shop_list.close()
    dinner_list.close()


def list_sorter(list_to_organise):  # the sorting algorithm
    list_to_organise.sort(key=lambda list_to_organise: list_to_organise[1])  # sort by name meal
    return list_to_organise


def intro():
    print("\n")
    print("Welcome to the Grocery Generator ", version_vari.rjust(20, '~'), "\n")

    set_up()
    # checking if the files exist to determine if access to list should be available
    if os.path.exists('shopping_list.txt'):
        validate = 0
        while True:
            if validate == 1:
                break
            print("old files have been found,")
            print("Would you like to remove the old files?")
            inny = input("[y/n]  ")
            if inny.lower() == "y":
                clear_screen()
                while True:
                    print("\n\n" + "*" * 80 + "\n" + "    " * 2
                          + "***     ARE YOU SURE YOU WANT TO DELETE THE FILES?[Y/N]     ***\n" + "*" * 80)
                    confirm = input("> ")
                    if confirm.lower() == "y":
                        os.remove('shopping_list.txt')
                        os.remove('dinner_list.txt')
                        clear_screen()
                        print("files removed")
                        return 0
                    elif confirm.lower() == "n":
                        clear_screen()
                        return 1
                    else:
                        clear_screen()
                        print("\n\nInput not recognized! try again")
                        time.sleep(2)  # wait 2 seconds and then recycle prompt
                        clear_screen()
            elif inny.lower() == "n":
                return 1
            else:
                clear_screen()
                print("\n\nThat input is not a valid selection\n[Y/N]")
    return 0


def randomizer():
    while True:
        print("how many meals would you like for the week? ")
        print("number must be equal to or less then: ", len(dinner_meal_list))
        meal_totl = input("> ")
        if meal_totl == 'end':
            break
        try:
            meal_totl = int(meal_totl)
        except ValueError:
            clear_screen()
            print("\n\nThat is not a number try again\n")
            continue
        if meal_totl > len(dinner_meal_list):
            clear_screen()
            print("That number is too high, try again!")
        if meal_totl <= len(dinner_meal_list) >= 1:
            break
        if meal_totl < 1:
            print("That number is too low, you must add something")
    try:
        meal_totl = int(meal_totl)
        if int(meal_totl) <= len(dinner_meal_list) >= 1:
            # extract meal lists
            random.shuffle(dinner_meal_list)
            shuffled_list = dinner_meal_list[:int(meal_totl)]
            write_files(shuffled_list)
            return 1
    except ValueError:
        if meal_totl.lower() == 'end':
            clear_screen()
            print("nothing was changed\n")
            return 0


def dinner_select():
    def price_check_single(master_item):
        total_value = 0
        for single_item in master_item[1:]:
            try:
                total_value += single_item[3]
            except IndexError:
                print(single_item[0], " does not have a price")
                pass
        print('\nThe estimate of ' + master_item[0] + ' is: ', total_value)

    def price_check_less(lower_than_price):
        meal_price = 0
        acceptable_meal = []
        for meals in dinner_meal_list:
            for ingredients in meals[1:]:
                try:
                    if ingredients[3]:
                        meal_price += ingredients[3]
                except IndexError:
                    pass
            if meal_price <= lower_than_price:
                acceptable_meal.append(meals[0])
            meal_price = 0
        if meal_price <= lower_than_price:
            print('\n\nthese meals are less than ' + str(lower_than_price) + ": ")
            for num, meals in enumerate(acceptable_meal, 1):
                print(str(num) + ") ", meals)

    clear_screen()
    seven_meals = []
    counter = 1
    dinner_meal_list.sort(key=lambda dinner_meal_list: dinner_meal_list[0].lower())  # sort by name meal
    for index, meal in enumerate(dinner_meal_list):
        print("  [", index + 1, "] ", meal[0])
        counter += 1
    print("Input a digit from the list above to choose a meal, or enter 'end' to stop")
    print("Type remove to remove the last item added")
    print("Type price and a meal number to check price")
    print("Type less and a price to check meals less than a certain price")
    print("Type refresh to refresh list")
    meals_on_list = 0
    while True:
        print("Total meals chosen: ", meals_on_list)
        inny = input("> ")

        # command zone
        if inny.lower() == "remove":
            if counter > 0:
                print_out = seven_meals.pop(-1)
                print(print_out[0], " :removed")
                counter -= 1
                continue

        if inny.lower() == 'refresh':
            clear_screen()
            for index, meal in enumerate(dinner_meal_list):
                print("  [", index + 1, "] ", meal[0])
                counter += 1
            print("Input a digit from the list above to choose a meal, or enter 'end' to stop")
            print("Type remove to remove the last item added")
            print("Type price and a meal number to check price")
            print("Type less and a price to check meals less than a certain price")
            print("Type refresh to refresh list")
            continue

        if inny.split()[0].lower() == 'less':
            try:
                if int(inny.split()[1]):
                    inny_number = int(inny.split()[1])
                    price_check_less(inny_number)
                    continue
            except IndexError:
                print("you have to specify a number to check up to")
                print("Example: less 20 ;this would check for meals less than $20")
                continue

        if inny.split()[0].lower() == 'price':
            try:
                if int(inny.split()[1]):
                    inny_number = int(inny.split()[1])
                    if inny_number <= len(dinner_meal_list) >= 1:
                        inny_number -= 1
                        price_check_single(dinner_meal_list[inny_number])
                        continue
                    else:
                        print("value out of range")
                        continue
            except IndexError:
                print("you have to specify which meal to price check")
                continue
        # end command zone
        # actual adding to list code
        if inny.lower() != "end":
            try:
                inny = int(inny)
            except ValueError:
                print("\nINPUT INVALID, ENTER A NUMBER OR 'END' TO QUIT\n")
                continue
            # append the list
            if inny <= len(dinner_meal_list) >= 1:
                inny -= 1
                print(dinner_meal_list[inny][0], ":has been added to the list!")
                seven_meals.append(dinner_meal_list[inny])
                meals_on_list += 1
                continue
            if inny > len(dinner_meal_list):
                print("\nVALUE TO LARGE TRY AGAIN\n")
            elif inny <= 0:
                print("\nVALUE TO LOW TRY AGAIN\n")
        if inny == "end":
            break

    if seven_meals:
        while True:
            # ask user if user would like to randomize list
            rnd_value = input("\nwould you like to shuffle this list? [y/n]")
            if rnd_value == "y":
                random.shuffle(seven_meals)
                break
            elif rnd_value == "n":
                break
            else:
                clear_screen()
                print("value was not recognised")
        write_files(seven_meals)
        return 1
    else:
        clear_screen()
        print("nothing has been added\n")


def manual_adder():
    # first nested function :D
    # it removes "remove" from char 1 and checks it against
    # the list in char 2. if its found it returns the key item
    def do_item_verify(char_1, char_2):
        char_1 = char_1.split()
        if 'remove' in char_1:
            char_1.remove('remove')
        char_1 = ' '.join(char_1)

        if char_1 in char_2:
            return char_1
        else:
            return 'no'

    def do_remove_help():
        clear_screen()
        help_article = '''  
        This is the help prompt for (remove)
        Type in a name of something that has already been added after remove
        Example:
    
            >remove apples
    
    
        This will cause apples to be removed, however if apples have not been added to the list
        it cannot be removed.
        Example:
    
            current list:
                apples
    
            >remove apple
    
    
        Apples will not be removed from the list because the 'apples' in the list is not plural
        this rule also applies to case sensitive words such as Pancakes
        try to maintain all lower casing if and when possible
    
        Type in all after remove to remove all items from the list,
        WARNING: this cannot be reversed
        Example:
    
            current list:
                apples, bananas, pineapples, kiwi
    
            >remove all
    
            current list:
                (nothing)
    
    
        If you wish to stop adding items to the list at any time type 'end'
    
        PRESS ENTER TO EXIT THIS PROMPT
                        '''
        print(help_article)
        input(" >")
        clear_screen()

    # end help section

    shop_list = open('shopping_list.txt', 'a')
    add_to_list = []
    cancel = ['end', 'stop', 'exit', 'quit', 'escape']
    count = 0
    while True:
        # prompt
        clear_screen()
        if not add_to_list:
            print("There is nothing currently being added.")
        else:
            print("Current list: \n", ", ".join(add_to_list))
        print("\nWhat would you like to add to the shopping list? enter 'END' to stop adding")
        if add_to_list:
            print("Type remove help for assistance")
        inny = str(input(" > "))

        if inny:
            if inny.split()[0].lower() == 'remove' and not add_to_list:
                print('\n\n\tyou must add something before being able to remove something')
                time.sleep(3)
            # error checking
            if add_to_list:
                if inny.split()[0].lower() == "remove":
                    try:
                        if inny.split()[1]:
                            if inny.split()[1].lower() == 'help':
                                do_remove_help()
                                continue
                            if inny.split()[1].lower() == "all":
                                copycat_list = add_to_list.copy()
                                for items in add_to_list:
                                    copycat_list.remove(items)
                                add_to_list = copycat_list
                            if inny.split()[1] in add_to_list:
                                add_to_list.remove(inny.split()[1].lower())
                                continue
                            special_key = do_item_verify(inny, add_to_list)
                            if special_key != 'no':
                                add_to_list.remove(special_key)
                                continue
                            else:
                                print('\n\n\titem not found')
                                time.sleep(3)
                    except IndexError:
                        clear_screen()
                        print("\n\nYou have to specify what to remove, EXAMPLE:\n"
                              "\t\tremove apple\n\n"
                              "if spelling does not match it will not be removed")
                        time.sleep(3)
                        continue

            if inny.lower() not in cancel and inny.split()[0].lower() != "remove":
                add_to_list.append(inny)
                count += 1
                continue

        if inny.lower() in cancel:
            break
    clear_screen()
    print(len(add_to_list), ": items were added to the list \n")
    if add_to_list:  # if the list is not blank
        # write add list to shop list
        shop_list.write("\n\n")
        shop_list.write("Manually added items:\n")
        list_adder(add_to_list, shop_list)
        shop_list.close()


def item_check():
    shop_list = open('shopping_list.txt', 'a')
    clear_screen()
    print("\nRemember two is one and one is none\n")
    forgotten_list = ["tp", "seasonings", "work or school supplies", "beer", "sodas", "monsters", "condoms"]
    add_to_list = []
    for items in forgotten_list:
        print("Do you need: ", items)
        inny = input("[y/n] ")
        if inny.lower() == "y":
            add_to_list.append(items)
        else:
            continue
    clear_screen()
    print("we have added these items to the list: ")
    enumer = 1
    for items in add_to_list:
        print(enumer, ") ", items)
        enumer += 1

    if add_to_list:
        # write add list to shop list
        shop_list.write("\n\n")
        shop_list.write("forgotten items:\n")
        list_adder(add_to_list, shop_list)
        shop_list.close()
        print("shopping list closed")
    else:
        print('nothing was added')
