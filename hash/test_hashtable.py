from pytest import fixture
from hashtable import HashTable


@fixture(scope='session')
def make_hash_table():
    return HashTable(1024)


@fixture(scope='session')
def test_words():
    with open('words') as words:
        word_list = [word.strip() for word in words]
    return word_list


def test_hashtable_creation(make_hash_table):
    test_t = make_hash_table
    for i in range(1024):
        assert test_t.hash_t[i].keys() == []


def test_hashtable_set(test_words, make_hash_table):
    test_t = make_hash_table
    for word in test_words:
        test_t.set(word, word)
    for word in test_words:
        assert word in test_t.hash_t[test_t.hash(word)].values()


def test_hashtable_get(test_words, make_hash_table):
    test_t = make_hash_table
    for word in test_words:
        test_t.set(word, word)
    for word in test_words:
        assert test_t.hash_t[test_t.hash(word)][word] == word
