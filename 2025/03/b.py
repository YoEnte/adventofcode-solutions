
def find_max(string, start, end, old):

    if (end - start < 1 or len(old) >= 12):
        return []

    indeces = []

    maxi = 0
    maxbatt1 = "0"
    for i in range(start, end):
        batt1 = string[i]
        if batt1 > maxbatt1:
            maxi = i
            maxbatt1 = batt1

    indeces.append(maxi)
    
    lin = []
    if (len(indeces) < 12):
        lin = find_max(string, maxi + 1, end, old+indeces)
    
    indeces.extend(lin)

    sin = []
    if (len(indeces) < 12):
        sin = find_max(string, start, maxi, old+indeces)

    indeces.extend(sin)

    return indeces

with open('input.txt', 'r', encoding='utf-8') as file:
    
    count = 0

    for bank in file:

        bank_ = bank.rstrip('\n')
        
        indeces = find_max(bank_, 0, len(bank_), [])

        sindeces = sorted(indeces)

        jolt = ""
        for j in sindeces:
            jolt += bank_[j]
        count += int(jolt)

    print(count)

