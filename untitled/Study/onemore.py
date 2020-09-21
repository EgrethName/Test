lst = [1, 2, 3, 4, 67, 7, 4]
lst1 = [1, 2, 3, 4, 5, 6, 11]


def found(input_lst):
    for i in input_lst:
        if i % 5 == 0:
            return True
    return False


def found2(input_lst):
    div5_found = False
    for i in input_lst:
        if i % 5 == 0:
            div5_found = True

    return div5_found


print(found(lst))
print(found(lst1))
