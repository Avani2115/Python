def f(*args,**kwargs):
    print("Positional: " , args)
    print("Named: " , kwargs)

f(23,45,79,h= 32,y="hello")