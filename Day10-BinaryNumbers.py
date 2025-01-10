#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    binary_num = ""
    while n>0:
        r = n%2
        binary_num = str(r) + binary_num
        n = n//2
    
    max_count = 0
    cons_count = 0
    
    for i in binary_num:
        if i=='1':
            cons_count+=1
        elif i=='0':
            if cons_count>max_count:
                max_count=cons_count
            cons_count=0
    if cons_count>max_count:
        max_count=cons_count
        
    print(max_count)
    
