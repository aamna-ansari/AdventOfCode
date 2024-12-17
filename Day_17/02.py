*a, b = _file_.split("/")
b = b.split(".")[0]
a = "/".join(a)

l = []
import re

def func(x):
    return [*map(int, re.findall(r"-?\d+", x))]

with open(f"{a}/input/{b}.txt") as f:
    for x in f.read().split("\n"):
        if x != "":
            l.extend(func(x))

from collections import *
import numpy as np
import math
from utils import *

DIAG_DIRS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # Clockwise from north for (i,j): l[di][dj]
ADJ_DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # NESW for (i, j): l[di][dj]

a, b, c, *prog = l

def run(prog, a, b, c):
    def combo(num):
        if num <= 3: return num
        if num == 4: return a
        if num == 5: return b
        if num == 6: return c

    o = []
    ip = 0
    while ip < len(prog):
        instr = prog[ip]
        operand = prog[ip + 1]
        if instr == 0:
            a = a // (2 ** combo(operand))
        elif instr == 1:
            b = b ^ operand
        elif instr == 2:
            b = combo(operand) % 8
        elif instr == 3:
            if a != 0:
                ip = operand - 2
        elif instr == 4:
            b = b ^ c
        elif instr == 5:
            o.append(combo(operand) % 8)
        elif instr == 6:
            b = a // (2 ** combo(operand))
        elif instr == 7:
            c = a // (2 ** combo(operand))
        ip += 2
    return o

print(*run(prog, a, b, c), sep=",")

def rec(n, a):
    if n == -1:
        return a
    a <<= 3
    for x in range(8):
        if run(prog, a + x, 0, 0) == prog[n:]:
            s = rec(n - 1, a + x)
            if s != -1:
                return s
    return -1

print(rec(len(prog) - 1, 0))