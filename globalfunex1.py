#globalsfunex1.py
a=10
b=20
c=30
d=40   # here a,b,c,d are global variables
def operation():
    print("-------------------------------------")
    global c,d
    c=c+1  #31
    d=d+1  #41
    a=100
    b=200 # here a and b  are called  local variables
    e=a+b+c+d # just print a,b(local value)c,d()local
    print("result=",e)
    print("----------------------------OR----------------")
    e=a+b+c+d+globals().get('a')+globals().get('b')
    print("result",e)
    print("result=",e)
    print("-------------------------OR------------------")
    x=globals() # here x is of type <class,'dict'>
    e=a+b+c+d+x.get('a')+x.get('b')
    print("result=",e)
    print("--------------------OR----------------")
    e=a+b+c+d+x['a']+x['b']
    print("result=",e)
#main program
operation()