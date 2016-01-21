#1
def linear_search(L, value):
    """ (list, object) -> int
    Returns the index of the last occurrence of value in lst, or return
    -1 if value is not in lst.
    >>> linear_search([2, 5, 1, -3], 5)
    1
    """ 

    i = len(L) - 1
    while i != -1 and L[i] != value:
        i = i - 1
    if i == -1:
        return -1
    else:
        return i
#4a.
def selection(L):
    """ (list) -> list
    Returns the inputted list sorted from smallest integer to largest.
    >>> selection([6, 5, 4, 3, 7, 1, 2])
    [1, 2, 3, 4, 5, 6, 7]
    """

    for i in L:
        line = sorted(L)
    return line


#4b.


#def insertion(L):
    
#5b
def order_list(L):
    end = len(L) - 1
    while end != 0:
        end = end - 1
#5c.
def bubble_sort(L):
    """ (list) -> NotQuiteSure
    Reorders the items in L from smallest to largest.
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> bubble_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """ 

    
    end = len(L) - 1
    while end > 0:
        for i in range(0, end):
            if L[i] > L[i + 1]:
                sorted_list = L[i + 1]
                L[i + 1] = L[i]
                L[i] = sorted_list
        end = end - 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
