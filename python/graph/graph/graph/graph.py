
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

    def add_edge(self, s_node, end_node):
        edge = Edge(end_node)
        self.adjacency_list[s_node].append(edge)

    def get_nodes(self):
        return [key.value for key in self.adjacency_list]

    def get_neighbors(self, node):
        return [(edge.node.value, edge.weight) for edge in self.adjacency_list[node]]

    def size(self):
        return len(self.adjacency_list)

    def breadth_first(self, node):
        nodes=[]
        queue= Queue()
        v_node= set()
        if node not in self.adjacency_list or self.adjacency_list[node]==[]:
            return None
        queue.enqueue(node)
        v_node.add(node.value)
        while not queue.isEmpty():
            vertix=queue.dequeue()
            nodes.append(vertix.value)
            for edge in self.adjacency_list[vertix]:
                if  edge.node.value not in v_node:
                    v_node.add(edge.node.value)
                    queue.enqueue(edge.node)

        return nodes


# if __name__ == '__main__':
#     graph = Graph()
#     a = graph.add_node('a')
#     b = graph.add_node('b')
#     c = graph.add_node('c')
#     d = graph.add_node('d')
#     e = graph.add_node('e')
#     f = graph.add_node('f')
#     graph.add_edge(a, c)
#     graph.add_edge(a, d)
#     graph.add_edge(b, c)
#     graph.add_edge(b, f)
#     graph.add_edge(c, a)
#     graph.add_edge(c, b)
#     graph.add_edge(c, e)
#     graph.add_edge(d, a)
#     graph.add_edge(d, e)
#     graph.add_edge(e, c)
#     graph.add_edge(e, d)
#     graph.add_edge(e, f)
#     graph.add_edge(f, b)
#     graph.add_edge(f, e)
#     print (graph)

