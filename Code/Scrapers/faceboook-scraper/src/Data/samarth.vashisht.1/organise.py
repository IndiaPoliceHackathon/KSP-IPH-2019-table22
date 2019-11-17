import os
import glob
structured=dict()
'''
def print_contents(contents):
    for i in contents:
        if(i=="\n"):
            pass
        else:
            print(i)

'''
'''
def file_read(filename):
    filecontents=open(filename)
    a=filecontents.readlines()
    if(filename == "Contact and Basic Info.txt"):
        if("No" in a[1]):
            a=a[2:]
            if("No" in a[1]):
                pass
            else:
                print(a[0])
                print_contents(a[1:])
        else:
            print(a)
            print("Nothing")
    if(filename == "Details About.txt"):
        a=filecontents.readlines()
        if("No" in a[1]):
            a=a[2:]
            if("No" in a[1]):
                pass
            else:
                print(a[0])
                print_contents(a[1:])
        else:
            print(a)
            print("Nothing")
    if(filename == "Details About.txt"):
        if("No" in a[1]):
            a=a[2:]
            if("No" in a[1]):
                pass
            else:
                print(a[0])
                print_contents(a[1:])
        else:
            print(a)
            print("Nothing")
    if(filename == "Family and Relationships.txt"):
        if("No" in a[1]):
            a=a[2:]
            if("No" in a[1]):
                pass
            else:
                print(a[0])
                print_contents(a[1:])
        else:
            print(a)
            print("Nothing")
    

for filename in glob.glob('*.txt'):
    file_read(filename)
'''

for filename in glob.glob('*.txt'):
    f=open(filename)
    print(f.read())

    

