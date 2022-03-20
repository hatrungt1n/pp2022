class student:
    def __init__(self, _id, _name, _dob):
        self.id = _id
        self.name = _name
        self.dob = _dob

class course:
    def __init__(self, _id, _name):
        self.id = _id
        self.name = _name

class mark(student):
    def __init__(self, _name):
        self.name = _mark

students = []
courses = []
marks = []

# Input number of students in a class
numOfStudents = int(input("How many students are there in a class ? \n"))

# Input student information: id, name, DoB
for i in range(0, numOfStudents):
    print(f"Student {i+1}'s informations: ")
    id = input("Id: ")
    name = input("Name: ")
    dob = input("Dob (format: dd/mm/yy): ")
    students.append(student(id, name, dob).__dict__)

    i += 1

# Input number of courses
numOfCourses = int(input("How many courses are there ? \n"))

# Input course information: id, name
for j in range(0, numOfCourses):
    print(f"Course {j+1}'s informations: ")
    id = input("Id: ")
    name = input("Name: ")
    courses.append(course(id, name).__dict__)

    j += 1

# Select a course, input marks for student in this course
courseSelection = 1
while courseSelection in range(1, numOfCourses + 1):
    courseSelection = int(
        input(
            f"To enter marks for student, select a course (from 1 to {numOfCourses}, type 0 to quit): "
        )
    )

    if courseSelection == 0:
        break

    for i in range(0, numOfStudents):
        print(f"Mark for student {students[i]['name']}: ")
        _mark = int(input())
        marks.append(mark(_mark).__dict__)

        i += 1

    # courses[courseSelection - 1]["marks"] = marks[
    #     (courseSelection - 1) * numOfStudents : courseSelection * numOfStudents
    # ]

print(courses)
print(students)
print(marks)
