from functools import cache
@cache
def f(a,b):
    pass

f(a=1,b=2)
f(a=2,b=1) #every 'f' is one object
f(a=2,b=2)
print(f.cache_info().currsize)