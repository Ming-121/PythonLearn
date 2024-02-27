tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d" #  不需要括号也可以
print(type(tup3))

# 元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用：
tup1 = (50)
print(type(tup1))     # 不加逗号，类型为整型

tup1 = (50,)
print(type(tup1))     # 加上逗号，类型为元组