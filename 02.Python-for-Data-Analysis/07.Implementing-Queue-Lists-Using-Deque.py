# importing deque
from collections import deque

# initializing
names = deque()

# Adding items to stack
names.append("John")
names.append("Doe")
names.append("Chris")
names.append("Peter")

# Removing last element from stack
names.popleft()
names.popleft()
