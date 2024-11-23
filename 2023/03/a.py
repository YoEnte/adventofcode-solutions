result = []

fileContent = []

def check(number, start):
    if len(number) > 0:
        hasSymbole = False
        print(number)
        for y in range(l - 1, l + 2):
            for x in range(start - 1, start + len(number) + 1):
                if y >= 0 and y < len(fileContent) and x >= 0 and x < len(line):
                    print(y, x, fileContent[y][x])
                    if fileContent[y][x] in ['-', '+', '*', '=', '@', '$', '&', '/', '%', '#']:
                        print(fileContent[y][x])
                        hasSymbole = True
            
        if hasSymbole:
            result.append(int(number))



with open('./a-input.txt') as file:
    for line in file:
        fileContent.append(line.rstrip())

    for l in range(len(fileContent)):
        line = fileContent[l]

        number = ''
        start = 0
        for c in range(len(line)):
            char = line[c]

            if char >= '0' and char <= '9':
                if number == '':
                    start = c
                
                number += char
            else:
                check(number, start)
                
                number = ''
                start = 0

        check(number, start)

        

print(result)
print(sum(result))

        