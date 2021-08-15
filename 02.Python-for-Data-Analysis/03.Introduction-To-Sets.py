# Sets =====> {} =====> keys and values
s = {
    'apple',
    'banana',
    'cherry'
}

# Accessing elements of set
for i in s:
    print(i)

# Operations on set
s.add('mango')
s.update({'orange', 'watermelon'})
s.remove('orange')
s.discard('orange')
s.pop()
s.clear()

# 1. set union
A = {1, 2, 4, 7, 8}
B = {1, 2, 3, 5, 9, 8}
A | B
A.union(B)
B.union(A)

# 2. set intersection
A & B
A.intersection(B)
B.intersection(A)

# 3. set difference
A-B
A.difference(B)
B.difference(A)

# 4. set symmetric difference
A ^ B
A.symmetric_difference(B)
B.symmetric_difference(A)
