listOfStudent = []
student_name = ''

while student_name != 'xxx':
    print("Please enter xxx for exit. ")
    student_name = input("Please enter student name: ")
    if student_name != 'xxx':
        grade = input(str("Please enter " + student_name) + "'s grade: ")
        listOfStudent.append([student_name,grade])

print(listOfStudent)