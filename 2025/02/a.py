with open('input.txt', 'r', encoding='utf-8') as file:
    
    data_string = ""

    for line in file:
        data_string += line

    ranges = data_string.split(",")

    count = 0
    i = 0
    for r in ranges:
        tr = list(map(int, r.split("-")))
        #print(tr)

        for i in range(tr[0], tr[1]+1):
            s = str(i)
            le = len(s) // 2
            #print(i,s,l,s[:l],s[l:])

            if s[:le] == s[le:]:
                count += i

        i+=1

    print(count)