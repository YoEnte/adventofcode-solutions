# Graph library from lecture "Introduction to Algorithms"
from graph import Graph

def dfs(node, graph: Graph):
    if node == "out":
        return 1
    
    succs = graph.get_succs(node)
    if len(succs) == 0:
        return 0
    
    paths = 0
    for _, succ in succs:
        paths += dfs(succ, graph)

    return paths

with open('input.txt', 'r', encoding='utf-8') as file:
    
    graph = Graph()
    
    for row in file:
        start, tos = tuple(row.rstrip("\n").split(":"))

        for to in (tos[1:]).split(" "):
            graph.add_edge(start, 0, to)

    print(dfs("you", graph))