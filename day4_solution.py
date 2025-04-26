#!/usr/bin/env python3
import re
import numpy as np

filename = "input/input_day4.txt"

# Part 1:
res_1=0
input=np.empty(0)
with open(filename, "r") as file:
    for line in file:  # horizontal search
        res_1 += len(re.findall(r'XMAS', line)) + len(re.findall(r'SAMX', line))
        string = np.array([[c for c in line]])[:,:-1]
        if np.size(input)==0:
            input = string
        else:
            input = np.append(input, string, axis=0)

for line in input.transpose():  # vertical search
    text = ''.join(line)
    res_1 += len(re.findall(r'XMAS', text)) + len(re.findall(r'SAMX', text))

rows, cols = input.shape
diagonals = []
# Top-left to bottom-right diagonals
for r in range(rows):
    diag = []
    i, j = r, 0
    while i < rows and j < cols:
        diag.append(input[i,j])
        i += 1
        j += 1
    if len(diag) >= 4:
        text = ''.join(diag)
        diagonals.append(text)
        res_1 += len(re.findall(r'XMAS', text)) + len(re.findall(r'SAMX', text))

for c in range(1,cols):
    diag = []
    i, j = 0, c
    while i < rows and j < cols:
        diag.append(input[i,j])
        i += 1
        j += 1
    if len(diag) >= 4:
        text = ''.join(diag)
        diagonals.append(text)
        res_1 += len(re.findall(r'XMAS', text)) + len(re.findall(r'SAMX', text))

# Top-right to bottom-left diagonals
for r in range(rows):
    diag = []
    i, j = r, cols - 1
    while i < rows and j >= 0:
        diag.append(input[i,j])
        i += 1
        j -= 1
    if len(diag) >= 4:
        text = ''.join(diag)
        diagonals.append(text)
        res_1 += len(re.findall(r'XMAS', text)) + len(re.findall(r'SAMX', text))

for c in range(cols-2,-1,-1):
    diag = []
    i, j = 0, c
    while i < rows and j >= 0:
        diag.append(input[i,j])
        i += 1
        j -= 1
    if len(diag) >= 4:
        text = ''.join(diag)
        diagonals.append(text)
        res_1 += len(re.findall(r'XMAS', text)) + len(re.findall(r'SAMX', text))

print(diagonals) 
print("Day4-Part1 result: {}".format(res_1))
