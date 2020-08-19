#!/usr/bin/python3
#Resume_Scanner_Python
#Read Job Description Text File and Clean Duplicates

import csv
from itertools import chain

#Open job description text file
with open(r"/Users/...","r", encoding='utf8') as f:
     cr = csv.reader(f,delimiter=" ") # , is default
     rows = list(cr) 

#Change the multidimentional list to one list
jobposting_list = list(chain.from_iterable(rows))

test_list = jobposting_list
seen = set()
result = []
for item in test_list:
    if item not in seen:
        seen.add(item)
        result.append(item)
print(result)
