from utils import *
from file_wrapper import PythonCode


class SyntaxChecker:
    """Класс для проверки наличия синтаксических ошибок."""

    def __init__(self, input_code: PythonCode) -> None:
        self.input_code = input_code

    def is_error_check(self) -> bool:
        # для проверки наличия синтаксических ошибок решила пойти простым путем :)

        # Но если ставить перед собой задачу - проверить Правило и наличие синтаксических ошибок
        # за один проход по коду, то можно было бы реализовать анализ AST
        # https://docs.python.org/3/library/ast.html#ast.parse
        # Но кажется, тогда получится реализация exec(), но с модификацией для проверки Правила
        try:
            exec(self.input_code.whole())
        except Exception:
            return True
        return False


class DefNamingChecker:
    """
    Класс для проверки ошибок в именах функций и методов.

    self._input_code -- входной код
    self._current_scope -- стэк, отслеживающий текущий scope,
                           (<функция/класс>, <уровень отступа>)
    self._is_in_class_scope -- счетчик для вложенных классов
    self._current_indentation -- уровень отступа текущей строки
    self._current_function -- имя текущей функции
    """

    def __init__(self, input_code: PythonCode) -> None:
        self._input_code = input_code
        self._current_scope = []
        self._is_in_class_scope = 0
        self._current_indentation = 0
        self._current_function = None

    def _refresh_scope(self) -> None:
        """Метод для обновления scope, если текущий scope закончился."""
        while self._current_scope and self._current_indentation <= self._current_scope[-1][1]:
            if self._current_scope[-1][0] == 'class':
                self._is_in_class_scope -= 1
            self._current_scope.pop()

    def _is_class_rule_broken(self) -> bool:
        """Проверка правила наименований внутри класса."""
        is_rule_broken = not is_lowercase_start(self._current_function)
        return self._is_in_class_scope and is_rule_broken

    def _is_out_class_rule_broken(self) -> bool:
        """Проверка правила наименований вне класса."""
        is_rule_broken = not is_uppercase_start(self._current_function)
        return not self._is_in_class_scope and is_rule_broken

    def is_error_check(self) -> bool:
        """Основной метод для проверки ошибок."""
        for line in self._input_code:
            if is_ignore_line(line):
                continue

            self._current_indentation = get_line_indentation(line)
            self._refresh_scope()

            if is_function_definition(line):
                self._current_function = get_function_name(line)
                if self._is_class_rule_broken() or self._is_out_class_rule_broken():
                    return True
                self._current_scope.append(('def', self._current_indentation))

            if is_class_definition(line):
                self._current_scope.append(('class', self._current_indentation))
                self._is_in_class_scope += 1
        return False
