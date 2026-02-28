# FUNCTIONS:
def printTitle():
    print("🎓 Student Grade Manager 🎓")

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
printTitle()

name = input("\nEnter the student's name: ")
subjectsNum = getSubjectsNum()
totalMarks = getTotalMarks()

overallTotalMarks = subjectsNum * totalMarks

subjects, marks = getLists(subjectsNum, totalMarks)

totalObtainedMarks = sum(marks)
percentage = (totalObtainedMarks / overallTotalMarks) * 100

grade = findGrade(percentage)

printResults(name, subjects, marks, totalObtainedMarks, overallTotalMarks, percentage, grade)