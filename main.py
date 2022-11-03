from sys import exit as sys_exit

from checkers import SyntaxChecker, DefNamingChecker
from file_wrapper import PythonCode


def check_code(file: str) -> int:
    student_code = PythonCode(file)

    check_program = [
        SyntaxChecker(student_code),
        DefNamingChecker(student_code)
    ]

    for checker in check_program:
        if checker.is_error_check():
            return 1
    return 0


if __name__ == '__main__':
    input_file = 'tests/test_1.py'
    # input_file = 'tests/test_2.py'
    # input_file = 'tests/test_3.py'
    # input_file = 'tests/test_4.py'
    check_result = check_code(input_file)
    sys_exit(check_result)
