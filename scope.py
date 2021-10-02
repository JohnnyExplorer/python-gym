
def scope1(arg) :
	print('inside scope 1', arg)
	print('inside scope 1 changed', arg)
def scope2(dictArg) :
	print('inside scope 2', dictArg)
	dictArg['new'] = 'test'
	print('inside scope 2 changed', dictArg)

x = 1
print('outside',x)
scope1(x)
print('after outside',x)


dictArg = {'test':'test'}
print('outside 2',dictArg)
scope2(dictArg)
print('after outside 2', dictArg)


def scope3() :
	local = 'local'
	local2 = 'local2'
	print('local',local)
	print('local2',local2)

	def scope4():
		nonlocal local
		local = 'local mod'
		local2 = 'local2 mod'
		print('local inside',local)
		print('local2 inside',local2)

	scope4()
	print('local outside',local)
	print('local2 outside',local2)

scope3()