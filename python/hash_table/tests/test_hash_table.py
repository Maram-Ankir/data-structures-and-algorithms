from hash_table import __version__

from hash_table.hashmap_repeated_word import repeated_word
def test_version():
    assert __version__ == '0.1.0'


def test_word_dupicate():
    str='Once upon a time, there was a brave princess who.'
    actual=repeated_word(str)
    assert actual=='a'

def test_word_no_dupicate():
    str='one day you will look back and laugh on the past'
    actual=repeated_word(str)
    assert actual=='No duplicates'
