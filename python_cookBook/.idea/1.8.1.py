#-*- coding:utf-8 -*-
'''
问题：如何实现在字典上对数据执行各式各样的计算（求最小值、最大值、排序等）

'''

price = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

print price
print price.keys()                 #用列表形式取出字典的key
print price.values()              #用列表形式取出字典值
print zip(price.values(),price.keys())        #需要学习zip函数的用法
print min(zip(price.values(),price.keys()))   #最小值
print max(zip(price.values(),price.keys()))   #最大值
price_sorted = sorted(zip(price.values(),price.keys()))  #排序
print price_sorted

def learn_zip():
    a = [1, 3, 4, 5]
    b = [7, 6, 5, 6]
    c = [3, 4, 6, 1]
    d = [1, 2, 3]
    print '*********learn zip***********'
    print 'zip(a,b) result:',zip(a,b)
    print 'zip(a,b,c) result:',zip(a,b,c)
    x = zip(a,b,c)
    print 'zip(*zip(a,b,c)) result:',zip(*x)
    print 'zip(a,d) result:',zip(a,d)
    print '******************************'

learn_zip()