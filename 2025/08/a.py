import math

iterations = 10

def euclid(x,y,z):
    return math.sqrt(x**2 + y**2 + z ** 2)

with open('input-test.txt', 'r', encoding='utf-8') as file:
    
    boxes = []
    matrix = []
    circuits = {}
    
    for row in file:
        box = tuple(map(int, row.rstrip("\n").split(",")))
        boxes.append(box)
        circuits[box] = [box]

    for i, b1 in enumerate(boxes):
        matrix.append([])
        for j, b2 in enumerate(boxes):
            d = euclid(b1[0]-b2[0], b1[1]-b2[1], b1[2]-b2[2])
            if d == 0:
                d = float('inf')
            matrix[-1].append((d, j, i))

    for i in range(iterations):
        minimum = min( [min(x) for x in matrix] )
        #print(minimum)
        matrix[minimum[1]][minimum[2]] = (float('inf'), minimum[1], minimum[2])
        matrix[minimum[2]][minimum[1]] = (float('inf'), minimum[2], minimum[1])

        fst = boxes[minimum[1]]
        snd = boxes[minimum[2]]
        

        #print(circuits[fst])
        #print(circuits[snd])
        combined = circuits[fst]
        for s in circuits[snd]:
            if s not in combined:
                combined.append(s)
                
        #print(combined)
        for c in combined:
            circuits[c] = combined
    
    uniques = []
    for c in circuits:
        if circuits[c] not in uniques:
            uniques.append(circuits[c])
    lens = [len(x) for x in uniques]
    lens.sort(reverse=True)
    print(math.prod(lens[:3]))
    
    """
    for c in circuits:
        print(circuits[c]) 
    print()
    for u in uniques:
        print(u) 
    """