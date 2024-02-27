# --------------------  基本操作  --------------------
print("--------------------  基本操作  --------------------")
list = [1, "red", "blue", 3, "yellow"]
print(list[0])
print(list[-2])
print(list[0: -1: 2])
for x in list:
    print(x)
print(type(list))
print()

# --------------------  脚本操作符  --------------------
print("--------------------  脚本操作符  --------------------")
L1 = [1, 2, 3]
L2 = [4, 5, 6]
print(L1 + L2)
print(L1 * 3)
print()

# --------------------  列表嵌套  --------------------
print("--------------------  列表嵌套  --------------------")
list = [['a', 'b', 'c'], [1, 2, 3]]
print(list[1][0])
print()

# --------------------  列表比较  --------------------
print("--------------------  列表比较  --------------------")
import operator
a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))
print()
