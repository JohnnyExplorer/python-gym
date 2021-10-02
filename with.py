class test:
	def __init__ (self,args) :
		print('init', args)

	def __enter__(self):
		print('enter')
	def __exit__(self, exc_type, exc_value, traceback):
		print('exit')



test = test('hello')

with test as t :
	pass
print('done')