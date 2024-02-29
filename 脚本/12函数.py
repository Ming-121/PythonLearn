# 函数传递不可变对象
def change(a):
    print(id(a))     # 指向的是同一个对象
    a = 10
    print(id(a))     # 一个新对象

a = 1
print(id(a))
change(a)

'''
140733829894952
140733829894952
140733829895240
'''

# 函数传递可变对象
def changeme(mylist):
    print(id(mylist))
    mylist.append([4, 5, 6])
    print(id(mylist))

mylist = [1, 2, 3]
print(id(mylist))
changeme(mylist)

'''
1758081367872
1758081367872
1758081367872
'''

# 关键字参数
def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return

printinfo( age = 50, name="runoob" )

# 默认参数
def printinfo( name, age = 35 ):
   print ("名字: ", name)
   print ("年龄: ", age)
   return

printinfo(age = 50, name = "runoob" )
print ("------------------------")
printinfo( name = "runoob")

# 不定长参数
# 可写函数说明
def printinfo( arg1, *vartuple ):
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50 )

# lambda
sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))

# return
def fun(a, b):
   return a, b

print(fun(1, 2))