from quick_sort import __version__
from quick_sort.quick_sort import quickSort


def test_version():
    assert __version__ == '0.1.0'

def test_success_sort():
    actual=quickSort([75,15,6,2,8,3],0,5)
    assert actual==[2,3,6,8,15,75]

def test_Reverse_sort():
    actual=quickSort([20,18,12,8,5,-2],0,5)
    assert actual==[-2,5,8,12,18,20]


def test_nearly_sorted_sort():
    actual=quickSort([2,3,5,7,13,11],0,5)
    assert actual==[2,3,5,7,11,13]
