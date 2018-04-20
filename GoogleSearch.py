# THIS IS A SIMPLE TOOL TO SEARCH IN GOOGLE ENGINE
# FOR EXAMPLE : SEARCH FOR >>> php?id= (sql injection)
# I'm BEGINNER BUT I WILL DEVELOP MY SKILLS ^_^ .
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

from googlesearch import search
import os
import sys
from time import sleep

green = '\033[1;32m'
greenf = '\033[1;m'
blue = '\033[1;34m'
bluef = '\033[1;m'
red = '\033[1;31m'
redf = '\033[1;m'


def Begin():

    print(red + '''  ____                   _        _   _            _    
     / ___| ___   ___   __ _| | ___  | | | | __ _  ___| | __
    | |  _ / _ \ / _ \ / _` | |/ _ \ | |_| |/ _` |/ __| |/ /
    | |_| | (_) | (_) | (_| | |  __/ |  _  | (_| | (__|   < 
     \____|\___/ \___/ \__, |_|\___| |_| |_|\__,_|\___|_|\_\
                       |___/        ''' + redf)

    print('\n')
    print(red +''' 
       
       +=========================================+
       |.........GOOGLE SEARCH HACKING ..........|
       +-----------------------------------------+
       |#Author:       MR BLACK 15               |
       |#Contact:   www.facebook.com/#           |
       |#Date:          20/04/2018               |
       |#This tool is made for pentesting.       |
       |#Changing the Description of this tool   |
       |Won't made you the coder ^_^ !!!         |
       |#Respect Coderz ^_^                      |
       |#I take no responsibilities for the      |
       |use of this program !                    |
       +=========================================+
       |.........GOOGLE SEARCH HACKING...........|
       +-----------------------------------------+
       ''' + redf)
    print(red + 'THIS IS A SIMPLE TOOL TO SEARCH IN GOOGLE ENGINE')
    print("EX : Search For (sql injection) >> php?id " + redf)
    sleep(7)
    print('\n')
Begin()


def work(file, search_d, time):
    try:
        os.system('touch ' + file + ".txt")
        if not os.path.exists(file + '.txt'):
            os.system('touch ' + file + ".txt")
        elif file == "":
            print(red + '[!] PLEASE ENTER a NAME !' + redf)
    except:
        print(red + '[!] There is a Mistake! ' + redf)
        sys.exit(127)
    try:
        searche = search(search_d, stop=time)
        file_e = open(file + ".txt", 'r+')
    except:

        print(red + 'THERE IS A MISTAKE !' + redf)
    for i in searche:
        file_e.write(i)
        file_e.write('\n')
        print("Adding :: ", i,"To",file,'.txt')
    sleep(3)
    print('\n')
    print('DONE, I Hope That I Helped U ^_^ !')
    print('Check The File {}.txt For Result Report'.format(red+file+redf))


print(blue + 'Give a Name To The File (String | Number)' + bluef)
store = str(input('>>> '))
print(blue + 'Enter What to Search For (String | Number)'+ bluef)
searchd = str(input('>>> '))
while True:
    try:
        print(blue + "How Many URL to Search in (Number)" + bluef)
        time_url = int(input(">>> "))
        break
    except:
        print(red + '[!] Please Put a Number !' + redf)
        sys.exit(2)

work(store, searchd, time_url)
