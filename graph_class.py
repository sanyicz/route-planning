class Graph(object):
    '''
    only one edge between two vertices
    '''
    def __init__(self):
        self.vertices = []
        #a list of vertex label
        #the label can be a number, a coordinate pair in a 2D grid, etc.
        self.edges = {}
        #keys: a tuple of two vertices that are connected
        #values: the length of the edge

    def __str__(self):
        string = 'Graph:'
        for vertex in self.vertices:
            string += '\n' + str(vertex) + ': '
            for edge in self.edges.keys():
                #print(edge)
                if vertex in edge:
                    v = edge[0] if edge[1] == vertex else edge[1]
                    string += str(v) + ', '
        return string

    def add_vertex(self, vertex_number, edges):
        self.vertices.append(vertex_number)
        if edges != []:
            for edge, length in edges.items():
                if (vertex_number, edge) not in self.edges.keys() and (edge, vertex_number) not in self.edges.keys():
                    self.edges[(vertex_number, edge)] = length

    def isEulerian(self):
        '''
        the graph can have at most two vertices with an odd degree
        '''
        odd_degrees = 0
        for vertex in self.vertices:
            degree = 0
            for edge in self.edges:
                if vertex in edge:
                    degree += 1
            if degree % 2 != 0:
                odd_degrees += 1
            if odd_degrees > 2:
                return False
        return True

    def eulerianPath(self):
        if self.isEulerian():
            pass

if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex(1, {2 : 7, 3 : 9, 6 : 14})
    graph.add_vertex(2, {3 : 10, 4 : 15})
    graph.add_vertex(3, {4 : 11, 6 : 2})
    graph.add_vertex(4, {5 : 6})
    graph.add_vertex(5, {6 : 9})
    graph.add_vertex(6, {})
    print(graph)
##    print(graph.edges)
