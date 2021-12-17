# https://adventofcode.com/2021/day/1

def part_1():
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

def part_2():
    list = []
    with open('text.txt') as f:
        lines = f.readlines()
        for line in lines:
            number = line.split()
            list.append(number[0])

    sum_list = []
    for i in range(len(list)):
        if i == len(list) - 1 or i == len(list) - 2:
            pass
        else:
            sum = int(list[i]) + int(list[i + 1]) + int(list[i + 2])
            sum_list.append(sum)

    count = 0
    for i in range(len(sum_list)):
        dif = int(sum_list[i]) - int(sum_list[i - 1])
        if dif > 0:
            count += 1

    print(count)

part_2()