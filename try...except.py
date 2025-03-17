from sys import exception
x=56
try:
    print(x)# this attempts to print x
except NameError:# this catches only "undefined variable" errors
    print("Variable is not defined")
else:# this prints "It's all good" after x is printed
     print("It's all good") #

x1=900
try:
   if type(x1) is not float:
    raise TypeError("THE ERROR")
except TypeError as e1:
    print(f"their is {e1}")
