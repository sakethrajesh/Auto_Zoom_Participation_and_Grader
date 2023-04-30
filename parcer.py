import os
import sys
import re
import csv

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
    csv_list = []
    csv_columns = ['First Name','Last Name','Grade']

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

                if (fname, lname) not in database:
                    database[(fname, lname)] = True
                    csv_list.append({'First Name':fname, 'Last Name':lname, 'Grade': 1})
    
    print(len(database))
    print(count)
    print(len(csv_list))
    print(csv_list)

    csv_file = "grades.csv"

    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in csv_list:
                writer.writerow(data)
    except IOError:
        print("I/O error")



def main():
    if len(sys.argv) == 2:
        parse(sys.argv[1])
    else:
        print("invalid arguments")
    
main()