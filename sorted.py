l = [34,234,12,1312]
print (l)
lsorted =sorted(l)
print (lsorted)

import operator
l2 = {
'test1': 4,
'test2': 3,
'test3': 2,
'test4': 1,
}
print(l2)
l2sortedkey = sorted(l2.items(),key=operator.itemgetter(0))
print(l2sortedkey)
l2sortedatt = sorted(l2.items(),key=operator.itemgetter(1))
print(l2sortedatt)