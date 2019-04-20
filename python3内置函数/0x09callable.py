print(callable(0))
print(callable(1))


def test():
    print('good')


print(callable(test))


class Test1(object):
    def test_class(self):
        print('very good')


print('==========Test1:===========')
print(callable(Test1))
a = Test1()
print(callable(a))


class Test2(object):
    def __call__(self):
        print('good job')


print('==========Test2:===========')
print(callable(Test2))
b = Test2()
print(callable(b))
