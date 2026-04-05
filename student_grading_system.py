#Preferred grading system
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
    pass



def calc_gpa():
    pass



#return menu
def return_menu():
    pass



#quit
def quit_app():
    print("Program quit successful!")
    sys.exit()



def delay():
    pass



if __name__ == "__main__":
    main_menu()