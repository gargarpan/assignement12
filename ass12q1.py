'''
a=3
if a<4:
    a=a/(a-3)
    print(a)
'''
# Error : ZeroDivisionError: division by zero

#Handled
a=3
try:
    if a<4:
        a=a/(a-3)
except ZeroDivisionError:
    print("Division By Zero Exception")
