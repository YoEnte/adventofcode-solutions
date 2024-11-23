cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
cards.reverse()
buckets = [[], [], [], [], [], [], []]
hands = []
wins = {}

result = []

with open('./a-input.txt') as file:
    for line in file:
        line = line.rstrip()
        
        hands.append(line[0:5])
        wins[hands[-1]] = int(line[6:])

        count = {}
        for i in hands[-1]:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        c = len(count)
        h = hands[-1]

        high_count = 0
        for i in count:
            if count[i] > high_count:
                high_count = count[i]

        if c == 5:
            buckets[0].append(h)
        elif c == 4:
            buckets[1].append(h)
        elif c == 3:
            if high_count == 2:
                buckets[2].append(h)
            elif high_count == 3:
                buckets[3].append(h)
        elif c == 2:
            if high_count == 3:
                buckets[4].append(h)
            elif high_count == 4:
                buckets[5].append(h)
        elif c == 1:
            buckets[6].append(h)


# radixsort like
#print(buckets)
for b in range(len(buckets)):
    copyB = buckets[b].copy()
    #print()
    #print(copyB, "test")

    subBuckets = {} # radix buckets
    for i in cards:
        subBuckets[i] = [];

    for d in range(1, 6):
        f = -d
        
        #print(copyB, "test2")

        for j in copyB:
            #print(subBuckets, j, f, j[f])
            subBuckets[j[f]].append(j)

        copyB = []
        for subB in subBuckets:
            #print(subBuckets[subB], subB, "asd")
            for l in range(len(subBuckets[subB])):
                copyB.append(subBuckets[subB][0])
                subBuckets[subB] = subBuckets[subB][1:]

        #print(copyB, "test3")

    buckets[b] = copyB.copy()

rank = 1
for b in buckets:
    for h in b:
        result.append(rank * wins[h])
        rank += 1

#print('\n')
#print(cards)
#print(hands)
#print(wins)
#print(buckets)
print(result)
print(sum(result))

        