import os
import sys
import re

def use_regex(input_text):
    # strips {date} {firstname} {lastname}
    pattern = re.compile(r"([0-9]{2}:[0-9]{2}:[0-9]{2}) From ([A-Za-z0-9]+) ([A-Za-z0-9]+)")    
    return pattern.match(input_text)   

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line 

def parse(input_file):
    print(sys.argv)
    
    database = {}
    # array of dictionaries with a date, sender, and message
    count = 0
    with open(input_file, encoding = 'cp850') as f_in:
        for line in nonblank_lines(f_in):
            groups = use_regex(line);
            if groups:
                count += 1
                fname = groups.groups(0)[1]
                lname = groups.groups(0)[2]

                if lname == 'to':
                    lname = 'NLN'
                database[(fname, lname)] = True
    
    print(len(database))
    print(count)


def main():
    if len(sys.argv) == 2:
        print("invalid arguments")
    else:
        parse(sys.argv[1])

main()