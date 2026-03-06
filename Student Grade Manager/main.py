# FUNCTIONS:
def printTitle():
    print("🎓 Student Grade Manager 🎓")

def printMenu():
    print("\n1. Add student\n2. View all students\n3. View single student's result\n4. Show high-achievers' result\n5. Show class average\n6. Delete student\n7. Exit")

def getSubjectsNum():
    while True:
        try:
            subjectsNum = int(input("Enter the number of subjects student is enrolled in: "))
            if subjectsNum > 0:
                return subjectsNum
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input, enter a number.")

def getTotalMarks():
    while True:
        try:
            totalMarks = int(input("Enter the total marks of each subject (0-100): "))
            if 0 <= totalMarks <= 100:
                return totalMarks
            else:
                print("Invalid, enter a number from 0-100.")
        except ValueError:
            print("Invalid input, enter a number.")

def getLists(subjectsNum, totalMarks):
    subjects = []
    marks = []

    for i in range(subjectsNum):
        subject_name = input(f"Enter the name of subject {i+1}: ")
        subjects.append(subject_name)

        while True:
            try:
                mark = int(input(f"Enter the marks obtained in {subject_name}: "))
                if 0 <= mark <= totalMarks:
                    marks.append(mark)
                    break
                else:
                    print(f"Marks must be between 0 and {totalMarks}. Try again.")
            except ValueError:
                print("Invalid input, enter a number.")

    return subjects, marks

def findGrade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    elif percentage >= 40:
        return 'E'
    else:
        return 'F'

def printResults(name, subjects, marks, totalObtainedMarks, overallTotalMarks, percentage, grade):
    print("\n      📊 Result Summary 📊"       )
    print(f"Student Name         : {name}")
    print( "Subjects             :",subjects)
    print( "Marks Obtained       :",marks)
    print(f"Total Obtained Marks : {totalObtainedMarks}")
    print(f"Total Marks          : {overallTotalMarks}")
    print(f"Percentage           : {percentage:.2f}%")
    print(f"Grade                : {grade}")

# MAIN PROGRAM:

students = []
totalMarks = None
printTitle()

while(True):
    printMenu()
    while(True):
        try:
            option = int(input("\nEnter your choice (1-7): "))
            if option < 1 or option > 7:
                print("Invalid input, enter from 1-7.")
                continue
            break       
        except ValueError:
            print("Invalid input, enter from 1-7.")
    if option == 1:
        name = input("\nEnter the student's name: ")
        subjectsNum = getSubjectsNum()
        if totalMarks == None:
            totalMarks = getTotalMarks()

        overallTotalMarks = subjectsNum * totalMarks

        subjects, marks = getLists(subjectsNum, totalMarks)

        totalObtainedMarks = sum(marks)
        percentage = (totalObtainedMarks / overallTotalMarks) * 100

        grade = findGrade(percentage)

        student = {
        "name": name,
        "subjects": subjects,
        "marks": marks,
        "total": totalObtainedMarks,
        "percentage": percentage,
        "grade": grade
        }

        students.append(student)
        print("Student added successfully!")
    
    elif option == 2:
        print("\n-------------------------------")
        print("      📋 STUDENTS LIST📋")
        print("-------------------------------\n")
        if len(students) == 0:
            print("No students added yet.")
        else:
            for i, student in enumerate(students, start=1):
                print(f"{i}. {student['name']}")

    elif option == 3:
        printResults(name, subjects, marks, totalObtainedMarks, overallTotalMarks, percentage, grade)

    elif option == 7:
        break