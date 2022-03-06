'''
This is the calculator test file
'''
from calculator import sub


# this is an example
def test_sub():
    assert sub(0, 0) == 0, "result not correct"
    assert sub(1, 2) == -1, "result not correct"


# add your code here

