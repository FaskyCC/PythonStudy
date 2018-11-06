#创建一个类
class PythonStudent():
    name = None
    age = 18
    course = "python"
    def doHomework(self):
        print("我在做作业呢")
        return None
CC = PythonStudent()
CC.name = "CC"
print(CC.name)
print(CC.age)
print(CC.course)
CC.doHomework()
