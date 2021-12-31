#globalkwdex1.py
a=10
b=20  # a and b are global variables
def operation1():
   d=a+b+c # here d is called local variable
   print("sum ={}".format(d))
def operation2():
   d=a-b-c #here d is called local variable
   print("sub={}".format(d))
#main program
c=30 # here c is global variable
operation1()
operation2()