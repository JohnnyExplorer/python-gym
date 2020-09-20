
try :
	1/0
except Exception as err :
	print(err.args)
else :
	print('all done')