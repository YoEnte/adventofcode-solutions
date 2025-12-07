def replaceAt(string, index, x):
    return string[:index] + x + string[index+1:]


with open('input.txt', 'r', encoding='utf-8') as file:
    
    manifold = []
    splits = 0
    
    for row in file:
        manifold.append(row.rstrip("\n"))

    for (i, row) in enumerate(manifold):
        for (j, c) in enumerate(row):

            if (i == 0):
                if c == "S":
                    manifold[i+1] = replaceAt(manifold[i+1], j, "|")
                continue

            if (i == len(manifold) - 1):
                break

            if c == "|":
                if manifold[i+1][j] == ".":
                    manifold[i+1] = replaceAt(manifold[i+1], j, "|")

                elif manifold[i+1][j] == "^":
                    splits += 1
                    if manifold[i+1][j-1] == ".":
                        manifold[i+1] = replaceAt(manifold[i+1], j-1, "|")
                    if manifold[i+1][j+1] == ".":
                        manifold[i+1] = replaceAt(manifold[i+1], j+1, "|")

    print(splits)