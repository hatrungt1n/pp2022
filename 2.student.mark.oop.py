class student:
    def __init__(self, _id, _name, _dob):
        self.id = _id
        self.name = _name
        self.dob = _dob

    def printStudentsList(self):
        print(
            (self.id).ljust(5, " "),
            (self.name).ljust(15, " "),
            self.dob,
        )

class course:
    def __init__(self, _id, _name, _studentList, _markList):
        self.id = _id
        self.name = _name
        self.studentList = _studentList
        self.markList = _markList

    def printCoursesList(self):
        print((self.id).ljust(5, " "), self.name)

class mark:
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

    for i in range(0, numOfStudents):
        print(f"Mark for student {students[i]['name']}: ")
        _mark = int(input())
        marks.append(mark(_mark).__dict__)

        i += 1

    courses.append(course(id, name, studentsList, marks[j * numOfStudents : (j+1) * numOfStudents]).__dict__)

    j += 1

choices = 1

# Listing functions
while choices < 4:
    choices = int(
        input(
            "If you want to see courses list, please type 1, students list, type 2, student marks, type 3, another number to quit: "
        )
    )

    # List courses
    if choices == 1:
        print("Id".ljust(5, " "), "Name")
        for j in range(0, numOfCourses):
            courses[0].printCoursesList()

    # # List students
    # elif choices == 2:
    #     print("Id".ljust(5, " "), "Name".ljust(15, " "), "Dob")
    #     for i in range(0, numOfStudents):
    #         print(
    #             str(students[i]["id"]).ljust(5, " "),
    #             students[i]["name"].ljust(15, " "),
    #             students[i]["Dob"],
    #         )
    # # Show student marks for a given course
    # elif choices == 3:
    #     for j in range(0, numOfCourses):
    #         print(courses[j]["name"])
    #         print("\tId".ljust(5, " "), "Name".ljust(15, " "), "Mark")
    #         for i in range(0, numOfStudents):
    #             print(
    #                 "\t",
    #                 str(students[i]["id"]).ljust(5, " "),
    #                 students[i]["name"].ljust(15, " "),
    #                 courses[j]["marks"][i][students[i]["name"]],
    #             )
    # else:
    #     break
