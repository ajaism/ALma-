#globalsfunex2.py
a=10
b=20
c=30
d=40   # here 'a' 'b' 'c' and 'd' are called global variables.
def   operation():
	print("--------------------------------")
	kvr=globals()
	for k,v in kvr.items():
		print("\t{}--->{}".format(k,v))
	else:
		print("--------------------------------")
		print("Our program Global Variable Names: dictobj[key]")
		print("--------------------------------")
		print("val of a=",kvr['a'])
		print("val of b=",kvr['b'])
		print("val of c=",kvr['c'])
		print("val of d=",kvr['d'])
		print("--------------------------------")
		print("------------OR-----------------")
		print("Our program Global Variable Names:--get(key)")
		print("--------------------------------")
		print("val of a=",kvr.get('a'))
		print("val of b=",kvr.get('b'))
		print("val of c=",kvr.get('c'))
		print("val of d=",kvr.get('d'))
		print("--------------------------------")
		print("------------OR-----------------")
		print("Our program Global Variable Names:--globls()[global Variable Name]")
		print("--------------------------------")
		print("val of a=",globals()['a'])
		print("val of b=",globals()['b'])
		print("val of c=",globals()['c'])
		print("val of d=",globals()['d'])
		print("--------------------------------")

		

#main program
operation()