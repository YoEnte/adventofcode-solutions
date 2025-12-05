def bin_search(x, l, s, e):
    m = (s + e) // 2
    if e - s < 1:
        return (False, m)
    
    if l[m] == x:
        return (True, m)
    
    if x < l[m]:
        return bin_search(x, l, s, m)
    else:
        return bin_search(x, l, m+1, e)

with open('input.txt', 'r', encoding='utf-8') as file:
    
    count = 0
    ranges = []

    x = 0
    for row in file:
        _row = row.rstrip('\n')
        if ("-" in _row): 
            tr = list(map(int, _row.split("-")))
            print(tr)

            for r in ranges:
                if tr[0] >= r[0] and tr[1] <= r[1]:
                    break

                if tr[0] >= r[0] and tr[0] <= r[1]:
                    tr[0] = r[1]+1
                
                if tr[1] >= r[0] and tr[1] <= r[1]:
                    tr[1] = r[0]-1

                if tr[0] < r[0] and tr[1] > r[1]:
                    r[0] = tr[0]
                    r[1] = tr[1]
                    break

            ranges.append(tr)

            """
            for i in range(tr[0], tr[1]+1):

                has, pos = bin_search(i, fresh, 0, len(fresh))
                if not has and pos == len(fresh):
                    fresh.extend(list(range(tr[0], tr[1]+1)))
                    break

                if not has:
                    fresh.insert(pos, i)

                """
        else:
            break
        
        x+=1

    print(count)
    print(ranges, len(ranges))

    freshcount = 0
    for r in ranges:
        freshcount += len(range(r[0], r[1]+1))
    print(freshcount)