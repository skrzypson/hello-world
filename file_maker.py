'''this is a program that creates a series of folders in a desired location
from an input text file'''

import os
import codecs #so the program works for text with polish characters

#asks user for text file destination, changes directory and prints it
text_file_path = input('file destination')
os.chdir(text_file_path)
print(os.getcwd())

#asks user to input text file name without extension
text_file_name = input('file name') + '.txt'

#make temporary list from text file content
file_list_temp = []

#make final list from temporary list
file_list = []

#define function which reads text file lines into a list object
def file_list_maker():
    with codecs.open(text_file_name, 'r', encoding="utf-8") as f:
        file_list_temp = f.read().splitlines()
    for x in file_list_temp:
        e = x
        if '﻿' in x:
            e = x.replace('﻿','')
        file_list.append(e)

print(file_list)

#function that creates new folders
def file_maker():
    i = -1
    for line in file_list:
        i += 1
        newpath = text_file_path + '\\' + line
        print(str(i) + ' ' + newpath)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
            print(newpath)

file_list_maker()
file_maker()