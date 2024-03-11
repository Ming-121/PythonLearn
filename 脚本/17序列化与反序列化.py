'''
obj -- 序列化对象
fp -- 文件描述符，将序列化的str保存到文件中。
skipkeys -- 默认为False。如果skipkeys是True则将跳过不是基本类型（str，int，float，bool，None）的dict键，不会引发TypeError
ensure_ascii -- 默认值为True，能将所有传入的非ASCII字符转义输出。如果ensure_ascii为False，则这些字符将按原样输出(ensure_ascii=False，让文件中的中文可以直接显示！)
check_circular -- 默认值为True。如果check_circular为False，则将跳过对容器类型的循环引用检查，循环引用将导致OverflowError
allow_nan -- 默认值为True。如果allow_nan为True，则将使用它们的JavaScript等效项（NaN，Infinity，-Infinity）。如果allow_nan为False，则严格遵守JSON规范，序列化超出范围的浮点值（nan，inf，-inf）会引发ValueError
indent -- 设置缩进格式，默认值为None，选择的是最紧凑的表示。如果indent是非负整数或字符串，那么JSON数组元素和对象成员将使用该缩进级别进行输入；indent为0，负数或“”仅插入换行符；indent使用正整数缩进多个空格；如果indent是一个字符串（例如“\t”），则该字符串用于缩进每个级别。
separators -- 去除分隔符后面的空格，默认值为None。如果指定，则分隔符应为（item_separator，key_separator）元组。如果缩进为None，则默认为（’，’，’：’）；要获得最紧凑的JSON表示，可以指定（’，’，’:’）以消除空格。
default -- 默认值为None。如果指定，则default应该是为无法以其他方式序列化的对象调用的函数。它应返回对象的JSON可编码版本或引发TypeError。如果未指定，则引发TypeError。
sort_keys -- 默认值为False。如果sort_keys为True，则字典的输出将按键值排序。

json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
'''
import json

# dumps可以格式化所有的基本数据类型为字符串
data1 = json.dumps([])         # 列表
print(data1, type(data1))
data2 = json.dumps(2)          # 数字
print(data2, type(data2))
data3 = json.dumps('3')        # 字符串
print(data3, type(data3))
dict = {"name": "Tom", "age": 18}   # 字典
data4 = json.dumps(dict)
print(data4, type(data4))

with open("test.json", "w", encoding='utf-8') as f:
    # indent 格式化保存字典，默认为None，小于0为零个空格。indent=4缩进4个空格
    f.write(json.dumps(dict, indent=4))
#   json.dump(dict, f, indent=4)  # 传入文件描述符，和dumps一样的结果
    
print('--------------------------')
print('反序列化')

dict = '{"name": "Tom", "age": 18}'   # 将字符串还原为dict
data1 = json.loads(dict)
print(data1, type(data1))

with open("test.json", "r", encoding='utf-8') as f:
    data2 = json.loads(f.read())    # load的传入参数为字符串类型
    print(data2, type(data2))
    f.seek(0)                       # 将文件游标移动到文件开头位置
    data3 = json.load(f)
    print(data3, type(data3))
