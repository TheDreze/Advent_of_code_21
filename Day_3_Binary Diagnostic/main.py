def part_1():

    list = []
    with open('test.txt') as f:
        lines = f.readlines()
        for line in lines:
            list.append(line.split()[0])
    # print(list)
    sum_1 = 0
    sum_0 = 0
    result = ""
    for i in list:
        for x in i:
            print(i[int(x)])
            if i[int(x)] == "1":
                sum_1 += 1
            elif i[int(x)] == "0":
                sum_0 += 1
            if sum_1 > sum_0:
                result.join("1")
            else:
                result.join("0")

    print(result)


part_1()






def part_2():
    number_list = []
    direction_list = []
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            # line.split(" ")
            direction, number = line.split()
            number_list.append(int(number))
            direction_list.append(direction)

    x = 0
    y = 0
    aim = 0
    for i in range(len(number_list)):
        if direction_list[i] == "forward":
            x += number_list[i]
            y += aim * number_list[i]
        elif direction_list[i] == "down":
            aim += number_list[i]
        elif direction_list[i] == "up":
            aim -= number_list[i]
        print("x: ", x)
        print("y: ", y)
        print("---------")

    print(x * y)

# part_2()