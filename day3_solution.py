#!/usr/bin/env python3
import re

filename = "input/input_day3.txt"

# Part 1:
res_1=0
with open(filename, "r") as file:
    text = "".join([l.strip() for l in file.readlines()])

matches = re.findall(r'mul\((\d+),(\d+)\)', text)
number_pairs = [(int(a), int(b)) for a, b in matches]
res_1 = sum(a * b for a, b in number_pairs)
print("Day3-Part1 result: {}".format(res_1))

# Part 2:
res_2 = 0
disabled = False
matches_with_idx = [(m.start(), m.group()) for m in re.finditer(r'mul\(\d+,\d+\)', text)]
enable_idx = [m.start() for m in re.finditer(r'do\(\)', text)]
disable_idx = [m.start() for m in re.finditer(r'don\'t\(\)', text)]
disable_itvl=[]
if len(disable_idx) > 0:
    for start_idx in disable_idx:
        end_ids = [j for j in enable_idx if j > start_idx]
        end_idx = -1
        if len(end_ids)>0:
            end_idx = end_ids[0]
        if end_idx not in [b for _, b in disable_itvl]:
            disable_itvl.append((start_idx, end_idx))
for idx, str in matches_with_idx:
    disabled = False
    for lower, upper in disable_itvl:
        if idx < lower:
            break
        if disable_itvl[-1][1] != -1 and idx > disable_itvl[-1][1]:
            break
        if upper != -1 and upper < idx:
            continue
        if idx > lower and (idx < upper or upper == -1):
            disabled = True
            break
    if disabled:
        continue
    match = re.search(r'mul\((\d+),(\d+)\)', str)
    res_2 += int(match.group(1))*int(match.group(2))
print("Day3-Part2 result: {}".format(res_2))