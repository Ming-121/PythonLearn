# 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
emptySet = set()
print(type(emptySet))

# 直接使用大括号创建集合
set1 = {1, 2, 3, 4}         
# 使用 set() 函数从列表创建集合  
set2 = set([4, 5, 6, 7])     