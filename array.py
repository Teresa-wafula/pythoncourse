courses = ["MIT", "Cybersecurity", "Datascience"]

# accessing an element in an array
print(courses[1])

# looping through an array
for course in courses:
    print(course)

# adding an element in an array
courses.append("Android development")
print(courses)

# removing an element
courses.remove("MIT")
print(courses)
