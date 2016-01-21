#1
def complement(sequence):
    """(str) -> str
    returns complement of inputted sequence.
    >>> complement('AATTGCCGT')
    'TTAACGGCA'
    """

    complement = {'A':'T','T':'A','C':'G','G':'C'}
    sequence_complement = ''

    for i in sequence:
        sequence_complement = sequence_complement + complement[i]

    return sequence_complement

#2a.
def min_draft(L):
    """(str) -> str
    returns complement of inputted sequence.
    >>> complement('AATTGCCGT')
    'TTAACGGCA'
    """
    index = 0
    smallest_value = L[0]

    for i in range(1, len(L)):
        if L[i] < smallest_value:
            index = i
            smallest_value = L[i]

#2b.

def min_index(L):
    """ (list) -> (object, int)
    Return a tuple containing the smallest item from L and its index.
    >>> min_index([4, 3, 2, 4, 3, 6, 1, 5])
    (1, 6)
    """ 

    index = 0
    smallest_value = L[0]

    for i in range(1, len(L)):
        if L[i] < smallest_value:
            index = i
            smallest_value = L[i]

    return (smallest_value, index)

#2c.

def min_or_max_index(L, flag):
    """ (list, bool) -> tuple of (object, int)
    Return the minimum or maximum item and its index from L, depending on
    whether flag is True or False.
    >>> min_or_max_index([4, 3, 2, 4, 3, 6, 1, 5], True)
    (1, 6)
    >>> min_or_max_index([4, 3, 2, 4, 3, 6, 1, 5], False)
    (6, 5)
    """ 

    index = 0
    current_value = L[0]

    if flag:
        for i in range(1, len(L)):
            if L[i] < current_value:
                index = i
                current_value = L[i]
    else:
        for i in range(1, len(L)):
            if L[i] > current_value:
                index = i
                current_value = L[i]        

    return (current_value, index)

#3a.
#open file
#read the description line
#loop through description until data is read.
#append the data to the list
#return the quantity per year of the data read from the file

#3b.

def file_data_average(filename):
    """ (str) -> float
    Return the average number of items produced per section for the data in the
    file named filename.
    """ 

    with open(filename, 'r') as newfile:
        
        newfile.readline()

        data = newfile.readline().strip()
        while data.startswith('#'):
            data = newfile.readline().strip()

        data_list = []
        data_list.append(int(data))
        
        for data in newfile:
            data_list.append(int(data.strip()))

    return sum(data_list) / len(data_list)


#6.

def dutch_flag(color_list):
    """ (list of str) -> list of str
    Return color_list rearranged so that 'red' strings come first, 'green' second,
    and 'blue' third.
    >>> color_list = ['red', 'green', 'blue', 'red', 'red', 'blue', 'red', 'green']
    >>> dutch_flag(['red', 'green', 'blue', 'red', 'red', 'blue', 'red', 'green'])
    >>> color_list
    ['red', 'red', 'red', 'red', 'green', 'green', 'blue', 'blue']
    """ 

    i = 0
    start_green = 0
    start_unknown = 0

    end_unknown = len(color_list) - 1

    print(color_list)

    while start_unknown <= end_unknown:

        if color_list[start_unknown] == 'red':
            color_list[start_green], color_list[start_unknown] = color_list[start_unknown], color_list[start_green]
            start_green += 1
            start_unknown += 1

         
        elif color_list[start_unknown] == 'green':
            start_unknown += 1

        
        else:
            color_list[start_unknown], color_list[end_unknown] = color_list[end_unknown], color_list[start_unknown]
            end_unknown -= 1

