def part_1():

    list = []
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            list.append(line.split()[0])
    # print(list)
    sum_1 = 0
    sum_0 = 0
    gamma_result = []
    epsilon_result = []

    for i in range(len(list[0])):
        for x in range(len(list)):
            num = list[x][i]
            if num == "1":
                sum_1 += 1
            elif num == "0":
                sum_0 += 1
        if sum_1 > sum_0:
            gamma_number = "1"
            epsilon_number = "0"
        else:
            gamma_number = "0"
            epsilon_number = "1"
        gamma_result.append(gamma_number)
        epsilon_result.append(epsilon_number)
        sum_1 = 0
        sum_0 = 0
    print("Gamma number: ", gamma_result)
    print("Epsilon number: ", epsilon_result)
    gamma_result = "".join(gamma_result)
    epsilon_result = "".join(epsilon_result)
    decimal_gamma = int(gamma_result, base = 2)
    decimal_epsilon = int(epsilon_result, base=2)

    print(decimal_gamma * decimal_epsilon)





# part_1()






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