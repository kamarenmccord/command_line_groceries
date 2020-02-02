

""" 
    list_sorter.py takes a list and counts the doubles and returns a list with a number
    after removing the doubles within the list given
    
    call module with list_sort.lst_builder(list)
    will return [[],[],[]] type list
"""

def counter(lst, x):
    count = lst.count(x)
    return count


def lst_builder(lst):
    # remove doubles
    a = []
    for x in lst:
        if x not in a:
            a.append(counter(lst, x))
            a.append(x)
    # put count inside the new matrix
    my_lst = []
    for count, x in enumerate(a,1):
        if (count % 2) != 0:
            nums = x
        if (count % 2) == 0:
            for num, matrix in enumerate(x, 0):
                if num == 0:
                    food = matrix
                if num == 1:
                    isle = matrix
                if num == 2:
                    price = matrix
            my_lst.append([nums, food, isle, price])
    return my_lst

