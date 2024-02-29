# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来：
dic = {'key1': 'value1', 'key2': 'value2'}
for k, v in dic.items():
    print(k, v)

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
for i, v in enumerate(['apple', 'banana', 'pear']):
    print(i, v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合：
questions = ['name', 'sex', 'favorite color']
answers = ['Bob', 'mboy', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

name = 'ming'
print('hello {0}'.format(name))
