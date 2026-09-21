
def main():
    gpa = float(input('Enter GPA: '))
    credits = int(input('Enter completed credits: '))

# A student qualifies for the honor society if:
#   GPA is at least 3.5
#   AND
#   Credits are at least 30

    if gpa >= 3.5 and credits >= 30:
        print('Qualified')
    else:
        print('Not qualified')

if __name__ == '__main__':
    main()