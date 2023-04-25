######################################################################
#  
# Assignment:    Assignment_1B 
# 
# Program Name:  AM_Assignment1B.py 
# 
# Purpose:       The purpose of this program is to demonstrate the  
#                process of creating a Python script and executing 
#                it. This program creates a table where different 
#                grades are displayed
# 
# Author:        Garry Daly 
# 
# Course:        CIS109.950
# 
# Created:       August 30, 2022 
# 
######################################################################





import turtle

def main():

    name = turtle.textinput ('Input', 'Enter the student name')
    score1 = turtle.numinput ('Input', 'Enter Test Score 1', default=0, minval=0, maxval=100.00)
    score2 = turtle.numinput ('Input', 'Enter Test Score 2', default=0, minval=0, maxval=100.00)
    score3 = turtle.numinput ('Input', 'Enter Test Score 3', default=0, minval=0, maxval=100.00)
    score4 = turtle.numinput ('Input', 'Enter Test Score 4', default=0, minval=0, maxval=100.00)
    score5 = turtle.numinput ('Input', 'Enter Test Score 5', default=0, minval=0, maxval=100.00)

    grade1 = determine_grade (score1)
    grade2 = determine_grade (score2)
    grade3 = determine_grade (score3)
    grade4 = determine_grade (score4)
    grade5 = determine_grade (score5)
 
#Beginning with the Table headings

    print ("="*53)
    print ("   ===", "Welcome to Grade and Average Test Scores", "===")
    print ("="*53)
    print (f'Student Name:{ name}')
    print ('-'*53)

    gap = (' '*5) 
    gap2 = (' '*14)
    gap3 = (' '*5)
    gap4 = (' '*13)
    heading1 = (f"{'Test' :1s} {gap} {'Numeric Grade' :6s} {gap} {'Letter Grade' :1s} {gap2}")

    print (heading1)
    print (f"{'-'*4} {gap3} {'-'*13} {gap3} {'-'*12} {gap4}")

    print (f" 1{' '*7} {' '} {score1:8,.2f} {' '*15} {grade1}")
    print (f" 2{' '*7} {' '} {score2:8,.2f} {' '*15} {grade2}")
    print (f" 3{' '*7} {' '} {score3:8,.2f} {' '*15} {grade3}")
    print (f" 4{' '*7} {' '} {score4:8,.2f} {' '*15} {grade4}")
    print (f" 5{' '*7} {' '} {score5:8,.2f} {' '*15} {grade5}")

    print ("="*53)
        
    testaverage = calc_average(score1, score2, score3, score4, score5)
    avggrade = determine_grade(testaverage)
    print(f'Average:{" "*6} {testaverage} {" "*15} {avggrade} {" "*15}')

    return

def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3+ score4+ score5) / 5
    return (average)

def determine_grade(total):
    if total>=90:
        return "A"
    elif total>=80:
        return "B"
    elif total>=70:
        return "C"
    elif total>=60:
        return "D"
    elif total<=59:
        return "F"

main ()   

 
