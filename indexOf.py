x = [1,2,3,4]

find = x.index(3)

print(find)

try : 
	find2 = x.index(43)
except:
	print('didn\'t find')

	print(find2)