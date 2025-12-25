#-----------------------Source Code-----------------------
#Emme's Lab 5B Postal Bar Codes
"""
In this lab I return a barcode depending on a zip code the user entered.  The get_zipcode function requests the zip code
as a string and then repeats this until a valid zipcode was entered.  Next, check_digit returns the check digit of the
function by finding 10 - the modulus 10 of the sum and then takes the modulus 10 of that result.  This returns the
check_digit.  The digit_string function returns the barcode of the check digit.   Finally,  the bar_code_string
function adds two startings and ending "|", creates the barcode and ads the check digit at the end. The main function
calls these previous functions and prints them for the user.
"""
#gets the zipcode from the user
def get_zipcode():
    user_zipcode = input("Enter a 5 digit zip code: ")
    #while the user's zipcode is not at length 5 ask the user for a new zipcode
    while len(user_zipcode) != 5:
        user_zipcode = input("Enter a 5 digit zip code: ")
    return user_zipcode

#function to generate the check digit number
def check_digit(zip_code):
    sum_zipcode = 0
    for i in zip_code:
        sum_zipcode += int(i)
        num_digit  = 0
    check_digit = (10 - (sum_zipcode % 10)) % 10
    return check_digit

#returns the string of the check digit
def digit_string(d):
    if d == 1:
        return ":::||"
    elif d == 2:
        return "::|:|"
    elif d == 3:
        return "::||:"
    elif d == 4:
        return ":|::|"
    elif d == 5:
        return ":|:|:"
    elif d == 6:
        return ":||::"
    elif d == 7:
        return "|:::|"
    elif d == 8:
        return "|::|:"
    elif d == 9:
        return "|:|::"
    elif d == 0:
        return "||:::"
#returns the full barcode with the check digit
def bar_code_string(zipcode):
    barcode = "|"
    for i in range(len(zipcode)):
        digit = int(zipcode[i])
        barcode += digit_string(digit)
    barcode += "|"
    return barcode

#main function that prints out the functions with formatting
def main():
    #gets zipcode
    zip_code = get_zipcode()
    #finds the check digit
    d = check_digit(zip_code)
    print("The check digit is:" , d)
    digit = digit_string(d)
    print("The check digit code is:\n",digit)
    full_zip_code = zip_code + str(d)
    barcode = bar_code_string(full_zip_code)
    print("The encoded zip code is: \n", barcode)

main()
