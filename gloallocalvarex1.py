#globallocalvarex1.py
lang="Python" # here it is Global Variable
def learnML ():
    sub1="ML" # here it is local variable
    print("\nBy Using'{}'we develop '{}'applications".format(lang,sub1))
def learnDL():
      sub2="DL" # here it is local variable
      print("\nBy Using'{}'we develop '{}'applications".format(lang,sub2))
def learnIOT():
        sub3="IOT" # here it is called local variale
        print("\nBy Using'{}'we develop '{}'applications".format(lang,sub3))
#main prorgram
learnML()
learnDL()
learnIOT()