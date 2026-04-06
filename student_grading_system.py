import time
import sys



#main menu
def main_menu():
    print("Student Grading System")
    print(" 1. Interpret results")
    print(" 2. Quit")

    try:
        user_choice = int(input("\nYour choice: "))

        if user_choice in range(1, 3):
            if user_choice == 1:
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

        sem_track = 2 if (sem_count%2 == 0) else 1

        print(f"\nDetails for Year {year_count}, Semester {sem_track}")
        while courses > 0:
            grades_menu()
            print("")
            courses -= 1

        sem_count += 1

        if sem_track == 2:
            year_count += 1



def grades_menu():
    credits = []
    grades = []

    try:
        course_name = input("Course Name: ")
        credit_hours = int(input("Number of credit hours: "))
        course_grade = float(input("Enter results: "))
    except ValueError:
        print("Value not accepted! Kindly try again.")
        time.sleep(0.8)
        course_menu(sems)



def calc_gpa():
    pass



#return menu
def return_menu():
    pass



#quit
def quit_app():
    delay()
    print("Program quit successful!")
    sys.exit()



def delay():
    pass



if __name__ == "__main__":
    main_menu()