
def main():

    print("Student Grade Calculator")
    print("-------------------------")

    # ===== Student 1 =====
    name1 = input("Enter student name: ")
    score1a = float(input("Enter exam 1 score: "))
    score1b = float(input("Enter exam 2 score: "))
    score1c = float(input("Enter exam 3 score: "))

    avg1 = (score1a + score1b + score1c) / 3

    if avg1 >= 90:
        grade1 = "A"
    elif avg1 >= 80:
        grade1 = "B"
    elif avg1 >= 70:
        grade1 = "C"
    elif avg1 >= 60:
        grade1 = "D"
    else:
        grade1 = "F"

    if avg1 >= 60:
        status1 = "PASS"
    else:
        status1 = "FAIL"

    print("Report for", name1)
    print("Average:", avg1)
    print("Grade:", grade1)
    print("Status:", status1)
    print()

    # ===== Student 2 =====
    name2 = input("Enter student name: ")
    score2a = float(input("Enter exam 1 score: "))
    score2b = float(input("Enter exam 2 score: "))
    score2c = float(input("Enter exam 3 score: "))

    avg2 = (score2a + score2b + score2c) / 3

    if avg2 >= 90:
        grade2 = "A"
    elif avg2 >= 80:
        grade2 = "B"
    elif avg2 >= 70:
        grade2 = "C"
    elif avg2 >= 60:
        grade2 = "D"
    else:
        grade2 = "F"

    if avg2 >= 60:
        status2 = "PASS"
    else:
        status2 = "FAIL"

    print("Report for", name2)
    print("Average:", avg2)
    print("Grade:", grade2)
    print("Status:", status2)
    print()

    # ===== Student 3 =====
    name3 = input("Enter student name: ")
    score3a = float(input("Enter exam 1 score: "))
    score3b = float(input("Enter exam 2 score: "))
    score3c = float(input("Enter exam 3 score: "))

    avg3 = (score3a + score3b + score3c) / 3

    if avg3 >= 90:
        grade3 = "A"
    elif avg3 >= 80:
        grade3 = "B"
    elif avg3 >= 70:
        grade3 = "C"
    elif avg3 >= 60:
        grade3 = "D"
    else:
        grade3 = "F"

    if avg3 >= 60:
        status3 = "PASS"
    else:
        status3 = "FAIL"

    print("Report for", name3)
    print("Average:", avg3)
    print("Grade:", grade3)
    print("Status:", status3)
    print()

    print("End of program")




if __name__ == '__main__':
    main()
