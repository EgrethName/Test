
def recurs(i):
    return i % 5 == 0

def found(list_x):
    a = 0
    for element in list_x:
        result = recurs(element)
        if result:
            a += 1
            break
    if a == 0:
        return False
    else:
        return True



def found_(list_x):
    a = 0
    for element in list_x:
        result = recurs(element)
        break
    if a == 0:
        return False
    else:
        return True

lst = [1, 2, 3, 4, 67, 7, 4]
lst1 = [1, 2, 3, 4, 5, 6, 11]
print(found(lst))
print(found(lst1))
