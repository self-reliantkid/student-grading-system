import time
import sys

from calculator import calc_gpa, calc_wa, calc_cgpa, calc_cwa, get_grade_point
from converter import cgpa_to_cwa, cwa_to_gpa
from utils import delay, view_records
from storage import save_records, load_records



data = load_records()


def check_for_records():
    if data:
        records_menu()
    else:
        main_menu()



def records_menu():
    print("Saved records found")
    print(" 1. Continue with saved data")
    print(" 2. Start fresh")

    try:
        user_choice = int(input("\nYour choice: "))

        if user_choice not in range(1, 3):
            print("Option not in menu! Kindly try again.\n\n")
            time.sleep(0.8)
            records_menu()
        else:
            if user_choice == 2:
                global data
                data = {}
        time.sleep(0.8)
        print("\n")    
        main_menu()

    except ValueError:
        print("Invalid input! Try again!\n\n")
        time.sleep(0.6)
        records_menu()



def main_menu():
    print("Student Grading System")
    print(" 1. Add Semester Results")
    print(" 2. Convert CGPA/GPA")
    print(" 3. View Records")
    print(" 4. Exit")

    try:
        user_choice = int(input("\nYour choice: "))

        if user_choice in range(1, 5):
            if user_choice == 1:
                time.sleep(0.5)
                running_menu()
            elif user_choice == 2:
                time.sleep(0.5)
                convert_menu()
            elif user_choice == 3:
                if data:
                    time.sleep(0.8)
                    view_records(data)
                    time.sleep(1)
                    return_menu()
                else:
                    print("There are currently no viewable records!")
                    time.sleep(0.8)
            else:
                quit_app()
        else:
            print("Option not in menu. Try again!\n\n")
            time.sleep(0.8)
            main_menu()

    except ValueError:
        print("Invalid input! Kindly select an appropriate option\n\n")
        time.sleep(0.8)
        main_menu()



def running_menu():
    print("\nSelect preferred grading system:")
    print(" 1. Cumulative Grade Point Average (CGPA)")
    print(" 2. Cumulative Weighted Average (CWA)")

    try:
        user_choice = int(input("\nYour choice: "))
        time.sleep(0.8)
    except ValueError:
        print("Invalid input! Kindly try again.\n")
        time.sleep(0.5)
        running_menu


    try:
        year = int(input("\nYear/Level: "))

        if len(str(year)) == 3:
            year = int(str(year)[0])

        if year not in range(1, 7):
            print("Year must be from 1 to 6! Try again!")
            time.sleep(0.8)
            running_menu()
            return

        max_sems = year * 2
        sems = int(input("Number of semesters taken so far: "))

        if sems > max_sems:
            print(f"Number of semesters taken cannot exceed {max_sems} for Year {year}! Try again")
            time.sleep(0.8)
            running_menu()
            return

    except ValueError:
        print("Value not accepted! Kindly try again.")
        time.sleep(0.8)
        running_menu()
        return

    course_menu(year, sems, user_choice)



def course_menu(year, n, sys_choice):
    sem_count = 1
    year_count = 1

    courses_taken = [0] * n

    print("")

    while sem_count <= n:
        sem_track = 2 if (sem_count % 2 == 0) else 1
        courses_taken[sem_count - 1] = int(input(f"Number of courses for Year {year_count}, Semester {sem_track}: "))
        sem_count += 1

        if sem_track == 2:
            year_count += 1

    sem_count = 1
    year_count = 1

    gpas = []
    was = []

    for courses in courses_taken:
        sem_track = 2 if (sem_count % 2 == 0) else 1

        print(f"\nDetails for Year {year_count}, Semester {sem_track}")

        credits = []
        grades = []
        grade_points = []

        courses_list = []

        for _ in range(courses):
            name, c, g, gp = grades_menu()
            credits.append(c)
            grades.append(g)
            grade_points.append(gp)

            courses_list.append({"name": name, "credits": c, "grades": g})
            print("")

        data.setdefault(f"year_{year_count}", {})[f"sem_{sem_track}"] = courses_list 

        sem_count += 1
        if sem_track == 2:
            year_count += 1

        gpas.append(calc_gpa(credits, grade_points))
        was.append(calc_wa(credits, grades))

    print("Validating user responses", end="")
    delay(5)
    print("Processing user data", end="")
    delay(10)
    print("Details successfully captured!")

    grading_system_menu(gpas, was, sys_choice)



def grades_menu():
    try:
        course_name = input("Course Name: ")
        credit_hours = int(input("Number of credit hours: "))
        course_grade = float(input("Enter results: "))
    except ValueError:
        print("Value not accepted! Kindly try again.")
        time.sleep(0.8)
        return grades_menu()

    grade_point = get_grade_point(course_grade)
    return course_name, credit_hours, course_grade, grade_point



def grading_system_menu(gpas, was, choice):
    try:
        if choice == 1:
            calc_cgpa(gpas)
            time.sleep(0.8)
            return_menu()
        elif choice == 2:
            calc_cwa(was)
            time.sleep(0.8)
            return_menu()
        else:
            print("Kindly select an option from the menu\n")
            time.sleep(0.5)
            grading_system_menu(gpas, was)
    except ValueError:
        print("Invalid input! Kindly try again.\n")
        time.sleep(0.5)
        grading_system_menu(gpas, was)



def return_menu():
    print("\nReturn to main menu?")
    print(" 1. Yes")
    print(" 2. Save and Return")
    print(" 3. Save and Exit")

    try:
        user_choice = int(input("\nYour choice: "))
        if user_choice in range(1, 3):
            if user_choice == 1:
                print("\n")
                time.sleep(0.8)
                main_menu()
            elif user_choice == 2:
                save_records(data)
                print("\n")
                time.sleep(0.8)
                main_menu()
            else:
                save_records(data)
                quit_app()
        else:
            print("\nOption not in menu! Try again.")
            time.sleep(0.3)
            return_menu()
    except ValueError:
        print("\nInvalid input! Kindly try again.")
        time.sleep(0.8)
        return_menu()



def convert_menu():
    print("\nGrade Conversion")
    print(" 1. CGPA to CWA")
    print(" 2. CWA to CGPA")

    try:
        user_choice = int(input("\nYour choice: "))
        if user_choice in range(1, 4):
            if user_choice == 1:
                cgpa_to_cwa()
            else:
                cwa_to_gpa()
            time.sleep(0.8)
            return_menu()
        else:
            print("Option not in menu. Try again!")
            time.sleep(0.5)
            convert_menu()
    except ValueError:
        print("Invalid input! Kindly try again.")
        time.sleep(0.8)
        convert_menu()



def quit_app():
    print("\nQuitting program", end="")
    delay()
    print("Program quit successful!")
    sys.exit()



if __name__ == "__main__":
    check_for_records()