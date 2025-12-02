with open('input.txt', 'r', encoding='utf-8') as file:
    
    data_string = ""

    for line in file:
        data_string += line

    ranges = data_string.split(",")

    count = 0
    k = 0
    for r in ranges:
        tr = list(map(int, r.split("-")))
        #print(tr)

        for i in range(tr[0], tr[1]+1):
            s = str(i)
            
            for sl in range(1, len(s)):
                if (len(s) % sl != 0):
                    continue

                splits = []
                for j in range(len(s) // sl):
                    splits.append(s[j*sl:(j+1)*sl])
                #print(s,sl,splits)
                
                toggle = True
                for sp in range(0, len(splits)-1):
                    toggle = toggle and splits[sp] == splits[sp+1]
                #print(toggle)
                if toggle:
                    count += i
                    break

        k+=1

    print(count)