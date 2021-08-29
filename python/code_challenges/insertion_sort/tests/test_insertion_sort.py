from insertion_sort import __version__
import insertion_sort
from insertion_sort.insertion_sort import insertion_Sort


def test_version():
    assert __version__ == '0.1.0'



def test_insertion_fun():
    actual=insertion_Sort([8,4,23,42,16,15])
    assert actual ==[4,8,15,16,23,42]

def test_reverse_sorted():
    actual=insertion_Sort([20,18,12,8,5,-2])
    assert actual ==[-2,5,8,12,18,20]


def test_nearly_sorted():
    actual=insertion_Sort([2,3,5,7,13,11])
    assert actual ==[2,3,5,7,11,13]


