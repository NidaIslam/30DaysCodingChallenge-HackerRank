#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    
    name, em = [], []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        
        gmail = emailID.split('@')[1]
        if gmail=='gmail.com':
            name.append(firstName)
            
    name_list = sorted(name)
    for i in range(len(name_list)):
        print(name_list[i])
     
