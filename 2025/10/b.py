import copy

#
#   NOT WORKING (Time efficiency)
#

def press_button_again(seq, button):
    new = list(seq)
    for b in button:
        new[b] += 1

    return tuple(new)

def replaceAt(string, index, x):
    return string[:index] + x + string[index+1:]

def isAbiggerB(a, b):
    for i, x in enumerate(a):
        if x > b[i]:
            return True
        
    return False

with open('input.txt', 'r', encoding='utf-8') as file:
    
    maschines = []
    
    for row in file:
        maschine_input = row.rstrip("\n").split(" ")

        for i, m in enumerate(maschine_input):
            if i == 0:
                maschines.append({})
                maschines[-1]["buttons"] = []

            elif i < len(maschine_input) - 1:
                button = tuple(map(int, m[1:-1].split(",")))
                maschines[-1]["buttons"].append(button)

            elif i == len(maschine_input) - 1:
                maschines[-1]["goal"] = tuple(map(int, m[1:-1].split(",")))
                maschines[-1]["sequences"] = [(tuple([0]*len(maschines[-1]["goal"])), tuple([0]*len(maschines[-1]["buttons"])))]


    total = 0
    for i, m in enumerate(maschines):
        print()
        print(i)
        #print(i,m)
        #print(press_button(m["goal"], m["buttons"][0]))

        old_jolt = set()
        old_jolt.add(m["sequences"][0][0])

        old_buts = set()
        old_buts.add(m["sequences"][0][1])

        found = -1
        while found == -1:
            print("run")
            #print("\nNEW")
            #print(m["sequences"])
            new_seqs = []
            for j, s in enumerate(m["sequences"]):
                if s[0] == m["goal"]:
                    found = sum(s[1])
                    break

                for k, b in enumerate(m["buttons"]):
                    new_but = list(s[1])
                    new_but[k] += 1
                    new_but = tuple(new_but)

                    if new_but in old_buts:
                        continue
                    
                    old_buts.add(new_but)

                    new_jolt = press_button_again(s[0], b)
                    if new_jolt in old_jolt or isAbiggerB(new_jolt, m["goal"]):
                        continue
                    
                    old_jolt.add(new_jolt)
                                 
                    new_seqs.append((new_jolt, new_but))

            m["sequences"] = new_seqs
            print(len(m["sequences"]))
            #print(m["sequences"], len(m["sequences"]))

        print(found)
        total += found

    print()
    print(total)