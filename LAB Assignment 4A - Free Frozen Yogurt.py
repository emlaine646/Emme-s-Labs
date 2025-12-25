#-----------------------------Source Code-----------------------------
"""Emme's Lab 4A:
In this code I prompt a user to enter in choices to tally the amount of stamps collected when buying frozen yogurt.  I
first check if the total amount of stamps is greater or equal to 12.  If the user types P or a string starting with P
the transaction will start.If it is, I ask the user if they would like a free frozen yogurt.  If they do it is applied,
and they loose 12 stamps from the total.  If no, the user then inputs the amount of frozen yogurt they want to buy.
This also happens when the user doesn't have 12 or more stamps. They gain one stamp to their total per yogurt bought.
It then prints out how many stamps they gained and the total amount of stamps before repeating the transaction.  If
the user types a string starting with upper or lowercase S the while loop stops and the code ends.  You CANNOT type in
strings when asked for a number or this code will error.
"""
#define local and global variables
total_stamps = 0
user_stamps = 0
STAMPS_FOR_FREE = 12
PURCHASE = "P"
SHUTDOWN = "S"
YES = "Y"
NO = "N"
INDENT1= "        "

#define a while loop that is true until the user inputs a string starting with S
while True:
    #prints menu
    print("Menu: " + "\n"
    + "P (process purchase) \n"
    + "S (Shut down)")
    #takes user input, only P and S values should be accepted
    user_choice = input("Your choice: ")
    #takes the first index of a string to isolate if the string starts with P or S
    user_choice = user_choice[0]
    #if the strings first index is P, will assume the user will buy yogurt
    if user_choice.upper() == PURCHASE:
        #if the total from previous iterations is above 12, will prompt the user to use a free yogurt for 12 stamps
        if total_stamps >= STAMPS_FOR_FREE:
            user_stamp_choice = input("You qualify for a free yogurt. Would you like to use your credits? (Y or N): ")
            #takes the first index of the input
            user_stamp_choice = user_stamp_choice [0]
            if user_stamp_choice.upper() == YES:
                #if the user wants to use their stamps for a free yogurt will subtract 12 from the total
                total_stamps = total_stamps - STAMPS_FOR_FREE
                print("You bought a yogurt, you have ", str(total_stamps), "stamps left.")
                print(INDENT1)
                continue
            #if the input is invalid continue
            elif user_stamp_choice.upper() != NO:
                print("Invalid input. Please try again.")
                print(INDENT1)
                continue
        #prompts the user for the amount of yogurt they want to buy, if the value is invalid repeats the loop
        user_stamps = int(input("How many yogurts would you like to buy ?: "))
        if user_stamps <=0:
            print(" *** Invalid # yogurts. ***")
            continue
        #if the input is valid adds the amount inputted to the total
        else:
            total_stamps = total_stamps + user_stamps
            print("You earned", user_stamps, "and you now have", total_stamps)
            print(INDENT1)
    #if the first index is S, program will shut down
    elif user_choice.upper() == str(SHUTDOWN):
        print("Shutting down, thank you for shopping!")
        break
    #if the index of a string does not equal S or P, the while loop will repeat
    else:
        print(" *** Use P or S, please. ***")
        print(INDENT1)
