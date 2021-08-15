# List =====> [] =====> Lists are mutable (changeable)
a = ['apple', 'banana', 'cherry']
a[1]
print(a)

# Operations on List
a.append('mango')
# Add 0 index item
a.insert(0, 'orange')
a.remove('orange')
a.pop()
# Remove 0 index item
a.pop(0)
copyList = a.copy()
a.clear()
a.reverse()
a.count('apple')
a.extend([3, 8])
a.sort()

# *****************************************************************************************
# *****************************************************************************************

# Tuple =====> () =====> Tuples are Immutable (not changeable)
b = (4, 8, 10, 12)
b[1]
print(b)
# Operations on Tuple
b.count(4)
b.index(12)
len(b)
# Using + operator to join tuples
u1 = (2, 5, 7, 9)
u2 = (1, 2, 5, 6)
u1+u2
