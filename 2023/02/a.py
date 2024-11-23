maxs = {
    'red': 12,
    'green': 13,
    'blue': 14
}

result = []

with open('./02a-input.txt') as file:
    j = 0
    for line in file:
        result.append(0)
        line = line.rstrip()
        line = line[line.index(':') + 2:]
        line = line.replace(';', ',')
        line += ','
        possible = True

        while (len(line) > 0):
            nextKomma = line.index(',')
            now = line[0:nextKomma]

            if int(now[0:now.index(' ') + 1]) > maxs[now[now.index(' ') + 1:]]:
                possible = False
            
            line = line[nextKomma + 2:]

        if possible:
            result[j] += j + 1

        j += 1

print(sum(result))

        