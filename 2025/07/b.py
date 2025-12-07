save_table = {}

def godown(manifold, r, c):
    
    if r == len(manifold):
        return 1
    
    if (r,c) in save_table:
        return save_table[(r,c)]
    
    timelines = 0
    if manifold[r][c] == "^":
        timelines = godown(manifold, r+1, c-1) + godown(manifold, r+1, c+1)
    else:
        timelines = godown(manifold, r+1, c)

    save_table[(r,c)] = timelines
    return timelines

with open('input.txt', 'r', encoding='utf-8') as file:
    
    manifold = []
    timelines = 0
    spos = 0
    
    for i, row in enumerate(file):
        manifold.append(row.rstrip("\n"))
        if i == 0:
            for j, x in enumerate(row):
                if x == "S":
                    spos = j

    timelines = godown(manifold, 1, spos)
    print(timelines)