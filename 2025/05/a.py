with open('input.txt', 'r', encoding='utf-8') as file:
    
    count = 0
    ranges = []
    fresh = []

    for row in file:
        _row = row.rstrip('\n')
        if ("-" in _row): 
            thisrange = list(map(int, _row.split("-")))
            ranges.append(thisrange)
        elif _row == '':
            fresh.sort()
        else:
            i = int(_row)
            for r in ranges:
                if i >= r[0] and i <= r[1]:
                    count+=1
                    break

    print(count)