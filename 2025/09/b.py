#
#   NOT WORKING
#

def inrect(pos, rect):
    a,b = rect

    if ((pos[0] >= a[0] and pos[0] <= b[0]) or (pos[0] <= a[0] and pos[0] >= b[0])) \
    and ((pos[1] >= a[1] and pos[1] <= b[1]) or (pos[1] <= a[1] and pos[1] >= b[1])):
        return True
                
    return False

def iscorner(pos, rect):
    return pos in rect or pos == (rect[0][0], rect[1][1]) or pos == (rect[1][0], rect[0][1])
        
def on_line(pos, line):
    if line[0][0] == line[1][0]:
        return pos[0] == line[0][0] and ((pos[1] >= line[0][1] and pos[1] <= line[1][1]) or (pos[1] >= line[1][1] and pos[1] <= line[0][1]))

    if line[0][1] == line[1][1]:
        return pos[1] == line[0][1] and ((pos[0] >= line[0][0] and pos[0] <= line[1][0]) or (pos[0] >= line[1][0] and pos[0] <= line[0][0]))

    return False

def corners(rect):
    a,b = rect
    return ((a[0], a[1]), (b[0], a[1]), (b[0], b[1]), (a[0], b[1]))


with open('input-test2.txt', 'r', encoding='utf-8') as file:
    
    red_tiles = []
    
    for row in file:
        tile = tuple(map(int, row.rstrip("\n").split(",")))
        red_tiles.append(tile)

    rects = []
    lines = set()
    hor_lines = []
    ver_lines = []
    for i, a in enumerate(red_tiles):
        if i > 2:
            pass

        b = red_tiles[(i+1) % len(red_tiles)]
        line = (a, b)
        lines.add(line)
        if a[0] == b[0]:
            hor_lines.append(line)
        else:
            ver_lines.append(line)
        
        b = red_tiles[(i+2) % len(red_tiles)]
        rects.append((a,b))
        
        print(i)
        
    print(lines, len(lines))



    inner_rects = set()

    for i, a in enumerate(red_tiles):
        min_area = float('inf')
        min_rect = (0,0)
        print(i)
        for j, b in enumerate(red_tiles):

            if a == b:
                continue

            if (a,b) in lines or (b,a) in lines:
                continue

            if (b,a) in inner_rects:
                continue


            rect = (a,b)
            rect_cs = corners(rect)
            rect_area = (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)

            rect_lines = []
            for k, c in enumerate(rect_cs):
                c2 = rect_cs[(k+1) % len(rect_cs)]
                rect_lines.append((c, c2))
            
            if abs(a[0]-b[0]) + 1 + abs(a[1]-b[1]) == rect_area:
                continue

            if rect_area >= min_area:
                continue
            
            '''
            #print(rect, rect_cs)
            all_in_area = True
            for c in rect_cs:
                if c not in area:
                    all_in_area = False
                    break

            if all_in_area:
                continue
            '''

            c_on_line_count = 0
            for c in rect_cs:
                if c in red_tiles:
                    c_on_line_count += 1
                else:    
                    for l in lines:
                        if on_line(c,l):
                            c_on_line_count += 1
                            break

            if c_on_line_count < 4:
                # use minium inner rects
                continue

            line_counter = 0
            for rl in rect_lines:
                la, lb = rl
                signx = 1
                if lb[0] - la[0] < -1:
                    signx = -1

                signy = 1
                if lb[1] - la[1] < -1:
                    signy = -1
                
                #print("LINE", rl)
                line_coords = [(la[0]+signx*x,la[1]+signy*y) for x in range(abs(lb[0] - la[0])+1) for y in range(abs(lb[1] - la[1])+1)]
                #print(line_coords)

                tile_counter = 0
                for lc in line_coords:
                    if lc in red_tiles:
                        tile_counter += 1

                if tile_counter > 2:
                    line_counter += 1

            #print()
            print("LCOUNT", line_counter)
            if line_counter == 0:
                min_rect = rect
                min_area = rect_area
            
        if min_rect != (0,0):
            inner_rects.add(min_rect)
                    

    print("inner", inner_rects, len(inner_rects))

    
    
    area = set()
    
    for i, ir in enumerate(inner_rects):
        a,b = ir
        print(i,a,b, (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1))
        width = abs(b[0] - a[0]) + 1
        w_sign = (width - 1) // (b[0] - a[0])

        height = abs(b[1] - a[1]) + 1
        h_sign = (height - 1) // (b[1] - a[1])

        new_area = set()
        for x in range(width):
            for y in range(height):
                area.add((a[0] + (x*w_sign), a[1] + (y*h_sign)))

    print(area)
    
    for y in range(9):
        s = ""
        for x in range(14):
            if (x,y) in area:
                s += "#"
            else:
                s += "."
                
        print(s)

    
    
    

    max_rect = 0

    for i, a_ in enumerate(red_tiles):
        print(i)
        a_rects = []
        for j, b_ in enumerate(red_tiles):
            
            rect = (a_,b_)
            rect_area = (abs(a_[0]-b_[0])+1) * (abs(a_[1]-b_[1])+1)
            a_rects.append((rect_area, rect))



        sorted_rects = sorted(a_rects, reverse=True)

        for s in sorted_rects:

            rect_area, rect = s
            a,b = rect

            if rect_area <= max_rect:
                continue

            if a == b:
                continue

            if (a,b) in lines or (b,a) in lines:
                continue

            rect_cs = corners(rect)
            print("RECT", rect, rect_area, max_rect, i)
            #print(rect_cs)
            rect_lines = []
            for k, c in enumerate(rect_cs):
                c2 = rect_cs[(k+1) % len(rect_cs)]
                rect_lines.append((c, c2))
            
            #print(rect_lines)
            corner_counter = 0
            for c in rect_cs:
                if c in red_tiles:
                    corner_counter += 1
                else:
                    for ir in inner_rects:
                        if inrect(c, ir):
                            corner_counter += 1
                            break
                
            
            if corner_counter < 4:
                continue
            
            line_counter = 0
            for rl in rect_lines:
                la, lb = rl
                signx = 1
                if lb[0] - la[0] < -1:
                    signx = -1

                signy = 1
                if lb[1] - la[1] < -1:
                    signy = -1
                
                #print("LINE", rl)
                line_coords = [(la[0]+signx*x,la[1]+signy*y) for x in range(abs(lb[0] - la[0])+1) for y in range(abs(lb[1] - la[1])+1)]
                #print(line_coords)

                inner_counter = 0
                for lc in line_coords:
                    for ir in inner_rects:
                        if inrect(lc, ir):
                            inner_counter += 1
                            break

                if inner_counter == len(line_coords):
                    line_counter += 1

            #print()
            
            if line_counter == 4:
                max_rect = rect_area

    print(max_rect)
    exit()
