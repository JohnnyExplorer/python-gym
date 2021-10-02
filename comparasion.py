test = (1, 2, 3)              < (1, 2, 4)
print(test)
test = [1, 2, 3]              < [1, 2, 4]
print(test)
test = 'ABC' < 'C' < 'Pascal' < 'Python'
print(test)
test = (1, 2, 3, 4)           < (1, 2, 4)
print(test)
test = (1, 2)                 < (1, 2, -1)
print(test)
test = (1, 2, 3)             == (1.0, 2.0, 3.0)
print(test)
test = (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
print(test)