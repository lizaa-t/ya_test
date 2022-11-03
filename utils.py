def is_lowercase_start(function_name):
    return function_name[0].islower()


def is_uppercase_start(function_name):
    return function_name[0].isupper()


def is_ignore_line(line):
    return line.isspace() or line.lstrip().startswith('#') or not line


def is_function_definition(line):
    return line.lstrip().startswith('def ')


def is_class_definition(line):
    return line.lstrip().startswith('class ')


def get_function_name(line):
    return line.strip().replace('def ', '')


def get_line_indentation(line, indent_size=4):
    return (len(line) - len(line.lstrip())) // indent_size
