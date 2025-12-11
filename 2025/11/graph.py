class Graph:
    '''
    Variant of the adjacency list implementation from the lecture
    in which arbitrary values (usually strings) can be used as
    node identifiers (key).
    Furthermore, nodes can have an optional label.
    The implementation uses a dictionary (a Hash-Map) for the
    implementation.
    '''
    def __init__(self):
        '''
        the edges and labels are stored in two seperate dictionaries
        '''
        self.graph = {}
        self.double_edges = 0
        
    def add_node(self, node, label=None):
        '''
        add node to the graph
        node is an identifier and label an otional label
        if node does not exist, add it
        if label is given, update label
        '''
        if node not in self.graph:
            self.graph[node] = (label,[])
        elif label is not None:
            old_label, succs = self.graph[node]
            self.graph[node] = (label,succs)
            
    def add_edge(self, start, label, dest):
        '''
        add edge to graph
        if nodes (start and dest) do not exist, add nodes as well
        '''
        self.add_node(start)
        self.add_node(dest)
        if (label, dest) not in self.graph[start][1]:
            self.graph[start][1].append((label, dest))
        else:
            self.double_edges += 1
        
    def add_bi_edge(self, start, label, dest):
        '''
        add edge from start to dest an vice versa to graph
        if nodes (start and dest) do not exist, add nodes as well
        '''
        self.add_edge(start, label, dest)
        self.add_edge(dest, label, start)

    def has_node(self, node):
        '''
        check if node occurs in graph
        '''
        return node in self.graph
                    
    def get_succs(self, node):
        '''
        successors (with edge labels) from the given node
        produces a copy to avoid manipulation from outside
        '''
        return self.graph[node][1].copy() 
    
    def get_node_label(self,node):
        '''
        node label of given node
        no copy needed, since usually strings (or other non-mutable types)
        are used
        '''
        return self.graph[node][0]
    
    def get_nodes_by_label(self, label):
        '''
        return all nodes with given label
        '''
        res = []
        for node in self.graph.keys():
            if self.graph[node][0] == label:
                res.append(node)
        return res
    
    def __str__ (self):
        return str(self.graph)
    
    def from_file(self, filename):
        '''
        read graph from file
        example in 'sh-map.csv'
        '''
        file = open(filename,mode='r')
        lines = file.readlines()
        file.close()
        directed = lines[0] == 'directed\n'
        lines = lines[1:]
        graph = self # Graph()
        for line in lines:
            cols = line.strip().split(',')
            if len(cols) == 2: # node with label
                graph.add_node(cols[0],cols[1])
            else:
                if len(cols) == 4: # edge with additional node label
                    graph.add_node(cols[0],cols[3])
                    cols = cols[:3]
                if directed:
                    graph.add_edge(cols[0],cols[1],cols[2])
                else:      # undirected graph as directed graph with
                            #symetric adges
                    graph.add_bi_edge(cols[0],cols[1],cols[2])
            
        return graph

if __name__ == "__main__":
    g = Graph()
    g = g.from_file('navi/kiel_s.csv')
    print(len(g.graph), g.double_edges)
    g = g.from_file('navi/kiel_z.csv')
    print(len(g.graph), g.double_edges)
    g = g.from_file('navi/kiel_zn.csv')
    print(len(g.graph), g.double_edges)
    g = g.from_file('navi/kiel_wik.csv')
    print(len(g.graph), g.double_edges)
    g = g.from_file('navi/kiel_cau.csv')
    print(len(g.graph), g.double_edges)

    #g = Graph.from_file('cau.csv')
    #print(g)

    g.to_csv('navi/kiel')
