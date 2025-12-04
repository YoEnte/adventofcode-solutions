with open('input.txt', 'r', encoding='utf-8') as file:
    
    count = 0

    for bank in file:
        bank_ = bank.rstrip('\n')
        
        maxi = 0
        maxbatt1 = "0"
        for i in range(0, len(bank_) - 1):
            batt1 = bank_[i]
            if batt1 > maxbatt1:
                maxi = i
                maxbatt1 = batt1

        maxj = 0
        maxbatt2 = "0"
        for j in range(maxi + 1, len(bank_)):
            batt2 = bank_[j]
            if batt2 > maxbatt2:
                maxj = j
                maxbatt2 = batt2

        count += int(maxbatt1 + maxbatt2)

    print(count)