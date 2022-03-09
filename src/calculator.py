'''
Clean Code 101 calculator hands on

Task 0: Create a branch with your name and switch to it

Task 1: Write a test for a new "div(a, b)" function and implement it ALONG THE WAY
Hints:
- consider the b = 0 case. Especially in your test!
- add your tests to src/tests/test_calculator.py

Task 2: Write a test for a new "add(summands)" function and implement it ALONG THE WAY.
It adds all items in provided by the 'summands' parameter, which is of type list
Hints:
- the list shall have arbitrary many items
- consider the len(summands) = 0 case!
- add your tests to src/tests/test_calculator.py
- don't use the built-in sum() function

Task 3.1: Push your branch to the remote repository
Task 3.2: Setup a Pull Request and assign it to your supervisor (rhelmke)
'''


# this is an example
def sub(minuend, subtrahend):
    return minuend - subtrahend


def add(summands):
    return sum(summands)


def div(divident, divisor):
    try:
        return divident / divisor
    except ZeroDivisionError:
        return None
