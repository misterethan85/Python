###############################################################################
#Author: Ethan Hicks                                                          #
#Published: 7/8/15                                                            #
#Format: Open Source                                                          #
#Use: Program takes in two files containing strings,compares them and prints  #
#the duplicate values.                                                        #
###############################################################################

#!/usr/bin/python

file1 = input('Enter First File to be Compared:')
file2 = input('Enter Second File to be Compared:')

line1=[]
line2=[]
line3=[]

with open(file1,'r') as newfile:
    line = newfile.readlines()
    for i in line:
        line1.append(i.strip(' \n'))
with open(file2,'r') as newfile:
    line = newfile.readlines()
    for i in line:
        line2.append(i.strip(' \n'))        
#print(line1)
#print(line2)
for i in line1:
    line = i
    #print(i)
    for x in line2:
        var = x
    print(var)
        #if i[0] == line:
         #   print(line)
 
