with open('input.txt', 'r', encoding='utf-8') as file:
    
    red_tiles = []
    
    for row in file:
        tile = tuple(map(int, row.rstrip("\n").split(",")))
        red_tiles.append(tile)

    areas = []

    area = set()
    for i, a in enumerate(red_tiles):
        if i > 2:
            pass

        b = red_tiles[(i+2) % len(red_tiles)]
        

        width = abs(b[0] - a[0]) + 1
        w_sign = (width - 1) // (b[0] - a[0])

        height = abs(b[1] - a[1]) + 1
        h_sign = (height - 1) // (b[1] - a[1])

        new_area = set()

        for x in range(width):
            for y in range(height):
                new_area.add((a[0] + (x*w_sign), a[1] + (y*h_sign)))
                # print((a[0] + (x*w_sign), a[1] + (y*h_sign)))
        
        areas.append(new_area)
        print(i)
    
    area = set()
    for i, a in enumerate(areas):
        area |= a & areas[(i+1)%len(areas)]

    '''
    print(area, len(area))
    
    for y in range(9):
        s = ""
        for x in range(14):
            if (x,y) in area:
                s += "X"
            else:
                s += "."

        print(s)
    '''
    max_rect = 0
    for i, a in enumerate(red_tiles):

        for j, b in enumerate(red_tiles):

            rect = (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)
            if rect > max_rect:
                c = (a[0], b[1])
                d = (b[0], a[1])
                """
                neighbors = [
                    red_tiles[(i-1) % len(red_tiles)],
                    red_tiles[(i+1) % len(red_tiles)],
                    red_tiles[(j-1) % len(red_tiles)],
                    red_tiles[(j+1) % len(red_tiles)],
                ]
                """
                if c in area and d in area:
                    #print(rect, a, b, c, d)
                    max_rect = rect

    #print(red_tiles)
    print(max_rect)

    