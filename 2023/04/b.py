result = []
card_wins = []
card_count = []

with open('./b-input.txt') as file:
    for line in file:
        line = line.rstrip()
        
        #print(line)
        
        result.append(0)
        card_wins.append(0)
        card_count.append(1)
        
        w = line[line.index(':') + 2:line.index('|') - 1].split(' ')
        wint = []
        for i in w:
            if i != '':
                wint.append(int(i))
        #print(w)
        #print(wint)
        m = line[line.index('|') + 2:].split(' ')
        mint = []
        for i in m:
            if i != '':
                mint.append(int(i))
        #print(m)
        #print(mint)

        for e in mint:
            if e in wint:
                card_wins[-1] += 1
        

#print(card_wins)

for c in range(len(card_wins)):
    #print(c)

    for i in range(card_count[c]):
        for j in range(card_wins[c]):
            card_count[j + c + 1] += 1

        #print(card_count)

#print('')
#print(card_wins)
print(card_count)

print(sum(card_count))

        