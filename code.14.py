def subject_grade(mark):
    if mark == "Absent":
        return "NA"
    mark = int(mark)
    if mark <= 39: return "F"
    elif mark <= 44: return "P"
    elif mark <= 49: return "C"
    elif mark <= 54: return "B"
    elif mark <= 59: return "B+"
    elif mark <= 69: return "A"
    elif mark <= 79: return "A+"
    elif mark <= 100: return "O"
    return "Invalid"

def evaluate_student(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    failed = m1 <= 39 or m2 <= 39 or m3 <= 39
    result = "Fail" if failed else "Pass"
    grades = [subject_grade(m) for m in (m1, m2, m3)]
    print(f"Total: {total}, Average: {average:.2f}, Result: {result}, Grades: {grades}")
