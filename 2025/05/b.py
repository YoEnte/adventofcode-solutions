with open('input.txt', 'r', encoding='utf-8') as file:
    
    count = 0
    ranges = []
    ranges_queue = []

    x = 0
    for row in file:
        _row = row.rstrip('\n')
        if ("-" in _row): 
            tr = list(map(int, _row.split("-")))
            #print(tr)

            ranges_queue.append(tr)

        else:
            break
        
        x+=1
        
    while len(ranges_queue) > 0:
        tr = ranges_queue.pop(0)
        still_append = True
        for r in ranges:
            if tr[0] >= r[0] and tr[1] <= r[1]:
                still_append = False
                break

            if tr[0] >= r[0] and tr[0] <= r[1]:
                ranges_queue.append([r[1]+1,tr[1]])
                still_append = False
                break
            
            if tr[1] >= r[0] and tr[1] <= r[1]:
                ranges_queue.append([tr[0],r[0]-1])
                still_append = False
                break

            if tr[0] < r[0] and tr[1] > r[1]:
                ranges_queue.append([tr[0],r[0]-1])
                ranges_queue.append([r[1]+1,tr[1]])
                still_append = False
                break

        if still_append:
            ranges.append(tr)

    #print(count)
    #print(ranges, len(ranges))

    freshcount = 0
    for r in ranges:
        freshcount += len(range(r[0], r[1]+1))
    print(freshcount)