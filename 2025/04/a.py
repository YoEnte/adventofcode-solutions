def inBounds(roll, row, width, height):
    if (roll < 0 or roll >= width):
        return False
    
    if (row < 0 or row >= height):
        return False
    
    return True

with open('input.txt', 'r', encoding='utf-8') as file:
    
    wall = []
    for row in file:
        wall.append(row.rstrip('\n'))
    
    width = len(wall[0])
    height = len(wall)

    count = 0

    for row in range(len(wall)):
        for roll in range(len(wall[row])):
            if wall[row][roll] == '@':
                countrolls = 0
                for y in range(-1, 2):
                    for x in range(-1, 2):
                        if (y == 0 and x == 0):
                            continue

                        newrow = row + y
                        newroll = roll + x

                        if not inBounds(newroll, newrow, width, height):
                            continue

                        if wall[newrow][newroll] == '@':
                            countrolls += 1
                
                if countrolls < 4:
                    count += 1

    print(count)
