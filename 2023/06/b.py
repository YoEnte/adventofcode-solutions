result = 0

time = ''
distance = ''

with open('./b-input.txt') as file:
    j = 0
    for line in file:
        line = line.rstrip()
        
        #print(line)
        
        #result.append(0)
        
        w = line[line.index(':') + 2:].split(' ')
        for i in w:
            if not j:
                time += i
            else:
                distance += i
        
        j += 1

time = int(time)
distance = int(distance)
print(time, distance)

for t in range(time + 1):
    ttime = time - t
    #print(ttime, time[i], t)

    if ttime * t > distance:
        result += 1

print(result)

