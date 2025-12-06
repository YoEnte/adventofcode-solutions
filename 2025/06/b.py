with open('input.txt', 'r', encoding='utf-8') as file:
    
    rows = []
    for row in file:
        _row = row.rstrip('\n')
        rows.append(_row)

    nums = []
    res = 0
    plus = True
    for c in range(len(rows[0])):
        strnum = ""
        end = False
        for r in range(len(rows)):
            ci = len(rows[r]) - c - 1
            char = rows[r][ci]
            if char in ["+", "*"]:
                end = True
                if char == "+":
                    plus = True
                else:
                    plus = False
            elif char != " ":
                strnum += char

        if strnum != "":
            nums.append(int(strnum))
        
        if end:
            subres = 0
            if not plus:
                subres = 1
            
            for n in nums:
                if plus:
                    subres += n
                else:
                    subres *= n

            res += subres
            nums = []

    print(res)