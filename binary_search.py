def binary_search(list=[int], number=int):
    """
        list: list of integers.
        number: the number to be found.
        return: True if in the list, else False.
    """
    number_found = False
    first = 0
    last = len(list) - 1
    if number > list[-1] or number < list[0]:
        return False

    while first <= last and not number_found:
        middle = round((last + first)/2)
        if list[middle] == number:
            return True
        else:
            if number < list[middle]:
                last = middle - 1
            else:
                first = middle + 1

    return False


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8))
