str = "this is a string that will make something to do"
bigword = ''

for word in str.split():
	if len(bigword) < len(word):
		bigword = word
print(bigword,len(bigword))