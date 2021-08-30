from merge_sort import __version__
from merge_sort.merge_sort import mergesort

def test_version():
    assert __version__ == '0.1.0'

def test_merge_sort():
    actual=mergesort([8,4,23,42,16,15])
    assert actual ==[4,8,15,16,23,42]


def test_Reverse_sort():
    actual=mergesort([20,18,12,8,5,-2])
    assert actual==[-2,5,8,12,18,20]

def test_nearly_sorted_sort():
    actual=mergesort([2,3,5,7,13,11])
    assert actual==[2,3,5,7,11,13]
