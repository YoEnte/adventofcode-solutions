import copy

def press_button(seq, button):
    for light in button:
        if seq[light] == "#":
            seq = replaceAt(seq, light, '.')
        else:
            seq = replaceAt(seq, light, '#')

    return seq

def replaceAt(string, index, x):
    return string[:index] + x + string[index+1:]

with open('input.txt', 'r', encoding='utf-8') as file:
    
    maschines = []
    
    for row in file:
        maschine_input = row.rstrip("\n").split(" ")

        for i, m in enumerate(maschine_input):
            if i == 0:
                maschines.append({})
                maschines[-1]["goal"] = m[1:-1]
                maschines[-1]["buttons"] = []
                maschines[-1]["sequences"] = [(len(m[1:-1])*".", [])]

            elif i < len(maschine_input) - 1:
                button = tuple(map(int, m[1:-1].split(",")))
                if button in maschines[-1]["buttons"]:
                    print("asdasdads")
                maschines[-1]["buttons"].append(button)


    total = 0
    for i, m in enumerate(maschines):
        print()
        print(i)
        #print(i,m)
        #print(press_button(m["goal"], m["buttons"][0]))

        old_lights = set()
        old_lights.add(m["sequences"][0][0])

        found = -1
        while found == -1:
            #print("\nNEW")
            #print(m["sequences"])
            new_seqs = []
            for j, s in enumerate(m["sequences"]):
                if s[0] == m["goal"]:
                    found = len(s[1])
                    break

                for b in m["buttons"]:
                    new_light = press_button(s[0], b)
                    if new_light in old_lights:
                        continue
                    else:
                        old_lights.add(new_light)
                                 
                    new_seq = copy.deepcopy(s[1])
                    new_seq.append(b)

                    new_seqs.append((new_light, new_seq))

            m["sequences"] = new_seqs

        print(found)
        total += found

    print()
    print(total)