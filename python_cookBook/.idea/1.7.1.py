#-*- coding:utf-8 -*-
'''
问题：创建一个字典，同时对字典做迭代或序列化操作时，也能控制其中元素的顺序。即实现让字典保持有序
解决方案是：使用collectiongs中的OrderedDict类
'''
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key,d[key])

print d
