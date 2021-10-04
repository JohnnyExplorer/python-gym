def f(x):
  return x + 2
def g(h,x):
  return h(x) * 2

print(g(f,42))