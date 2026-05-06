# i forgot to import sys for sys.exit sorry
import sys


# variables
total_grade = int()
last_digit = int()
score = int()
extra_credit = int()
sign = None
letter = None


def _calculate_grade(score,extra_credit):

    total_grade = score + extra_credit
    # to total the score...

    # to get the letter of the grade
    if total_grade >= 101: # value too high.
        print("err")
        sys.exit(0)
    elif total_grade == 100:
        letter = 'S'
    elif total_grade >= 80:
        letter = 'A'
    elif total_grade >= 75:
        letter = 'B'
    elif total_grade >= 60:
        letter = 'C'
    elif total_grade >= 50:
        letter = 'D'
    else:
        letter = 'F'
    
    # to get the sign of the grade
    last_digit = total_grade % 10

    if letter == 'F': # first and foremost
        sign = "neutral" # don't be too harsh on the student HAHAHAHA
    elif last_digit >= 7 or total_grade == 100:
        sign = "+"
    elif last_digit <= 3:
        sign = "-"
    else:
        sign = ""
    
    return f"{letter}{sign}"
    

        


# total time: 2hr\
# comments: i did not cry once
# credits to: github.com/gdcolo7 <-- that is me

try:
    print("Total score shouldn't exceed 100.")
    score = int(input("Type in the score/grade: "))
    extra_credit = int(input("Type in the extra credits: ")) 
    if score == 100:
        print("score is 100, no extra credits needed")
        print(100)
        sys.exit(0)
    elif score >= 101:
        print("Score is more than 100?")
        sys.exit(1)
        
    if extra_credit == 100:
        print("Extra credit is 100?")
        sys.exit(1)
    # negative handler

    if score < 0 or extra_credit < 0:
        print("Negative int?")
        sys.exit(1)


except ValueError:
    print("Error: Not an int!")
    sys.exit(1)

except KeyboardInterrupt:
    print("Keyboard interrupt!")
    sys.exit(1)

except ArithmeticError:
    print("Arithmetic Error!")
    print("Achievement got! [How did we get here?]")
    sys.exit(1)


print(_calculate_grade(score,extra_credit))


