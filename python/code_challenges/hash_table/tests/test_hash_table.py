from hash_table import __version__
from hash_table.hash_table import Hashmap

def test_version():
    assert __version__ == '0.1.0'

def test_add():
  test=Hashmap()
  test.add('maram','name')
  assert test.contains('maram')==True


