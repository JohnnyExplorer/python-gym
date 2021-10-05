## Higher order Functions  in Python


#composition
def f(x):
  return x + 2
def g(h,x):
  return h(x) * 2

print(g(f,42))


#closure
# x is captured and bound when closure is created
# y is free
# look into partial function (func toosl )
##from functools import partial
# A normal function
##def f(a, b, c, x):
    ##return 1000*a + 100*b + 10*c + x
# A partial function that calls f with
# a as 3, b as 1 and c as 4.
##g = partial(f, 3, 1, 4)
# Calling g()
##print(g(5))

def addx(x):
    def _(y):
      return x + y
    return _

add2 = addx(2)
add3 = addx(3)
print (add2(2), add3(3))

# currying
def f(x,y):
  return x*y
def f2(x):
  def _(y):
    return f(x,y)
  return _

print(f2(2))
print(f2(2)(3))


## Pure Functions
## 1 or 3
# do it all func
def get_ints(ints,odd=True,even=True):
  if odd and even:
    return [i for i in ints]
  elif odd:
    return [i for i in ints if i % 2]
  elif even:
    return [i for i in ints if not i % 2]
  else :
    return []

## vs
def get_event_ints(ints):
  return [i for i in ints if not i % 2]

def get_odd_ints(ints):
  return [i for i in ints if i % 2]

def get_all_ints(ints):
  return [i for i in ints]


