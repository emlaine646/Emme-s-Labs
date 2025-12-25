#Emme's LAB Assignment 4B - Payment Calculator
"""
In Lab 4B we are printing a list of information depending on the interest rate and the starting
loan amount.  The user inputs the loan amount and then the number of years (at least 5).  If the
loan amount is equal to 0, the program exists, but if it less than 0 it prompts the user until a
valid value is inputted.  Then, we use an equation to find the monthly payment which is then
printed and used to find the total payment.  I used rounding with f strings to ensure everything
had a consistent decimal place and stopped the program at 8% interest.
"""
#sets variables equal to their corresponding values, specifically the starting and ending interest rate
interest_rate = 0.05
interest_rate_min = 0.05
interest_rate_max = 0.08
interest_increment= 0.00125
INDENT_1 = "         "
INDENT_2 = "           "

#creates a while loop
while True:
    #prompts the user for a loan amount
    loan_amount = int(input("Please enter the loan amount: "))
    #quits program is loan amount is 0
    if loan_amount == 0:
        print("Thanks for using the Payment Calculator!")
        exit()
    #continouly prompts the user for a valid loan amount
    elif loan_amount < 0:
        while loan_amount <0:
            loan_amount = int(input("Please enter the loan amount: "))
            if loan_amount == 0:
                print("Error")
                exit()
    #asks the user for the amount of years
    loan_years = int(input("Please enter the number of years (at least 5): "))
    #while the loan years number is less than five prompts the user for a valid input
    while loan_years < 5:
        loan_years = int(input("Please enter the number of years (at least 5): "))
    #prints menu
    print("Interest Rate    Monthly Payment    Total Paid")
    #prints the interest rate, monthly payment, and total paid between the interest rate min and max
    while interest_rate_min <= interest_rate <= interest_rate_max :
        interest_rate = round(interest_rate, 5)
        #calculates the monthly payment
        monthly_payment = (loan_amount * (interest_rate / 12) / (1 - 1 / (1 + (interest_rate / 12)) ** (loan_years * 12)))
        #finds the total paid
        total_paid = monthly_payment * (loan_years * 12)
        total_paid = round(total_paid, 2)
        #prints the interest, monthly payment, and the total paid for the user
        print("%3.3f%% %s %3.2f %s %3.2f" % (round(float(interest_rate*100.000), 3),INDENT_1,  round(monthly_payment, 2),INDENT_2, total_paid))
        interest_rate = interest_rate + interest_increment

