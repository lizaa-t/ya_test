# Правило выполняется (вложенный случай)

def CircleFactory():
    class Another:
        def foo(self):
            pass

    def Foo():
        pass

    print('hello')
    print('world')


class Triangle():
    def method_one(self):
        # тоже с маленькой, т.к. внутри класса
        def foo():
            pass
        pass

    def method_two(self):
        pass

    class Some:
        def foo(self):
            pass
