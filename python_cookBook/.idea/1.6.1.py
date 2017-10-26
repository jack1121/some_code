#-*- coding:utf-8 -*-
'''
将字典中的键映射到多个值上问题。其实就是把每个键映射到另一个容器如列表和集合中,list和dict都还比较熟悉，set（集合）有什么不一样，还不懂，需要加以学习。
该例还引用了一个collection模块中的defaultdict类，该类的特性也还不懂，引用的好处也不懂
'''
from collections import defaultdict

d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}

e = {
    'a' : [1, 2, 3],
    'b' : [4,5]
}


f = defaultdict(list)
f['a'].append(1)
f['b'].append(2)
f['c'].append(3)

g = defaultdict(set)
g['a'].add(1)
g['b'].add(2)
g['c'].add(4)

h = {}
h.setdefault('a',[]).append(1)
h.setdefault('b',[]).append(2)
h.setdefault('c',[]).append(4)


print d, "*****", d['a']
print e, "*****", e['a']
print f, "*****", f['a']
print g, "*****", g['a']
print h, "*****", h['a']