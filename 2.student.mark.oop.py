class student:
    def __init__(self, _id, _name, _dob):
        self.id = _id
        self.name = _name
        self.dob = _dob
        # self.students.append(_id, _name, _dob)

class course:
    def __init__(self, _id, _name, _studentList, _marksList):
        self.id = _id
        self.name = _name
        self.studentList = _studentList
        self.marksList = _marksList

class mark():
    def __init__(self, _mark):
        self.mark = _mark

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
    studentsList = students
    courses.append(course(id, name, studentsList).__dict__)

    j += 1
print(courses)
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
    courses.append(course(marks).__dict__)

print(courses)
# print(students)
# print(marks)
