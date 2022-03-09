'''
This is the calculator test file
'''
from calculator import sub, add, div


# this is an example
def test_sub():
    assert sub(0, 0) == 0, "result not correct"
    assert sub(1, 2) == -1, "result not correct"


def test_add():
    assert add([1, 2]) == 3, "result not correct"
    assert add([1, -2]) == -1, "result not correct"


def test_div():
    assert div(1, 2) == 0.5, "result not correct"
    assert div(1, 0) is None, "result not correct"
    assert div(-5, -5) == 1, "result not correct"
    assert div(5, -5) == -1, "result not correct"
    assert div(-5, 5) == -1, "result not correct"
    assert div(0.25, .4) == 0.625, "result not correct"
# add your code here

