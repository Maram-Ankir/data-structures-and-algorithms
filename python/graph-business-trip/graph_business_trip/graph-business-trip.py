
class Queue():
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue (self,value):
        node=Vertex(value)
        if self.front==None:
            self.front=node
            self.rear=node
            return self.rear.value
        else:
            self.rear.next=node
            self.rear=node
            return self.rear.value
    def dequeue(self):
        try:
            if self.front == None:
              raise Exception
            temp=self.front
            self.front=self.front.next
            return temp.value
        except Exception:
            return 'error'
    def isEmpty(self):
        return self.front==None
###############
class Vertex:
    def __init__(self, value):
        self.value = value
class Edge:
    def __init__(self, node, weight=0):
        self.node=node
        self.weight=weight

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        node = Vertex(value)
        self.adjacency_list[node] = []
        return node

    def add_edge(self, start_node, end_node, weight=0):
        if start_node not in self.adjacency_list or  end_node not in self.adjacency_list:
            return None

        edge = Edge(end_node, weight)
        self.adjacency_list[start_node].append(edge)

    def get_nodes(self):
        return [key.value for key in self.adjacency_list]

    def get_neighbors(self, node):
        return [(edge.node.value, edge.weight) for edge in self.adjacency_list[node]]

    def size(self):
        return len(self.adjacency_list)


    # def __str__(self):
    #     output = ''
    #     for vertix in self.adjacency_list.keys():
    #         output += vertix.value
    #         for edge in self.adjacency_list[vertix]:
    #             output += ' -> ' + edge.node.value
    #         output += '\n'
    #     return output



def business_trip(graph,city_name):
    cost=0
    vertic= list(graph.adjacency_list.keys())
    adjacent=set()
    for item in city_name:
        if item not in graph.get_nodes():
            return False
    for i in range(len(city_name)-1):
        for j in vertic:
            if city_name[i]== j.value:
                vertix=j
        for edge in graph.adjacency_list[vertix]:
            adjacent.add(edge.node.value)
            if edge.node.value == city_name[i+1]:
                    cost+= edge.weight
        if city_name[i+1] not in adjacent:
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
