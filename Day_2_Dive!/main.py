def part_1():
    number_list = []
    direction_list = []
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
            # line.split(" ")
            direction, number = line.split()
            number_list.append(int(number))
            direction_list.append(direction)

    x = 0
    y = 0
    for i in range(len(number_list)):
        if direction_list[i] == "forward":
            x += number_list[i]
        elif direction_list[i] == "down":
            y += number_list[i]
        elif direction_list[i] == "up":
            y -= number_list[i]

    print(x*y)



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

part_2()