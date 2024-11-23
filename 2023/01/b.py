result = []
digitstrings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for i in range(2):
    with open('./01b-input.txt') as file:
        j = 0
        for line in file:
            line = line.rstrip()

            if not i:
                result.append('')

            length = len(line)

            for l in range(length):
                
                anyone = False
                if line[-i] >= '0' and line[-i] <= '9':
                    result[j] += line[-i]
                    anyone = True
                else:
                    for d in range(len(digitstrings)):
                        dgt = digitstrings[d]

                        if (not i and line.startswith(dgt)) or (i and line.endswith(dgt)):
                            result[j] += str(d + 1)
                            anyone = True
                    
                if anyone:
                    if i:
                        result[j] = int(result[j])
                    break

                if i:
                    line = line[:-1]
                else:
                    line = line[1:]

            j += 1

                      
print(sum(result))