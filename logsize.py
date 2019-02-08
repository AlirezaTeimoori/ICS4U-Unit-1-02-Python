#---------------------------------------#
#-- Created by:     Alireza Teimoori  --#
#-- Created on:     Feb 8 2019        --#
#-- Created for:    Unit 1-02         --#
#-- Course Code:    ICS4U             --#
#-- Teacher Name:   Chris Atkinson    --#
#---------------------------------------#

# variables:
weight = 0.00
capacity = 1100.00
totalweight = 0

# Asks the user to enter their desired number:
choice = input("Hello,\nPlease enter your number below:  (0.25 or 0.5 or 1) \n")

if choice == 0.25 or 0.5 or 1:
    # the choice must be one of the three numbers above
    print("OK, so your choice is " + str(choice))

    # calculations for this problem
    weight = 20 * float(choice)
    answer = capacity / float(weight)

    # print out the answer
    print("The answer is " + str(answer))

else:
    # Just in case if somebody enters invalid value
    print("WRONG INPUT: The number must be 0.25 or 0.5 or 1")


