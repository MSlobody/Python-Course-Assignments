import re

#extracting the numbers from the text file "regex_sum_322935.txt" and finding the sum of those values.

handle = open("regex_sum_322935.txt")
lst_of_strnumbers = []
numbers = []

for line in handle:
    y = re.findall('[0-9]+', line)
    if len(y) >= 1:
        lst_of_strnumbers += y


for entry in lst_of_strnumbers:
    numbers.append(int(entry))

total_num = sum(numbers)
print(total_num)
