result = []

for i in range(2):
    with open('./01a-input.txt') as file:
        j = 0
        for line in file:
            line = line.rstrip()

            if not i:
                result.append('')

            for k in range(len(line)):

                c = line[(k * (-1) ** i) - i]
                if c >= '0' and c <= '9':
                    result[j] += c
                    if i:
                        result[j] = int(result[j])
                    break
        
            #print("\n")
            j += 1

print(sum(result))

        