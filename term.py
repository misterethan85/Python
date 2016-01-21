import csv

def upper_case():
    """ Reads input file data, converts to all uppercase
    and writes altered data to newfile. Returns nothing."""
    
    source = input('Enter Source File:')
    destination = input('Enter Desination File:')
    with open(source,'r') as oldfile:
        data = oldfile.read()
        #print(data)
        newdata = data.upper()
        #print(newdata)
        with open(destination,'w') as newfile:
            newfile.write(newdata)

    oldfile.close()
    newfile.close()

def csv_parse():
    """ takes csv filename as argument and returns tuple of two
    lists containing header data and list of lists"""
    source = input('Enter Source File:')

    x = []
    y = []
    z = tuple()
    
    with open(source,'r') as newfile:
        data1 = newfile.readline()
        data2 = newfile.readlines()
        x.append(data1)
        for i in data2:
            y.append(i)
        z = (x,y)
        #print(x)
        #print(y)
        #print(z)
    return z

def common_birds():
    """ Returns the unique bird names from two lists."""
    n1 = input('Enter First List:')
    n2 = input('Enter Second List:')

    x = []
    uniques1 = set(n1)
    uniques2 = set(n2)
    #for i in uniques1:
    x.append(uniques1)
    x.extend(uniques2)
    #for i in uniques2:
     #   x.append(i)#uniques = uniques1.extend(uniques2)
    print(x)

def csv_dict():
    """ takes csv filename as argument and returns dictionary of two
    lists containing header data and list of lists"""
    source = input('Enter Source File:')

    x = []
    y = []
    z = {}
    with open(source,'r') as newfile:
        data1 = newfile.readline()
        data2 = newfile.readlines()
        x.append(data1)
        for i in data2:
            y.append(i)

        #print(x)
        #print(y)
        #print(z)
   


#if __name__ == '__main__':
#    import doctest
#    doctest.testmod()
    
