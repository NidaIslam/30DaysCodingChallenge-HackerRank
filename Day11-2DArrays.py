#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    

    max_sum = -9*7
    for r in range(0,len(arr)-2):
        for c in range(0, len(arr)-2):
            hourglass_sum = (arr[r][c] + arr[r][c+1] + arr[r][c+2] +
             arr[r+1][c+1] +
             arr[r+2][c] +arr[r+2][c+1] + arr[r+2][c+2])
            max_sum = max(max_sum,hourglass_sum)
    print(max_sum)
    