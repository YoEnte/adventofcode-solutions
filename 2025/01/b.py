with open('input.txt', 'r', encoding='utf-8') as file:
    
    dial = 50
    count = 0

    for line in file:
        d = line[0]
        num = int(line[1:])

        dire = 1
        if (d == "L"):
            dire = -1

        for i in range(num):
            dial += dire
            dial %= 100
            if dial == 0:
                count += 1

    print(count)