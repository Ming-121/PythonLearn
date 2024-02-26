# ------------------ 逻辑运算符 --------------------
print("------------------ 逻辑运算符 --------------------")
a, b = 10, 20

print(a and b)
print(a or b)
print(not(a and b))
print(not(a or b))
print()

# ------------------ 成员运算符 --------------------
print("------------------ 成员运算符 --------------------")
a = 10
b = 20
list = [1, 2, 3, 4, 5 ]
 
if ( a in list ):
   print ("1 - 变量 a 在给定的列表中 list 中")
else:
   print ("1 - 变量 a 不在给定的列表中 list 中")
 
if ( b not in list ):
   print ("2 - 变量 b 不在给定的列表中 list 中")
else:
   print ("2 - 变量 b 在给定的列表中 list 中")
 
# 修改变量 a 的值
a = 2
if ( a in list ):
   print ("3 - 变量 a 在给定的列表中 list 中")
else:
   print ("3 - 变量 a 不在给定的列表中 list 中")
print()

# ------------------ 身份运算符 --------------------
print("------------------ 身份运算符 --------------------")
a = 20
b = 20
 
if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")
 
if ( id(a) == id(b) ):
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识")
 
# 修改变量 b 的值
b = 30
if ( a is b ):
   print ("3 - a 和 b 有相同的标识")
else:
   print ("3 - a 和 b 没有相同的标识")
 
if ( a is not b ):
   print ("4 - a 和 b 没有相同的标识")
else:
   print ("4 - a 和 b 有相同的标识")
print()

# ------------------ 海象运算符 --------------------
print("------------------ 海象运算符 --------------------")
# 传统写法
n = 10
if n > 5:
    print(n)
    
# 使用海象运算符
if (n := 10) > 5:
    print(n)
    
# n 次循环的一般写法：    
n = 5
while n:
    print('hello, walrus operator!')
    n -= 1
    
# n 次循环使用海象运算符:
n = 5
while (n := n - 1) + 1: # 需要加1是因为执行输出前n就减1了
    print('hello, walrus operator!')