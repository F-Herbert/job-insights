from src.pre_built.counter import count_ocurrences

path = "data/jobs.csv"
word = "Python"


def test_counter():
    result = count_ocurrences(path, word)
    assert result == 1639
