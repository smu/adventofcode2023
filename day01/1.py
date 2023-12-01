
import re

digits = re.compile('\d')
numbers = []
with open('day01/input') as f:
    for line in f.readlines():
        linenumber = []
        for dd in digits.finditer(line):
            linenumber.append(dd.group(0)) 

        numbers.append(int(  linenumber[0] + linenumber[-1]   ))

#print(numbers)
# a)
#print(sum(numbers))
##  54632


# b)

digits = re.compile('\d')
# Your calculation isn't quite right. It looks like some of the digits are actually spelled out 
# with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
txtnumbers = {'one':'one1one', 'two':'two2two', 'three':'three3three', 'four':'four4four', 'five':'five5five', 'six':'six6six', 'seven':'seven7seven', 'eight':'eight8eight', 'nine':'nine9nine'}
numbers = []
with open('day01/input') as f:
#with open('day01/example_input.txt') as f:
    for line in f.readlines():
        line = line.rstrip()
        for num in txtnumbers.keys():
            line = re.sub(num, str(txtnumbers[num]), line)
        linenumber = []
        for dd in digits.finditer(line):
            linenumber.append(dd.group(0)) 
        numbers.append(int(  linenumber[0] + linenumber[-1]   ))

print(numbers)
print(sum(numbers))
