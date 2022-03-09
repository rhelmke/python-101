'''
This is a simple parser.py test file that uses the program's output for functional
verification.
'''

from subprocess import check_output

import parser

SCRIPT_FILE_PATH = parser.__file__

def test_simple_parser_py():
    pass
    # add your simple test code in this function. The code snippet below may be of use for you :-)
    output = check_output(['python3', SCRIPT_FILE_PATH])

