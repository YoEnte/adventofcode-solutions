result = []

with open('./a-input.txt') as file:
    for line in file:
        line = line.rstrip()
        
        print(line)
        
        result.append(0)
        
        w = line[line.index(':') + 2:line.index('|') - 1].split(' ')
        wint = []
        for i in w:
            if i != '':
                wint.append(int(i))
        print(w)
        print(wint)
        m = line[line.index('|') + 2:].split(' ')
        mint = []
        for i in m:
            if i != '':
                mint.append(int(i))
        print(m)
        print(mint)

        for e in mint:
            if e in wint:
                if result[-1] == 0:
                    result[-1] += 1
                else:
                    result[-1] *= 2
        
        
        
        

print(result)
print(sum(result))

        