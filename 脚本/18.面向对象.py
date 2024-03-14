# 简单类实例
class People:
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fun(self):
        return (self.name, self.age)
    
# 实例化类
p = People('ming', 18)

# 访问类的属性和方法
print(p.name)
print(p.fun())