'''
This is the calculator test file
'''
from calculator import add


# this is an example
def test_add():
    assert add(0, 0) == 0, "result not correct"
    assert add(1, 2) == 3, "result not correct"

# add your tests here

