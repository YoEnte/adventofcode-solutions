scheme = ""
desertMap = {}

with open('./a-input.txt') as file:
    i = 0
    for line in file:
        line = line.rstrip()
        
        if i == 0:
            scheme = line
        elif i >= 2:
            desertMap[line[0:line.index(" =")]] = (line[line.index("(") + 1:line.index(",")], line[line.index(", ") + 2:line.index(")")])

        i += 1



pos = 'AAA'
depth = 0
while True:
    print(pos, depth)

    if pos == 'ZZZ':
        break

    move = depth % len(scheme)
    nextStep = ''
    if scheme[move] == "L":
        nextStep = desertMap[pos][0]
    elif scheme[move] == "R":
        nextStep = desertMap[pos][1]

    pos = nextStep
    depth += 1

#print(scheme)
#print(desertMap)
print(depth)
        