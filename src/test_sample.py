# content of test_sample.py
def add_one(x):
    return x + 1


def test_add_one():
    assert add_one(4) == 5

def test_add_one_2():
    assert add_one(3) == 5
