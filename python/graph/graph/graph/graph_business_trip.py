from graph.graph import Vertex, Graph

def business_trip(graph,city_names):
    cost=0
    verticess= list(graph.adjacency_list.keys())
    adjacent_nodes=set()

    for item in city_names:
        if item not in graph.get_nodes():
            return False


    for i in range(len(city_names)-1):
        print(i)
        for item in verticess:
            if city_names[i]== item.value:
                vertix=item

        for edge in graph.adjacency_list[vertix]:
            adjacent_nodes.add(edge.node.value)
            if edge.node.value == city_names[i+1]:
                    cost+= edge.weight

        if city_names[i+1] not in adjacent_nodes:
            return False

    return f'True, ${cost}'

if __name__=='__main__':
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    graph.add_edge(a, c,1)
    graph.add_edge(a, e, 2)
    graph.add_edge(b, c,7)
    graph.add_edge(b, f)
    graph.add_edge(c, a)
    graph.add_edge(c, b)
    graph.add_edge(c, e,1)
    graph.add_edge(d, a,6)
    graph.add_edge(d, e)
    graph.add_edge(e, c,3)
    graph.add_edge(e, d,4)
    graph.add_edge(e, f,5)
    graph.add_edge(f, b)
    graph.add_edge(f, e)

    city=['a', 'e', 'c' ]
    city1= ['b', 'c', 'e', 'd','a' ]
    city2= ['g', 'c', 'e', 'd','a' ]
    city2= ['a', 'c', 'e', 'h','a' ]
    city4=['a','c']

    print(business_trip(graph,city))
    print(graph)
