#Shanna, Chang
#changti@onid.oregonstate.edu
#Assignment#1
import os
import sys
import getopt

f=0
e=0
a=0
s=0
u=0
l=0
c=0
h=0
count=0

print "Enter multiple option and enter done when finish."

while True:
    foption = raw_input("Enter option: ")
    if foption == "done": 
        break
    try:
        if foption == 'f':
            f=f+1
        elif foption == 'e':
            e=e+1
        elif foption == 'a':
            a=a+1
        elif foption == 's':
            s=s+1
        elif foption == 'u':
            u=u+1
        elif foption == 'l':
            l=l+1
        elif foption == 'c':
            c=c+1
        elif foption == 'h':
            h=h+1
        else:
            print "Not a valid option"
    except:
        print "Not a valid option"

fname = raw_input("Enter file name: ")

try:
    if h==1:
        print "Option:\nf: remove space before first character\ne: remove space after last character\na: remove all space and tab\ns: remove space before first character and space after last character\nu: change all text to upper case \nl: change all text to lower case\nh: help\n"

    elif c==1:
        word = raw_input("Enter the word you want to count: ")
        fopen = open(fname)
        for line in fopen:
            if line.find(word):
                count = int(count) +1
                continue
        print count
    else:
        fopen = open(fname)
        for line in fopen:
            if f>0:
                line = line.lstrip()
            if e>0:
                line = line.replace(" ", "").replace('\t', "").replace('\n', "")
            if a>0:
                line = line.rstrip()
            if s>0:
                line = line.strip()
            if u>0:
                line = line.upper()
            if l>0:
                line = line.lower()
            print line
except:
    print "not a valid file"
