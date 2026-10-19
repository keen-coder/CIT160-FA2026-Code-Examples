def main():
    print("Student Grade Calculator")
    print("-------------------------")

    name = input("Enter student name: ")
    s1 = get_score()
    s2 = get_score()
    s3 = get_score()

    avg = average(s1, s2, s3)

    letter = letter_grade(avg)

    status = ''

    if is_passing(avg):
        status = "PASS"
    else:
        status = "FAIL"

    print_report(name, avg, letter, status)
    
def get_score():
    while ( ( (score := float(input("Enter an exam score: "))) < 0) ):
        print('ERROR: Negative Score')

    return score

def average(score1, score2, score3):
    avg = (score1 + score2 + score3) / 3
    return avg

def letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

def is_passing(average):
    # if average >= 60:
    #     return True
    # else:
    #     return False

    return average >= 60

def print_report(name, avg, grade, status):
    print("Report for", name)
    print("Average:", avg)
    print("Grade:", grade)
    print("Status:", status)
    print()

if __name__ == '__main__':
    main()