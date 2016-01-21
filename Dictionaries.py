#11.8 exercises

#1
def find_dups(a):
    """Returns the number of duplicates from the inputted list
    >>> find_dups([1,1,1,3,4,5,5,3,2,4,6,7,8,9])
    {1, 3, 4, 5}
    >>> find_dups(['lo','li','ol','lo','lo'])
    {'lo'}"""

    num_set= set()
    duplicate_set = set()
    for i in a:
        Blength = len(num_set)
        num_set.add(i)
        Alength = len(num_set)
        if Blength == Alength:
            duplicate_set.add(i)

    return(duplicate_set)
        

#2
def pairs(first,second):
    """Returns a set of pairs from the two inputted sets.
    >>> pairs({'jimi','john','mike'},{'mary','lina','sara'})
    {('jimi', 'sara'), ('john', 'mary'), ('mike', 'lina')}
    >>> pairs({123,456,789},{123,456,789})
    {(456, 456), (123, 123), (789, 789)}"""

    pairs = set()
    num_pairs = len(first)
    for i in range(num_pairs):
        first_set = first.pop()
        second_set = second.pop()
        pairs.add((first_set,second_set),)

    return pairs

#3
def file_owner(filenames):
    """returns authors in PDB files from filenames as a list."""

    authors = set()
    for i in filenames:
        file = open(i)
        for line in file:
            if line.lower().startswith('author'):
                author = line[6:].strip()
                authors.add(author)

    return authors

#4
def sum_val(dictionary):
    """returns number of non duplicate values in a dictionary
    >>> sum_val({'car': 1, 'truck': 2, 'suv': 1})
    2"""
    return len(set(dictionary.values()))

#5
def min_val(particle_probability):
    """returns particle with lowest probability of detection.
    >>> min_val({'meson': 0.55, 'proton': 0.21, 'neutron': 0.03, 'muon': 0.07})
    'neutron'"""
    
    minimum = []
    name = ''
    for particle in particle_probability:
        #print(particle)
        probability = particle_probability[particle]
        #probablility is a set of floats at this point.
        minimum.append(probability)
        minval = min(minimum)
    #print(minval)
    for particle in particle_probability:
        probability = particle_probability[particle]
        if minval == probability:
            name = particle
            return particle

#6
def dub_count(dictionary):
    """Returns number of duplicate values in a given dictionary
    >>> dub_count({'a': 3, 'b': 2, 'c': 4, 'd': 1, 'e': 4})
    1"""
    dubs = 0
    values = list(dictionary.values())
    for i in values:
        if values.count(i) >= 2:
            dubs = dubs + 1
            frequency = values.count(i)
            for a in range(frequency):
                values.remove(i)
                
    return dubs
        
#7
def balanced(color_val):
    """ Returns a true if color_val is a balanced color.
    >>> balanced({'r': 0.5, 'g': 0.2, 'b': 0.8})
    False
    >>> balanced({'r': 0.3, 'g': 0.5, 'b': 0.2})
    True"""
    
    values = list(color_val.values())
    total = sum(values)
    return total == 1.0

#8
def intersection(d1,d2):
    """Returns dictionary composed of key/vals that only occur in
    both dictionaries.
    >>> intersection({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'd': 2, 'b': 2})
    {'a': 1, 'b': 2}"""
    
    intersection = {}
    for (key,value) in d1.items():
        if key in d2 and value == d2[key]:
            intersection[key] = value
    return intersection

#9
def inception(d_in_d):
    """Returns a set of keys from the inner dictionary in d_in_d
    >>> inception({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}})
    {1, 2, 3}"""

    deep_keys = set()
    for key in d_in_d:
        for i in d_in_d[key]:
            deep_keys.add(i)

    return deep_keys

#10
def consistency(d_in_d):
    """ Returns T or F depending on if the dictionaries share the same keys.
    >>> consistency({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}})
    False
    """
    
    deep_key_list = []
    for key in d_in_d:
        deep_keys = list(d_in_d[key].keys())
        deep_keys.sort()
        deep_key_list.append(deep_keys)

    for i in range(1, len(deep_key_list)):
                   
        if len(deep_key_list[0]) != len(deep_key_list[i]):
            return False

        for j in range(len(deep_key_list[0])):
                   if deep_key_list[0][j] != deep_key_list[i][j]:
                       return False
    return True

#11a

def vsparse(v1,v2):
    """Returns sum of sparse vectors v1 and v2.
    >>> vsparse({1: 4, 2: 4}, {2: 5, 3: 6, 5: 6})
    {1: 4, 2: 9, 3: 6, 5: 6}"""
    v_sum = v1.copy()

    for key in v2:
        if key in v_sum:
            v_sum[key] = v_sum[key] + v2[key]
        else:
            v_sum[key] = v2[key]

    return v_sum

#11b
def s_ping(v1,v2):
    """ Returns the Dot Product of sparse vectors v1 and v2.
    >>> s_ping({1: 2, 3: 5}, {2: 4, 1: 5, 5: 6})
    10"""
    dot_prod = 0
    
    for key1 in v1:
        if key1 in v2:
            dot_prod = dot_prod + v1[key1]*v2[key1]

    return dot_prod

#11c
### Will all entries be stored as non zero, if not what class will they be.##


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
