# ---------------- 列表推导式 --------------------
print('---------------- 列表推导式 --------------------')
# 计算 30 以内可以被 3 整除的整数:
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples, end='\n\n')

# 过滤掉长度小于或等于3的字符串列表，并将剩下的转换成大写字母：
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names, '\n\n')

print('---------------- 字典推导式 --------------------')
# 使用字符串及其长度创建字典：
listdemo = ['Google','Runoob', 'Taobao']
newdict = {key:len(key) for key in listdemo}
print(newdict, '\n\n')

print('---------------- 集合推导式 --------------------')
# 判断不是 abc 的字母并输出：
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a, type(a), '\n\n')

print('---------------- 元组推导式 --------------------')
a = (x for x in range(1, 10))
print(a, type(a))   # <generator object <genexpr> at 0x0000024B70D5F1D0> <class 'generator'>
print(tuple(a))     # (1, 2, 3, 4, 5, 6, 7, 8, 9)