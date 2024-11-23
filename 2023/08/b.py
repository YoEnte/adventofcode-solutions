scheme = ""
desertMap = {}
pos = []

with open('./b-input.txt') as file:
    i = 0
    for line in file:
        line = line.rstrip()
        
        if i == 0:
            scheme = line
        elif i >= 2:
            key = line[0:line.index(" =")]
            value = (line[line.index("(") + 1:line.index(",")], line[line.index(", ") + 2:line.index(")")])
            desertMap[key] = value

            if key.endswith('A'):
                pos.append(key)

        i += 1

importOld = True
if importOld:
    depth = 1487723409
    pos = ['SCZ', 'LFC', 'HLJ', 'PTZ', 'NQZ', 'SLK']
else:
    depth = 0

while True:

    zCounter = 0
    move = depth % len(scheme)
    side = 0
    if scheme[move] == "R":
        side = 1

    nextSteps = []
    for p in pos:
        nextP = desertMap[p][side]
        nextSteps.append(nextP)
        if nextP.endswith('Z'):
            zCounter += 1

    pos = nextSteps.copy()
    depth += 1

    if zCounter >= 3:
        print(depth, pos, scheme[move], zCounter * "###   ")

    if zCounter == len(pos):
        break

print(scheme)
print(desertMap)
print(depth)
        