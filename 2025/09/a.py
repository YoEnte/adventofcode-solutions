with open('input.txt', 'r', encoding='utf-8') as file:
    
    red_tiles = []
    
    for row in file:
        tile = tuple(map(int, row.rstrip("\n").split(",")))
        red_tiles.append(tile)

    max_rect = 0
    for a in red_tiles:

        for b in red_tiles:

            rect = (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)
            if rect > max_rect:
                max_rect = rect

    print(red_tiles)
    print(max_rect)

    