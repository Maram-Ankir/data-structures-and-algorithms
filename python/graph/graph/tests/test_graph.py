from graph import __version__
from graph.graph import Graph

def test_version():
    assert __version__ == '0.1.0'


def test_add_node():
    g= Graph()
    one= g.add_node(1)
    two= g.add_node(2)
    b= g.add_node("a")
    g.add_edge(b, one)
    g.add_edge(b, two)
    g.add_edge(one,two)
    expected=[key.value for key in g.adjacency_list]
    assert expected == [1,2,"a"]



def test_add_edge():
    g= Graph()
    one= g.add_node(1)
    two= g.add_node(2)
    a= g.add_node('a')
    g.add_edge(a, one)
    g.add_edge(a, two)
    g.add_edge(one,two)
    expected_val=[1,2]
    b_values=g.adjacency_list[g]
    actual_val=[item.node.value for item in b_values]
    expected_1=[2]
    values_1=g.adjacency_list[g]
    actual_1=[values_1[0].node.value]
    assert expected_val==actual_val
    assert expected_1==actual_1



def test_get_nodes():
    g= Graph()
    one= g.add_node(1)
    two= g.add_node(2)
    a= g.add_node('a')
    g.add_edge(a, one)
    g.add_edge(a, two)
    g.add_edge(one,two)
    actual=g.get_nodes()
    assert actual == [1, 2, 'a']


def test_get_neighbors():
    g= Graph()
    one= g.add_node(1)
    two= g.add_node(2)
    a= g.add_node('a')
    g.add_edge(a, one)
    g.add_edge(a, two)
    g.add_edge(one,two)
    actual=g.get_neighbors(g)
    assert actual == [(1, 0), (2, 0)]



def test_size():
    g= Graph()
    one= g.add_node(1)
    two= g.add_node(2)
    a= g.add_node('a')
    g.add_edge(a, one)
    g.add_edge(a, two)
    g.add_edge(one,two)
    actual= g.size()
    assert actual==3


############## Breadth first ###################

def test_breadth_first():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    graph.add_edge(a, c)
    graph.add_edge(a, d)
    graph.add_edge(b, c)
    graph.add_edge(b, f)
    graph.add_edge(c, a)
    graph.add_edge(c, b)
    graph.add_edge(c, e)
    graph.add_edge(d, a)
    graph.add_edge(d, e)
    graph.add_edge(e, c)
    graph.add_edge(e, d)
    graph.add_edge(e, f)
    graph.add_edge(f, b)
    graph.add_edge(f, e)
    actual=graph.breadth_first(a)
    assert actual == ['b', 'c', 'f', 'a', 'e', 'd']


