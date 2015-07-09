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
h=0

try:
    opts, args = getopt.getopt(sys.argv[1:], 'feasulh')
    for opt, arg in opts:
        if opt == '-f':
            f=f+1
        if opt == '-e':
            e=e+1
        if opt == '-a':
            a=a+1
        if opt == '-s':
            s=s+1
        if opt == '-u':
            u=u+1
        if opt == '-l':
            l=l+1
        elif opt == '-h':
            h=h+1
except:
    print "not a valid option"

if h==1:
    print "Option:\nf: remove space before first character\ne: remove space after last character\na: remove all space and tab\ns: remove space before first character and space after last character\nu: change all text to upper case \nl: change all text to lower case\nh: help\n"

else:
    for line in sys.stdin.readlines():
        if f==1:
            line = line.lstrip()
        if a==1:
            line = line.replace(" ", "").replace('\t', "").replace('\n', "")
        if e==1:
            line = line.rstrip()
        if s==1:
            line = line.strip()
        if u==1:
            if l==1:
                print "Can't lower and upper in the same time."
                break
            else:
                line = line.upper()
        if l==1:
            if u==1:
                break
            else:
                line = line.lower()

        print line
