#!/usr/bin/env python3
import numpy as np

filename = "input/input_day1.txt"

# Part1:
input = np.genfromtxt(filename, delimiter="   ", dtype=int)
input_sorted = np.sort(input, axis=0)
d1_result = np.sum(abs(input_sorted[:,0]-input_sorted[:,1]))
print("Day1-Part1 result: {}".format(d1_result))

# Part2:
unique, count = np.unique(input[:,1], return_counts=True)
unique_right = dict(zip(unique, count))
d2_result=0
for left in input[:,0]:
    if left in unique_right.keys():
        d2_result += left*unique_right[left]
print("Day1-Part2 result: {}".format(d2_result))