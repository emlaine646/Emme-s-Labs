#-------------------Source Code-------------------
"""
Emmeline Laine's LAB 3B: In this code I examine three different phone plans and evaluate the best plan depending
on the user's number of minutes per month.  After a certain number of minutes, plan A and B will charge a rate for
every additional minute past the threshold used.  This does not apply to package C because it has a flat rate.
It will print the number of additional minutes, the cost for the additional minutes, the total cost, and the overall
cost comparison with the other two un-chosen packages.
"""
import sys

# Package A intended constants
PAC_A_NAME = "A"
PAC_A_COST = 39.99
PAC_A_MINUTES = 450
PAC_A_ADDITIONAL_MIN = 0.45

# Package B intended constants
PAC_B_NAME = "B"
PAC_B_COST = 59.99
PAC_B_MINUTES = 900
PAC_B_ADDITIONAL_MIN = 0.40

# Package C intended constants
PAC_C_NAME = "C"
PAC_C_COST = 69.99
PAC_C_MINUTES = 1000000  # 1 million will simulate unlimited
PAC_C_ADDITIONAL_MIN = 0

INDENT1 = "   "             # first line of package
INDENT2 = "              "  # other parts of the package

# initialize accumulator variables
user_min = 0.
total_cost = 0

#impliment symbolic parameters
max_min = 9999
min_min = 0


#print the package options
print(INDENT2)
print("---------- List of Packages ---------")
print(INDENT1 + "Package A: " + "$" + str(PAC_A_COST) + "\n"
      + INDENT2 + str(PAC_A_MINUTES) + " minutes \n"
      + INDENT2 + "$" + str(PAC_A_ADDITIONAL_MIN) + " per additional minute")
print(INDENT2)

print(INDENT1 + "Package B: " + "$"+ str(PAC_B_COST) + "\n"
      + INDENT2 + str(PAC_B_MINUTES) + " minutes\n"
      + INDENT2 + "$" + str(PAC_B_ADDITIONAL_MIN) + " per additional minute")
print(INDENT2)

print(INDENT1 + "Package C: " + "$" + str(PAC_C_COST) + "\n"
      + INDENT2 + str(PAC_C_MINUTES) + " minutes\n"
      + INDENT2 + "$" + str(PAC_C_ADDITIONAL_MIN) + " per additional minute")
print(INDENT2)

#Prompts the user for their type of package
user_pac = input("What package would you like?:")
if user_pac.upper() != PAC_A_NAME.upper():
    if user_pac.upper() != PAC_B_NAME.upper():
        if user_pac.upper() != PAC_C_NAME.upper():
            print("Please input a valid package.")
            exit()

#Prints base cost for chosen package
if user_pac == PAC_A_NAME.upper():
    print("Cost for base package: " + "$" + str(PAC_A_COST))
if user_pac == PAC_B_NAME.upper():
    print("Cost for base package: " + "$" + str(PAC_B_COST))
if user_pac == PAC_C_NAME.upper():
    print("Cost for base package: " + "$" + str(PAC_C_COST))

#Errors out code if the user input is less than 0 or greater than 9999
user_min = int(input("How many minutes did you use?: "))
if user_min <=min_min or user_min>=max_min:
    print("Please input a valid number.")
    exit()



#calculates the total cost if the user picked package A
if user_min>=PAC_A_MINUTES and user_pac == PAC_A_NAME.upper():
    total_cost = PAC_A_COST + (user_min-PAC_A_MINUTES)*PAC_A_ADDITIONAL_MIN
    print("Additional minutes used: ", user_min-PAC_A_MINUTES)
    print("The additional minute cost $", (user_min-PAC_A_MINUTES)*PAC_A_ADDITIONAL_MIN)
    print("Your total cost is: $", total_cost)
elif user_min <= PAC_A_MINUTES:
    total_cost = PAC_A_COST
    print("Your total cost is: $", PAC_A_COST)

#calculates the total cost if the user picked package B
if user_min>=PAC_B_MINUTES and user_pac == PAC_B_NAME.upper():
    total_cost = PAC_B_COST + (user_min-PAC_B_MINUTES)*PAC_B_ADDITIONAL_MIN
    print("Additional minutes used: ", user_min-PAC_B_MINUTES)
    print("The additional minute cost $", (user_min-PAC_B_MINUTES)*PAC_B_ADDITIONAL_MIN)
    print("Your total cost is: $", total_cost)
elif user_min <= PAC_B_MINUTES:
    total_cost = PAC_B_COST
    print("Your total cost is: $", PAC_B_COST)

#calculates the total cost if the user picked package C
if user_pac == PAC_C_NAME.upper():
    total_cost = PAC_C_COST
    print("Your total cost is: $", PAC_C_COST)

print(INDENT2)

#Prints the total cost for the amount of minutes for each package
print("Analysis:")

if user_pac != PAC_A_NAME.upper():
    if user_min>=PAC_A_MINUTES:
        total_cost = PAC_A_COST + (user_min - PAC_A_MINUTES) * PAC_A_ADDITIONAL_MIN
        print("Package A: $", total_cost)
    else:
        print("Package A: $", PAC_A_COST)

if user_pac != PAC_B_NAME.upper():
    if user_min>=PAC_B_MINUTES:
        total_cost = PAC_B_COST + (user_min - PAC_B_MINUTES) * PAC_B_ADDITIONAL_MIN
        print("Package B: $", total_cost)
    else:
        print("Package B: $", PAC_B_COST)

if user_pac != PAC_C_NAME.upper():
    if user_min>=PAC_C_MINUTES:
        total_cost = PAC_C_COST + (user_min - PAC_C_MINUTES) * PAC_C_ADDITIONAL_MIN
        print("Package C: $", total_cost)
    else:
        print("Package C: $", PAC_C_COST)

