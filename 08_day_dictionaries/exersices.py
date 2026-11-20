
# 1. Create  an empty dictionary called dog
# 2. Add name, color, breed, legs, age to the dog dictionary
# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
# 4. Get the length of the student dictionary
# 5. Get the value of skills and check the data type, it should be a list
# 6. Modify the skills values by adding one or two skills
# 7. Get the dictionary keys as a list
# 8. Get the dictionary values as a list
# 9. Change the dictionary to a list of tuples using _items()_ method
# 10. Delete one of the items in the dictionary
# 11. Delete one of the dictionaries

dct = {}

dct["name"] = "Buddy"
dct["color"] = "Brown"
dct["breed"] = "Labrador"
dct["legs"] = 4
dct["age"] = 5

student = {
  "first_name": "John",
  "last_name": "Doe",
  "gender": "Male",
  "age": 20,
  "marital_status": "Single",
  "skills": ["Python", "JavaScript"],
  "country": "USA",
  "city": "New York",
  "address": "123 Main St"
}

print(len(student))

print(student["skills"])
print(type(student["skills"]))

student["skills"].append("HTML")

print(list(student.keys()))
print(list(student.values()))

student_items = list(student.items())

print(student_items)

del student["marital_status"]

del dct
