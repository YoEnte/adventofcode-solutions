def inrect(pos, rect):
    width = abs(rect[1][0] - rect[0][0]) + 1
    w_sign = (width - 1) // (rect[1][0] - rect[0][0])

    height = abs(rect[1][1] - rect[0][1]) + 1
    h_sign = (height - 1) // (rect[1][1] - rect[0][1])

    for x in range(width):
        for y in range(height):
            if rect[0][0] + (x*w_sign) == pos[0] and rect[0][1] + (y*h_sign) == pos[1]:
                return True
                
    return False

def iscorner(pos, rect):
    return pos in rect or pos == (rect[0][0], rect[1][1]) or pos == (rect[1][0], rect[0][1])
        
def on_line(pos, line):
    if line[0][0] == line[1][0]:
        return pos[0] == line[0][0] and ((pos[1] >= line[0][1] and pos[1] <= line[1][1]) or (pos[1] >= line[1][1] and pos[1] <= line[0][1]))

    if line[0][1] == line[1][1]:
        return pos[1] == line[0][1] and ((pos[0] >= line[0][0] and pos[0] <= line[1][0]) or (pos[0] >= line[1][0] and pos[0] <= line[0][0]))

def corners(rect):
    return (rect[0], rect[1], (rect[0][0], rect[0][1]), (rect[1][0], rect[0][1]))

board_width = 100000
board_height = 100000



with open('input.txt', 'r', encoding='utf-8') as file:
    
    red_tiles = []
    
    for row in file:
        tile = tuple(map(int, row.rstrip("\n").split(",")))
        red_tiles.append(tile)

    rects = []
    lines = []
    hor_lines = []
    ver_lines = []
    for i, a in enumerate(red_tiles):
        if i > 2:
            pass

        b = red_tiles[(i+1) % len(red_tiles)]
        line = (a, b)
        lines.append(line)
        if a[0] == b[0]:
            hor_lines.append(line)
        else:
            ver_lines.append(line)
        
        b = red_tiles[(i+2) % len(red_tiles)]
        rects.append((a,b))
        
        print(i)
        
    print(lines, len(lines))
    
    '''
    for y in range(board_height):
        s = ""
        for x in range(board_width):
            is_on_line = False
            for l in lines:
                if on_line((x,y), l):
                    is_on_line = True
                    break
            
            if is_on_line:
                s += "#"
            else:
                s += "."
                
        print(s)'''
    
    max_rect = 0
    
    for r in rects:
        rect_area = (abs(r[0][0]-r[1][0])+1) * (abs(r[0][1]-r[1][1])+1)
        if rect_area <= max_rect:
            continue
        
        corners_r = corners(r)
        for c in corners_r:
            print(c)
            if c in red_tiles:
                continue
            
            for l in lines:
                if not on_line(c, l):
                    hor_crosses = 0
                    ver_crosses = 0
                    for v in range(c[1]+1):
                        for hl in hor_lines:
                            if c[1] == v:
                                break
                            if on_line((c[0], v), hl):
                                hor_crosses += 1
                    
                    if hor_crosses % 2 == 0:
                        break
                    
                    for h in range(c[0]+1):
                        for vl in ver_lines:
                            if c[0] == h:
                                break
                            if on_line((h, c[1]), vl):
                                ver_crosses += 1

                    if hor_crosses % 2 == 1 and hor_crosses % 2 == 1:
                        max_rect = rect_area
    
    print(max_rect)
                        
    exit()
    
    
    max_rect = 0
    for i, a in enumerate(red_tiles):

        for j, b in enumerate(red_tiles):

            rect_area = (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)
            rect = (a,b)
            if rect_area > max_rect:
                c = (a[0], b[1])
                d = (b[0], a[1])
                
                if c in rects and d in area:
                    #print(rect, a, b, c, d)
                    max_rect = rect_area

    #print(red_tiles)
    print(max_rect)

    