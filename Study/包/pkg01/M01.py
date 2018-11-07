#创建一个模块,包含一个类,一个函数,一个输出语句

class Student():
    def __init__(self,name = "No",age = 0):
        self.name = name
        self.age = age
    def selfIntroduce(self):
        print("你好,我的名字是{0},我今年{1}岁了".format(self.name,self.age))

def sayHello():
    print("Hello World")


print("这是一个模块") #最好不要,导入时会执行