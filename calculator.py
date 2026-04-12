import time

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



#convert results to grade point
def get_grade_point(course_grade):
    if course_grade in range(80, 101):
        return grade_scale["A"]
    elif course_grade in range(75, 80):
        return grade_scale["B+"]
    elif course_grade in range(70, 75):
        return grade_scale["B"]
    elif course_grade in range(65, 70):
        return grade_scale["C+"]
    elif course_grade in range(60, 65):
        return grade_scale["C"]
    elif course_grade in range(55, 60):
        return grade_scale["D+"]
    elif course_grade in range(50, 55):
        return grade_scale["D"]
    elif course_grade in range(45, 50):
        return grade_scale["E"]
    else:
        return grade_scale["F"]


def calc_gpa(credits, grade_points):
    weighted = sum(c * gp for c, gp in zip(credits, grade_points))
    return weighted / sum(credits)


def calc_wa(credits, grades):
    weighted = sum(c * g for c, g in zip(credits, grades))
    return weighted / sum(credits)


def calc_cgpa(gpas):
    print("")
    for i, gpa in enumerate(gpas, start=1):
        time.sleep(0.2)
        print(f"Sem{i} GPA: {gpa:.2f}")

    cgpa = sum(gpas) / len(gpas)
    time.sleep(0.4)
    print(f"Your CGPA is: {cgpa:.2f}")


def calc_cwa(was):
    print("")
    for i, wa in enumerate(was, start=1):
        time.sleep(0.2)
        print(f"Sem{i} WA: {wa:.2f}")

    cwa = sum(was) / len(was)
    time.sleep(0.4)
    print(f"\nYour CWA is: {cwa:.2f}")