######################################################################################################


'''
# is and is not are the identity operators in Python.
# They are used to check if two values (or variables) are located on the same part of the memory.
# Two variables that are equal does not imply that they are identical.


# is operator
x = ["apple", "banana"]
# print(id(x))
y = ["apple", "banana"]
# print(id(y))
z = x

# print(x is z)
# returns True because z is the same object as x

# print(x is y)
# returns False because x is not the same object as y, even if they have the same content

# print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
'''



d=[1,1,1]
k=[1,1,1]
# print(id(d))
# print(id(k))
# print(d is k)

# d=k
# print(id(d))
# print(id(k))
# print(k is d)



x1 = 5
y1 = 5

print(id(x1))
print(id(y1))
# print(x1 is not y1)

print(x1 is y1)    # same memory location


'''
x2 = 'Hello'
y2 = 'Hello'
# Output: True
# print(id(x2))
# print(id(y2))
# print(x2 is y2)    # same memory location


x3 = [1,2,3]
y3 = [1,2,3]
# Output: False
# print(id(x3))
# print(id(y3))
# print(x3 is y3)   # Not same memory location

# print(x3 is not y3)


x4 = (1,2,3)
y4 = (1,2,3)
# Output: True
# print(id(x4))
# print(id(y4))
# print(x4 is y4)
'''
##############################################################################################