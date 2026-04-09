#Calculation of grade point per course.

import time
import sys


#grade point scale
grade_scale = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "D+": 1.5,
    "D": 1.5,
    "E": 0.5,
    "F": 0.0
    }


global gpas
global was
gpas = []
was = []


#main menu
def main_menu():
    print("Student Grading System")
    print(" 1. Interpret results")
    print(" 2. Quit")

    try:
        user_choice = int(input("\nYour choice: "))

        if user_choice in range(1, 3):
            if user_choice == 1:
                time.sleep(0.5)
                running_menu()
            else:
                quit_app()
        else:
            print("Option not in menu. Try again!\n\n")
            time.sleep(0.8)
            main_menu

    except ValueError:
        print("Invalid input! Kindly select an appropriate option\n\n")
        time.sleep(0.8)
        main_menu()



def running_menu():
    try:
        global year
        global sems

        year = int(input("\nYear/Level: "))

        #convert level in year if user enters level
        if len(str(year)) == 3:
            year = int(str(year)[0])

        #check if year entered falls within range of 1 to 6
        if year not in range(1, 7):
            print("Year must be from 1 to 6! Try again!")
            time.sleep(0.8)
            running_menu()


        max_sems = year * 2 #maximum number of semesters based on year
        sems = int(input("Number of semesters taken so far: "))

        #check if number of semesters exceeds the possible maximum
        if sems > max_sems:
            print(f"Number of semesters taken cannot exceed {max_sems} for Year {year}! Try again")
            time.sleep(0.8)
            running_menu()

    except ValueError:
        print("Value not accepted! Kindly try again.")
        time.sleep(0.8)
        running_menu()

    course_menu(sems)



def course_menu(n):
    sem_count = 1 #semester count
    year_count = 1 #year count

    courses_taken = [0] * n

    print("")

    while sem_count <= n:
        sem_track = 2 if (sem_count%2 == 0) else 1 #keep track of current sem (1/2)

        courses_taken[sem_count - 1] = int(input(f"Number of courses for Year {year_count}, Semester {sem_track}: "))

        sem_count += 1

        #increment the year count after two semester
        if sem_track == 2:
            year_count += 1
    

    sem_count = 1 
    year_count = 1

    for courses in courses_taken:
        global credits
        global grades
        global grade_points

        credits = []
        grades = []
        grade_points = []


        sem_track = 2 if (sem_count%2 == 0) else 1

        print(f"\nDetails for Year {year_count}, Semester {sem_track}")
        while courses > 0:
            grades_menu()
            print("")
            courses -= 1

        sem_count += 1

        if sem_track == 2:
            year_count += 1

        calc_gpa(credits, grade_points)
        calc_wa(credits, grades)

    print("Validating user responses", end="")
    delay()
    print("Processing user data", end="")
    delay(9)
    print("Details successfully captured!")

    grading_system_menu()



#grades menu
def grades_menu(): 
    #course details
    try:
        course_name = input("Course Name: ")
        credit_hours = int(input("Number of credit hours: "))
        course_grade = float(input("Enter results: "))
    except ValueError:
        print("Value not accepted! Kindly try again.")
        time.sleep(0.8)
        course_menu(sems)

    credits.append(credit_hours)

    #convert raw results to grade point
    if course_grade in range(80, 101):
        grade_points.append(grade_scale["A"])
    elif course_grade in range(75, 80):
        grade_points.append(grade_scale["B+"])
    elif course_grade in range(70, 75):
        grade_points.append(grade_scale["B"])
    elif course_grade in range(65, 70):
        grade_points.append(grade_scale["C+"])
    elif course_grade in range(60, 65):
        grade_points.append(grade_scale["C"])
    elif course_grade in range(55, 60):
        grade_points.append(grade_scale["D+"])
    elif course_grade in range(50, 55):
        grade_points.append(grade_scale["D"])
    elif course_grade in range(45, 50):
        grade_points.append(grade_scale["E"])
    else:
        grade_points.append(grade_scale["F"])

    grades.append(course_grade)
    


#menu for grading system type
def grading_system_menu():
    print("\nSelect preferred grading system:")
    print(" 1. Cumulative Grade Point Average (CGPA)")
    print(" 2. Cumulative Weighted Average (CWA)")

    try:
        user_choice = int(input("\nYour choice: "))
        if user_choice == 1:
            calc_cgpa()
            time.sleep(0.8)
            return_menu()
        elif user_choice == 2:
            calc_cwa()
            time.sleep(0.8)
            return_menu()
        else:
            print("Kindly select an option from the menu\n")
            time.sleep(0.5)
            grading_system_menu()
    except ValueError:
        print("Invalid input! Kindly try again.\n")
        time.sleep(0.5)
        grading_system_menu()



#calculate gpa
def calc_gpa(ch, gpp):
    cred_x_grd_pnt = []

    #take credit hour and corresponding grade point
    for c, gp in zip(ch, gpp):
        cred_x_grd_pnt.append(c * gp)

    gpa = sum(cred_x_grd_pnt)/sum(ch)
    gpas.append(gpa)



#calculation of cgpa
def calc_cgpa():
    print("")

    for i, x in enumerate(gpas, start=1):
        time.sleep(0.2)
        print(f"Sem{i} GPA: {x:.2f}")
    
    cgpa = sum(gpas)/len(gpas)
    time.sleep(0.4)
    print(f"Your CGPA is: {cgpa:.2f}")



#calculate wa
def calc_wa(ch, gr):
    global cred_x_weight
    cred_x_weight = []

    for c, w in zip(ch, gr):
        cred_x_weight.append(c * w)

    wa = sum(cred_x_weight)/sum(ch)
    was.append(wa)



#calculation of cwa
def calc_cwa():
    print("")

    for i, x in enumerate(was, start=1):
        time.sleep(0.2)
        print(f"Sem{i} WA: {x:.2f}")
    
    cwa = sum(cred_x_weight)/sum(credits)
    time.sleep(0.4)
    print(f"\NYour CWA is: {cwa:.2f}")



#return menu
def return_menu():
    print("\nReturn to main menu?")
    print(" 1. Yes")
    print(" 2. Quit")

    try:
        user_choice = int(input("\nYour choice: "))

        if user_choice in range(1, 3):
            if user_choice == 1:
                print("\n")
                time.sleep(0.8)
                main_menu()
            else:
                quit()
        else:
            print("\nOption not in menu! Try again.")
            time.sleep(0.3)
            return_menu()
    
    except ValueError:
        print("\nInvalid input! Kindly try again.")
        time.sleep(0.8)
        return_menu()



#quit
def quit_app():
    print("\nQuitting program", end="")
    delay()
    print("Program quit successful!")
    sys.exit()



#delay
def delay(n=6):
    for _ in range(n):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("")
    time.sleep(0.6)



if __name__ == "__main__":
    main_menu()