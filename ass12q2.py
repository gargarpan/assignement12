'''
l=[1,2,3]
print(l[3])
'''
#Erroe :IndexError: list index out of range

#Handled
l=[1,2,3]
try:
    print(l[3])
except:
    print("list index out of range")
