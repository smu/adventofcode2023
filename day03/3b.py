
# idea:
#  1. read symbols and their position
#  2. find numbers and ther positions_s_
#  3. compare


class Number(object):
    def __init__(self):
        self.v = None
        self.c = []

    def add_match(self, match, x):
        self.v = int(match.group(0))
        c0 = match.span()
        # all coords for all digits
        for n in range(c0[0], c0[1]):
            self.c.append((n, y))

    def __str__(self):
        return(f"{ self.v } ::  { self.c }")


class Symbol:
    def __init__(self):
        self.s = None
        self.c = []

    def add_match(self, match, x):
        self.s = match.group(0)
        c0 = match.span()
        self.c.append((c0[0], y))

    def __str__(self):
        return(f"{ self.s } ::  { self.c }")

    def find_neightboor(self, numbers):
        neighboors = []
        for n in numbers:
            # print(f'Testing { n }')
            if self.is_neightboor(n):
                neighboors.append(n.v)
        return(neighboors)

    def is_neightboor(self, n):
        c = self.c[0]
        cx = c[0]
        cy = c[1]
        nc = n.c
        for y in (-1,0,1):
            for x in (-1,0,1):
                if (cx+x,cy+y) in nc:
                    return(True)
        return(False)

                


import re

symbol_re = re.compile('\*{1}')
number_re = re.compile('\d+')

numbers  = []
symbols =[]

#with open('day03/input_example') as f:
with open('day03/input') as f:
    y = 0
    for line in f.readlines():
        line = line.rstrip()
        # print(line)
        for s in symbol_re.finditer(line):
            # print(s)
            nn = Symbol()
            nn.add_match(s, y)
            symbols.append(nn)
        for n in number_re.finditer(line):
            nn = Number()
            nn.add_match(n, y)
            numbers.append(nn)
        y += 1


gears = []
for s in symbols:
    print(s)
    # find neighbooring numbers.
    n_num = s.find_neightboor(numbers)
    if len(n_num) == 2:
        gears.append(n_num[0] * n_num[1])


print('-----------------')
print(gears)
print(sum(gears))
