with open('input.txt', 'r', encoding='utf-8') as file:
    
    tasks = []
    
    for row in file:
        _row = row.rstrip('\n')
        
        splittow = _row.split()
        for i, r in enumerate(splittow):
            
            if len(tasks) <= i:
                tasks.append([])
                
            try:
                tasks[i].append(int(r))
            except:
                tasks[i].insert(0, r)
            
            
    res = 0
    for task in tasks:
        subres = 0
        plus = True
        for j, t in enumerate(task):
            if j == 0:
                if t == '*':
                    plus = False
                    subres = 1
            else:
                if plus:
                    subres += t
                else:
                    subres *= t
                    
        res += subres


    print(res)