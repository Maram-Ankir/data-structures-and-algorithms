from graph_business_trip import __version__

from graph_business_trip import business_trip , Graph

def test_version():
    assert __version__ == '0.1.0'





def test_success_1():
    graph =Graph()
    Metroville = graph.add_node('Metroville')
    Pandora = graph.add_node('Pandora')
    Arendelle = graph.add_node('Arendelle')
    Narnia= graph.add_node('Narnia')
    graph.add_edge(Metroville,Pandora,250)
    graph.add_edge(Metroville,Arendelle,180)
    graph.add_edge(Arendelle,Narnia,360)
    graph.add_edge(Pandora,Narnia, 210)
    cities=['Metroville','Pandora','Narnia']
    actual= business_trip(graph,cities)
    expected='True, $460'
    assert expected==actual


def test_no_road_btw_cities():
    graph =Graph()
    Metroville = graph.add_node('Metroville')
    Pandora = graph.add_node('Pandora')
    Arendelle = graph.add_node('Arendelle')
    Narnia= graph.add_node('Narnia')
    graph.add_edge(Metroville,Pandora,250)
    graph.add_edge(Metroville,Arendelle,180)
    graph.add_edge(Arendelle,Narnia,360)
    graph.add_edge(Pandora,Narnia, 210)
    cities=['Arendelle','Narnia','Pandora']
    actual= business_trip(graph,cities)
    expected=False
    assert expected==actual


