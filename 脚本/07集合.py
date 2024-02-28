# 创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
emptySet = set()
print(type(emptySet))

# 直接使用大括号创建集合
set1 = {1, 2, 3, 4}         
# 使用 set() 函数从列表创建集合  
set2 = set([4, 5, 6, 7])     

set3 = { 'apple', 'watermelon', 'pear', }
# 添加元素
set3.add('banana')
print(set3)     # {'pear', 'watermelon', 'banana', 'apple'}
set3.update(set([1, 2]))
print(set3)     # {'pear', 1, 2, 'apple', 'watermelon', 'banana'}
# 移除元素
set3.remove('apple')
print(set3)
# 随机移除元素
print('随机移除的元素: ', '')
print(set3.pop())
print('随机移除后的集合：', '')
print(set3)