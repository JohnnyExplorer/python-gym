class Count:
   def __init__(self, count=0):
      self.__count=count

a=Count(2)
b=Count(2)
print(a)
print(b)
print(id(a)==id(b), end = '' '')
#c= ''hello''
#d= ''hello''
#print(id(c)==id(d))