class Student:

    def __init__(self, lastname, firstname, ID):
        """ (Student, str, str, int) -> NoneType

        Create a new student with lastname, firstname, and an ID number.
        >>> student = Student('Smith', 'John', 13596)
        >>> student.lastname
        'Smith'
        >>> student.firstname
        'John'
        >>> student.ID
        13596"""

        self.lastname = lastname
        self.firstname = firstname
        self.ID = ID

        
    
    def __str__(self):
        """ (Student) -> str

        Returns a description of a student as a string

        >>> student = Student('John', 'Smith', 13596)
        >>> student.__str__()
        'Student Name: John,Smith Student ID: 13596'
        """ 

        return '''Student Name: {},{} Student ID: {}'''.format(
            self.lastname, self.firstname, self.ID)



    def __repr__(self):
        """ (self) -> str

        Return a concise string representation of this Student.

        >>> student = Student('John', 'Smith', 13596)
        >>> student.__repr__()
        "Student('John', 'Smith', '13596')"
        """ 

        return "Student('{}', '{}', '{}')".format(
            self.lastname, self.firstname, self.ID)
            
    def __eq__(self, other):
        """ Returns compared matching entries.
        >>> student = Student('Smith', 'John', 13596)
        >>> student1 = Student('Smith', 'James', 13598)
        >>> student == student1
        False
        >>> student2 = Student('miller', 'bernie', 13596)
        >>> student == student2
        True
        >>> student == 5
        False"""

        if isinstance(other, Student):

            return self.ID == other.ID
        else:
            return NotImplemented

    
    def __ne__(self, other):

        """ Returns compared matching entries.
        >>> student = Student('Smith', 'John', 13596)
        >>> student1 = Student('Smith', 'James', 13598)
        >>> student == student1
        False
        >>> student2 = Student('miller', 'bernie', 13596)
        >>> student == student2
        True
        >>> student == 5
        False"""

        if isinstance(other, Student):

            return self.ID != other.ID
        else:
            return NotImplemented

    def __gt__(self, other):
        """ Returns compared matching entries if greater than other.
        >>> student = Student('Smith', 'John', 13596)
        >>> student1 = Student('Smith', 'James', 13598)
        >>> student > student1
        False
        >>> student2 = Student('miller', 'bernie', 13596)
        >>> student > student2
        False
        >>> student > '5'
        False"""

        if isinstance(other, Student):

            return self.firstname > other.firstname and self.lastname > other.lastname and self.ID > other.ID
        else:
            return NotImplemented

    def __ge__(self, other):
        """ Returns compared matching entries if greater than or equal to other.
        >>> student = Student('Smith', 'John', 13596)
        >>> student1 = Student('Smith', 'James', 13598)
        >>> student >= student1
        False
        >>> student2 = Student('miller', 'bernie', 13596)
        >>> student >= student2
        False
        >>> student >= '5'
        False"""

        if isinstance(other, Student):

            return self.firstname >= other.firstname and self.lastname >= other.lastname and self.ID >= other.ID
        else:
            return NotImplemented

    def __lt__(self, other):
        """ Returns compared matching entries if less than other.
        >>> student = Student('Smith', 'John', 13596)
        >>> student1 = Student('Smith', 'James', 13598)
        >>> student < student1
        False
        >>> student2 = Student('miller', 'bernie', 13596)
        >>> student < student2
        False
        >>> student < '5'
        False"""

        if isinstance(other, Student):

            return self.firstname < other.firstname and self.lastname < other.lastname and self.ID < other.ID
        else:
            return NotImplemented
    def __le__(self, other):
        """ Returns compared matching entries if less than or equal to other.
        >>> student = Student('Smith', 'John', 13596)
        >>> student1 = Student('Smith', 'James', 13598)
        >>> student <= student1
        False
        >>> student2 = Student('miller', 'bernie', 13596)
        >>> student <= student2
        True
        >>> student <= '5'
        False"""

        if isinstance(other, Student):

            return self.firstname <= other.firstname and self.lastname <= other.lastname and self.ID <= other.ID
        else:
            return NotImplemented



if __name__ == '__main__':
    import doctest
    doctest.testmod()
