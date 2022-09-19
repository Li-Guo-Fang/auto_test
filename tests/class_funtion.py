
class A:
    count = 0
    def fun1(self):
        self.count += 1
        print(self.count)


class B:
    count = 0
    count1 = 100

    @classmethod
    def fun1(cls):
        cls.count += 1
        cls.count1 -= 1
        print(cls.count)
        print(cls.count1)


class C:
    @staticmethod
    def fun1():   #如果方法里面需要self时候不能使用staticmethod
        print('staticmethod1')

    def fun2(self):
        print('staticmethod2')

    def fun3(self):
        self.fun1()

    def fun4(self):
        C.fun1()


class D:
    '''必须包含__enter__，__exit__'''
    def __init__(self,filename):
        self.filename = filename

    def __enter__(self):
        self.f = open(self.filename,'r',encoding='utf-8')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()

    def read(self):
        return self.f.read()


A().fun1()
A().fun1()
A().fun1()

print('-'*50)

B.fun1()
B.fun1()
B.fun1()

print('-'*50)

C.fun1()
C().fun2()
C().fun3()
C().fun4()

print('-'*50)

#上下文管理器
with D('reflections.py') as d:
    print(d.read())






