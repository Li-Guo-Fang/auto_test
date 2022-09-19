import time

'''用在批量处理调用方法地方'''

class Cal:
    def __init__(self,name='xiaoli'):
        self.name = name

    def add(self,*args):
        print('加法：a + b')
        return sum(*args)

    def sub(self):
        print('减法：a - b')

    def mul(self):
        print('乘法：a * b')

    def mod(self):
        print('除法：a / b')

    #基础写法
    def fun2(self,method):
        if method == 'add':
            return self.add((1,2,3))
        if method == 'sub':
            return self.sub()
        if method == 'mul':
            return self.mul()
        if method == 'mod':
            return self.mod()
        else:
            return f'{method}不存在'

    #反射用法，【性能好】，*代码结构清晰
    def fun(self,method,*args):
        if hasattr(self, method):   #判断方法属性是否存在
            return getattr(self, method)(args) #调用方法
        else:
            print(f'{method}不存在')

    def use_get_set(self,method_name):
        setattr(self, 'fanshe_test', method_name)   #把外面方法加在类里面,重命名fanshe_test
        getattr(self, 'fanshe_test')()  #调用方法

    #eval()用法
    def fun1(self,method):
        eval(method)()


def reflect_test():
    print(time.time())

cal = Cal()

setattr(cal,'name','wangwu')   #可以修改类属性的变量值
print(getattr(cal,'name'))   #调用类属性-变量
print(cal.fun('add',1,2,3))
# cal.fun1('self.sub1')

# cal.use_get_set(reflect_test)  #参数为方法名
# print(cal.fun2('add'))


#
# setattr(cal,'fanshe_test',fanshe_test)
# getattr(cal,'fanshe_test')()




'''
cal = Cal()
# cal.add()
if hasattr(cal,'add'):
    # add1 = getattr(cal,'add')
    # add1()
    getattr(cal, 'add')()

'''



















