#!/usr/bin/env python3
import numpy as np

filename = "input/input_day2.txt"

# Part 1:
input={}
output_p1=np.empty(0)

def check_safety(val):
    val_diff = np.diff(val)
    if (all(val_diff>0) or all(val_diff<0)) and \
        all(abs(val_diff)<=3) and all(abs(val_diff)>=1):
        return True
    else:
        return False

with open(filename, 'r') as file:
    for i, line in enumerate(file):
        entry = np.empty(0)
        for c in line.split():
            entry = np.append(entry, int(c))
        input[i] = entry
        if check_safety(entry):
            output_p1 = np.append(output_p1, 1)
        else:
            output_p1 = np.append(output_p1, 0)
num_p1 = len(output_p1[output_p1==1])
print("Day2-Part1 result: {}".format(num_p1))

# Part 2:
output_p2 = output_p1.copy()
unsafe_index = np.where(output_p1==0)

def check_relaxed_safety_slow(input):
    for lvl in input:
        idx = np.where(input == lvl)[0]
        for i in idx:
            new = np.delete(input, i)
            if check_safety(new):
                return True
    return False

for i, val in input.items():
    if not np.isin(unsafe_index, i).any():
        continue
    val_diff = np.diff(val)
    if (not all(val_diff>0)) and len(val_diff[val_diff<=0])==1:
        idx = np.where(val_diff<=0)[0]
    elif not all(val_diff<0) and len(val_diff[val_diff>=0])==1:
        idx = np.where(val_diff>=0)[0]
    elif any(abs(val_diff)>3) and len(val_diff[abs(val_diff)>3])<=2:
        idx = np.where(abs(val_diff)>3)[0]
    elif any(abs(val_diff)<1) and len(val_diff[abs(val_diff)<1])<=2:
        idx = np.where(abs(val_diff)<1)[0]
    else:
        continue
    if check_safety(np.delete(val, idx[0])) or \
        check_safety(np.delete(val, idx[0]+1)):
        output_p2[i] = 1
    # if check_relaxed_safety_slow(val):  # alternative slow solution
    #     output_p2[i] = 1
num_p2 = len(output_p2[output_p2==1])
print("Day2-Part2 result: {}".format(num_p2))