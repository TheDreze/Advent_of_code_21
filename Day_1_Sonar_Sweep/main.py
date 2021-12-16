# https://adventofcode.com/2021/day/1

list = []
with open('text.txt') as f:
    lines = f.readlines()
    for line in lines:
        number = line.split()
        list.append(number[0])

count = 0
for i in range(len(list)):
    dif = int(list[i]) - int(list[i-1])
    if dif > 0:
        count += 1

print(count)
