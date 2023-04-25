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


from tkinter import N


def main ():

    question1 = input("Enter the student name:")
    question2 = float(input(("Enter Test score 1:")))
    question3 = float(input("Enter Test score 2:"))
    question4 = float(input("Enter Test score 3:"))
    question5 = float(input("Enter Test score 4:"))
    question6 = float(input("Enter Test score 5:"))

    grade1 = determine_grade (question2)
    grade2 = determine_grade (question3)
    grade3 = determine_grade (question4)
    grade4 = determine_grade (question5)
    grade5 = determine_grade (question6)

    average = calc_average (question2, question3, question4, question5, question6)
    averagegrade = determine_grade (average)


    print ("="*53)
    print ("   ===", "Welcome to Grade and Average Test Scores", "===")
    print ("="*53)
    print ("Student Name:", question1)
    print ('-'*53)

    gap = (' '*5) 
    gap2 = (' '*14)
    gap3 = (' '*5)
    gap4 = (' '*13)
    heading1 = (f"{'Test' :1s} {gap} {'Numeric Grade' :6s} {gap} {'Letter Grade' :1s} {gap2}")

    print (heading1) 
    print (f"{'-'*4} {gap3} {'-'*13} {gap3} {'-'*12} {gap4}")


    print (f" 1{' '*7} {' '} {question2:8,.2f} {' '*15} {grade1}")
    print (f" 2{' '*7} {' '} {question3:8,.2f} {' '*15} {grade2}")
    print (f" 3{' '*7} {' '} {question4:8,.2f} {' '*15} {grade3}")
    print (f" 4{' '*7} {' '} {question5:8,.2f} {' '*15} {grade4}")
    print (f" 5{' '*7} {' '} {question6:8,.2f} {' '*15} {grade5}")

    print ("-"*53)
    print (f"Average:    {average:8.2f}                 {averagegrade}") 
def calc_average(question2, question3, question4, question5, question6):
    average = (question2 + question3 + question4+ question5+ question6) / 5
    return (average)


def determine_grade (total):
    if total>=90:
        grade = "A"
    elif total>=80:
        grade = "B"
    elif total>=70:
        grade= "C"
    elif total>=60:
        grade = "D"
    elif total<=59:
        grade = "F"

    return grade

main()