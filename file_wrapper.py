from __future__ import annotations


class PythonCode:
    """
    Класс-обертка, чтобы хранить содержимое файла и итерироваться
    по нему неограниченное число раз.
    """
    def __init__(self, filename: str) -> None:
        with open(filename, 'r') as py_file:
            self._whole_code = py_file.read()
        self._code_lines = self._whole_code.split('\n')
        self._current_line = -1

    def __iter__(self) -> PythonCode:
        self._current_line = -1  # сбрасываем счетчик строки, чтобы снова итерироваться
        return self

    def __next__(self) -> str:
        try:
            self._current_line += 1
            return self._code_lines[self._current_line]
        except IndexError:
            raise StopIteration

    def whole(self) -> str:
        return self._whole_code
