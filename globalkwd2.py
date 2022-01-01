#globalkwdex2.py
a=10  # global variable
def  update1():
	print("i am in update1()")
	global a
	a=a+1
	print("Val of a in update1()=",a)
def  update2():
	print("i am in update2()")
	global a
	a=a*2
	print("Val of a in update2()=",a)


#main program
print("Val of a a in main program before updat1()={}".format(a)) # 10
update1()
print("Val of a a in main program after update1()={}".format(a)) # 11     
update2()
print("Val of a a in main program after update2()={}".format(a)) # 22