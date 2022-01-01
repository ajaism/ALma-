#globalkwdex3.py
a=10
b=20 # here a,b are called global variable
def modifyvalues():
       global a,b  # referring global variables values a and b
       a=a*2
       b=b+1
       print("value of a in modifyvalues ={}".format(a))
       print("value of b in modifyvalues ={}".format(b))
#main program
print("value of a before modifyvalues ={}".format(a))
print("value of b before modifyvalues ={}".format(b))
modifyvalues()
print("value of a after modifyvalues ={}".format(a))
print("value of a after modifyvalues ={}".format(b))
