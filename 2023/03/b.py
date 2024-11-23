all_numbers = []
gears = []
result = []

fileContent = []

def check_number(number, start):
    if len(number) > 0:
    
        all_numbers[-1].append([int(number), list(range(start, start + len(number)))])

def check_gear(y, x):
    
    gears.append([y, x, [], []])

    for _y in range(y - 1, y + 2):
        gears[-1][3].append([])
        for _x in range(x - 1, x + 2):
            
            if _y >= 0 and _y <= len(fileContent[0]) and _x >= 0 and _x <= len(fileContent):
                
                for n in all_numbers[_y]:
                    if _x in n[1] and _x not in gears[-1][3][-1]:
                        gears[-1][2].append(n[0])
                        gears[-1][3][-1] += n[1]

with open('./b-input.txt') as file:
    for line in file:
        fileContent.append(line.rstrip())

    for l in range(len(fileContent)):
        line = fileContent[l]

        all_numbers.append([])

        number = ''
        start = 0
        for c in range(len(line)):
            char = line[c]

            if char >= '0' and char <= '9':
                if number == '':
                    start = c
                
                number += char
            else:
                check_number(number, start)

                number = ''
                start = 0

        check_number(number, start)

    for l in range(len(fileContent)):
        line = fileContent[l]

        for c in range(len(line)):
            char = line[c]

            if char == '*':
                check_gear(l, c)


print(all_numbers)
print(gears)

for g in gears:
    if len(g[2]) == 2:
        result.append(g[2][0] * g[2][1])

print(result)
print(sum(result))

        