import os
import collections
import csv

def filelist(path):

    list_of_files = list(os.walk(path))
    extensions = []
    for files in list_of_files:
        for filename in files[-1]:
            print(filename)
            line = filename[::-1].lower().split('.')[0][::-1]
            for row in extensions:
                if line in row[0]:
                    row[1] +=1
                    break
            else:
                extensions.append([line,1])
    for line in sorted(extensions):
        print('{}: {}'.format(line[0],line[1]))


def filecollection(path):

    extensions = collections.defaultdict(int)
    list_of_files = list(os.walk(path))
    for path, dirs, files in list_of_files:
       for filename in files:
           if os.path.splitext(filename.lower())[1] == '':
               continue
           extensions[os.path.splitext(filename.lower())[1]] += 1
    for key,value in sorted(extensions.items()):
        x = key[1:]
        print('{}: {}'.format(x,value))


def filedict(path):

    list_of_files = list(os.walk(path))
    extensions = {}
    for files in list_of_files:
        for filename in files[-1]:
            line = filename[::-1].split('.')[0][::-1]
            print(line)
            if line in extensions:
                extensions[line] +=1
            else:
                extensions[line] = 1
                print(extensions)
    for key, value in sorted(extensions.items()):
        print('{}: {}'.format(key,value))


def double_list(path):
   
    list_of_files = list(os.walk(path))
    extensions = []
    values = []
    extensions1 = []
    for files in list_of_files:
        for filename in files[-1]:
            line = filename[::-1].split('.')[0][::-1]
            for row in extensions:
                if line in row[0]:
                    row[1] +=1
                    break
            else:
                extensions.append([line,1])
    for line in sorted(extensions):
        values.append(line[-1])
    for line in sorted(extensions):
        extensions1.append(line[0])
    for i in range(len(extensions1)):
        print('{}: {}'.format(extensions1[i],values[i]))

def files_in_cwd(path):
    
    path = os.getcwd()
    #path = input('Enter Absolute Filepath of Desired Directory of Files:')
    list_of_files = list(os.walk(path))
    extensions = []
    for files in list_of_files:
        for filename in files[-1]:
            line = filename[::-1].lower().split('.')[0][::-1]
            for row in extensions:
                if line in row[0]:
                    row[1] +=1
                    break
            else:
                extensions.append([line,1])
    for line in sorted(extensions):
        print('{}: {}'.format(line[0],line[1]))
