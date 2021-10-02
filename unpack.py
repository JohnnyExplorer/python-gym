

def unpack(one,two,three):
	print('one',one)
	print('two',two)
	print('three',three)



test = [1,2,3]

unpack(*test)

test2 = {1:'one',2:"two",3:"three"}

print(test2)

unpack(*test2.values())
