# Dictionary =====> {} =====> keys and values
a = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# print(a)

# Creating dictionary using dict() method
thisDict = dict(brand="Ford", model="Mustang", year=1960)
# print(thisDict)

# Operations on Dictionary
a.get('brand')
a['brand']
a['brand'] = "Toyota"
a['color'] = "Red"
copyDict = a.copy()
# Loop key, value of Dictionary
a.items()
# Loop keys of Dictionary
a.keys()
# Loop values of Dictionary
a.values()
a.pop('color')
a.popitem()
a.update({"year": 2021})
a.clear()


# *****************************************************************************************
# *****************************************************************************************

# Nested Dictionary =====> {} =====> keys and values
student_marks = {
    'Ram': {
        'Maths': 75,
        'Science': 80,
        'English': 78
    },
    'Shyam': {
        'Maths': 60,
        'Science': 66,
        'English': 70
    },
    'Mohan': {
        'Maths': 65,
        'Science': 75,
        'English': 75
    }
}
# print(student_marks)

# Accessing values in a nested dictionary
student_marks['Mohan']
student_marks['Mohan']['Maths']

student_marks['Rohan'] = {}
student_marks['Rohan']['Maths'] = 80
student_marks['Rohan']['Science'] = 80
student_marks['Rohan']['English'] = 80
student_marks['Rohan']

# Removing item from a nested dictionary
student_marks.pop('Shyam')

# Iterating through a nested dictionary
for name, subjects in student_marks.items():
    print("Name of student", name)
    for marks in subjects:
        print(marks, ":", subjects[marks])
