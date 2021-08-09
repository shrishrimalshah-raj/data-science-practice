
s1 = 'This is string'
s2 = "This is string"
s3 = """
        This is multiline string
    """

# String Formatting
first_name = 'john'
last_name = 'doe'

# using format() function
print('Hello! I am {} {}'.format(first_name, last_name))

# using numbers inside bracket
print('Hello! I am {0} {1}'.format(first_name, last_name))

# using f-strings
print(f'Hello! I am {first_name} {last_name}')


# String Methods

# 1. capitalize() method
first_name.capitalize()

# 2. lower() method
first_name.lower()

# 3. upper() method
first_name.upper()

# 4. join() method
arr = ["Ram", "Shyam", "Mohan"]
x = "".join(s1)
print(x)

# 5. len() method
x = len(first_name)
print(x)

# 6. count() method
st = "Lionel Messi"
count = st.count('i')
print(count)

# 7. find() method
st = "Lionel Messi"
isFound = st.find('u')
print(isFound)

# 8. islower() method
st = "Lionel Messi"
isLower = st.islower()
print(isLower)

# 9. isupper() method
st = "Lionel Messi"
isLower = st.isupper()
print(isLower)

# 10. split() method
st = "Lionel Messi"
splitList = st.split(' ')
print(splitList)

# 11. strip() method
st = "Lionel Messi"
stripString = st.strip()
print(stripString)
