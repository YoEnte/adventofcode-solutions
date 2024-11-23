result = {
    'red': [],
    'green': [],
    'blue': [],
    'total': []
}

with open('./02b-input.txt') as file:
    j = 0
    for line in file:
        result['red'].append(0)
        result['green'].append(0)
        result['blue'].append(0)

        line = line.rstrip()
        line = line[line.index(':') + 2:]
        line = line.replace(';', ',')
        line += ','

        while (len(line) > 0):
            nextKomma = line.index(',')
            now = line[0:nextKomma]

            # here
            if int(now[0:now.index(' ') + 1]) > result[now[now.index(' ') + 1:]][j]:
                result[now[now.index(' ') + 1:]][j] = int(now[0:now.index(' ') + 1])
            
            line = line[nextKomma + 2:]
        
        else:
            result['total'].append(result['red'][j] * result['green'][j] * result['blue'][j]) 

        j += 1

print(sum(result['total']))

