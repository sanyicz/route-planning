from graph_class import Graph

def Dijkstra(graph, source, target=None):
    distance = {} #distances from source to vertices
    prev = {}
    unvisited = set() #unvisited vertices
    for vertex in graph.vertices:
        distance[vertex] = float('inf') #initialize as infinite
        prev[vertex] = None
        unvisited.add(vertex)
    distance[source] = 0 #distance from source to itself is 0

    while len(unvisited) > 0:
##        print('############################')
        u = None #the current vertex
        minDist = float('inf')
        #u = None
        for vertex in unvisited:
            if distance[vertex] < minDist:
                minDist = distance[vertex]
                u = vertex
                if target != None and u == target:
                    #print(u)
                    return distance, prev
##        print(u, minDist)
        unvisited.remove(u) #mark the current vertex as visited

        for vertex in unvisited: #for every yet unvisited vertex
##            print('----------')
##            print(vertex)
##            print(distance[vertex])
##            print((vertex, u))
            if (vertex, u) in graph.edges.keys(): #if neighbor of u
                alt = distance[u] + graph.edges[(vertex, u)]
            elif (u, vertex) in graph.edges.keys(): #if neighbor of u
                alt = distance[u] + graph.edges[(u, vertex)]
            else:
                alt = float('inf')
##            print(u, vertex, alt)
            if alt < distance[vertex]: #if there is a closer neighbor to u
                distance[vertex] = alt
                prev[vertex] = u
##        if target != None and u == target:
##            print(u)
##            return distance, prev

    return distance, prev

if __name__ == '__main__':
    graph = Graph()
    graph.add_vertex(1, {2 : 7, 3 : 9, 6 : 14})
    graph.add_vertex(2, {3 : 10, 4 : 15})
    graph.add_vertex(3, {4 : 11, 6 : 2})
    graph.add_vertex(4, {5 : 6})
    graph.add_vertex(5, {6 : 9})
    graph.add_vertex(6, {})
    ##print(graph)
    print(graph.edges)
    
    dist, prev = Dijkstra(graph, 1, 4)
    print('dist:', dist)
    print('prev:', prev)
    
