#import txt file then search for keyword and print rest of string
#use that search to find com port of spec file
#print out com port and store as variable
#take that variable and replace com of txt file in folder (default com1)

import subprocess as sp
import time
import pyautogui as pa
import os


# getting location of txt file and setting it to read and storing as fp
with open (r'C:\svdu5_test\Specification File G5 - Rev_D.txt', 'r') as fp:
    # checking each line in fp = text file(r)
   for line in fp:
    # if "keyword" is in line
    if "COM-SK:" in line:
        # print and store to new variable we could just use line as well
        new_string = line
                
# Function which returns last word
def lastWord(string):
   
    # taking empty string
    newstring = ""
     
    # getting length of string
    length = len(string)
     
    # starting from last
    for i in range(length-1, 0, -1):
       
        # if space is occurred then return
        if(string[i] == " "):
           
            # return reverse of newstring
            return newstring[::-1]
        else:
            newstring = newstring + string[i]

string = new_string

com = lastWord(string)

def func(value):
    return ''.join(value.splitlines())

# Phrase will be replaced with txt file which contains same text info
file = open('C:\\svdu5_test\\puttyserialcom.txt', 'r')
data = file.readline()

# Index 18 is the position of the letter we want to overwrite (c)om1
index = 18

# Issue with this new variable, keeps printing in two lines
new = data[:index] + com + data[index+4:]
final = (func(new))
# print(final)

os.popen("Start cmd")
time.sleep(3)
open("C:\\svdu5_test\\puttyserialcom.txt", "r")
time.sleep(3)
for line in open("C:\\svdu5_test\\cdsvdu5.txt","r"):
    pa.typewrite(line)
    pa.press("enter")
time.sleep(3)
pa.typewrite(final)
pa.press('enter')
