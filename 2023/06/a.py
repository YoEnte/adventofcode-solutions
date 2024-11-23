result = [1]

time = []
distance = []

with open('./a-input.txt') as file:
    j = 0
    for line in file:
        line = line.rstrip()
        
        #print(line)
        
        #result.append(0)
        
        w = line[line.index(':') + 2:].split(' ')
        for i in w:
            if i != '':
                if not j:
                    time.append(int(i))
                else:
                    distance.append(int(i))
        
        j += 1

#print(time, distance)

for i in range(len(time)):
    result.append(0)
    for t in range(time[i] + 1):
        ttime = time[i] - t
        #print(ttime, time[i], t)

        if ttime * t > distance[i]:
            result[-1] += 1

    result[0] *= result[-1]

print(result)
print(result[0])

        