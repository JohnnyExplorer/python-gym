
class group():

	def __init__ (self) :
		self.chars = []
		self.len = len(self.chars)
		self.index = 0
	def __iter__(self) :
		return self
	def __next__(self) :
		if(self.index == len(self.chars) ) :
			self.index = 0
			raise StopIteration
		data = self.chars[self.index]
		self.index += 1
		return data
	def addChar(self,char) :
		self.chars.append(char)
		self.len = len(self.chars)
	def getChar(self):
		for char in self.chars :
			yield char



class char() :
	def __init__(self,className):
		self.className = className


char1 = char('rogue')
char2 = char('wizard')
char3 = char('warrior')

group = group()
group.addChar(char1)
group.addChar(char2)
group.addChar(char3)

for char in group :
	print(char.className)

for char in group :
	print(char.className)

for char in group.getChar():
	print(char.className)

for char in group.getChar():
	print(char.className)