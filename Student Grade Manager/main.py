print("🎓 Student Grade Manager 🎓")

name = input("\nEnter the student's name: ")
subjectsNum = int(input("Enter the number of subjects student is enrolled in: "))

totalMarks = int(input("Enter the total marks of each subject: "))
overallTotalMarks = subjectsNum*totalMarks

subjects = []
marks = []

for i in range(0, subjectsNum):
    subjects.append(input(f"Enter the name of subject {i+1}: "))
    
    while True:
        mark = int(input(f"Enter the marks obtained in {subjects[i]}: "))
        if mark>=0 and mark<=totalMarks:
            marks.append(mark)
            break
        else:
            print(f"⚠️ Invalid input! Marks must be between 0 and {totalMarks}. Try again.")

totalObtainedMarks = sum(marks)
percentage = (totalObtainedMarks/overallTotalMarks)*100

if percentage > 90:
    grade = 'A+'
elif percentage > 80:  
    grade = 'A'
elif percentage > 70:  
    grade = 'B'
elif percentage > 60: 
    grade = 'C'
elif percentage > 50:  
    grade = 'D'
elif percentage > 40: 
    grade = 'E'
else:                  
    grade = 'F'

print("\n      📊 Result Summary 📊"       )
print(f"Student Name         : {name}")
print( "Subjects             :",subjects)
print( "Marks Obtained       :",marks)
print(f"Total Obtained Marks : {totalObtainedMarks}")
print(f"Total Marks          : {overallTotalMarks}")
print(f"Percentage           : {percentage:.2f}%")
print(f"Grade                : {grade}")