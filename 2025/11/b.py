# Graph library from lecture "Introduction to Algorithms"
from graph import Graph

transposition = {}

def dfs(node, graph: Graph, has_dac, has_fft, visited):
    print(node, visited)
    if node == "out":
        if has_dac and has_fft:
            return 1
        else:
            return 0
    
    if (node, has_dac, has_fft) in transposition:
        return transposition[(node, has_dac, has_fft)]
    

    succs = graph.get_succs(node)
    if len(succs) == 0:
        return 0
    
    paths = 0
    for _, succ in succs:
        paths += dfs(succ, graph, has_dac or node == "dac", has_fft or node == "fft", visited+1)

    transposition[(node, has_dac, has_fft)] = paths
    return paths

with open('input.txt', 'r', encoding='utf-8') as file:
    
    graph = Graph()
    
    for row in file:
        start, tos = tuple(row.rstrip("\n").split(":"))

        for to in (tos[1:]).split(" "):
            graph.add_edge(start, 0, to)

    print(dfs("svr", graph, False, False, 0))