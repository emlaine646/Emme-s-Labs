#Pizza Nutrition Calculator
"""
Emmeline Laine Lab3A: Make a nutritional calculator were you input the number of grams for each pizza topping, and you get the
output of the total calories, fat, fiber, and protein for a single serving of your pizza.  The code stops if you have a
serving number below 1 or above 11 OR if you input a gram amount below 0 and above 1100 grams.  The code has an if
statement that if the user doesn't follow these limits will stop the code.
"""

#Ingriedient 1
topping_1 = "marinara sauce"
topping_1_cal_P100G = 51
topping_1_fat_P100G = 1.5
topping_1_fiber_P100G = 1.8
topping_1_protein_P100G = 1.4

#Ingriedient 2
topping_2 = "cheese"
topping_2_cal_P100G = 402
topping_2_fat_P100G = 33
topping_2_fiber_P100G = 0
topping_2_protein_P100G = 25

#Ingriedient 3
topping_3 = "pepperoni"
topping_3_cal_P100G = 494
topping_3_fat_P100G = 44
topping_3_fiber_P100G = 0
topping_3_protein_P100G = 23

#Ingriedient 4
topping_4 = "mushrooms"
topping_4_cal_P100G = 22
topping_4_fat_P100G = 0.3
topping_4_fiber_P100G = 1
topping_4_protein_P100G = 3.1

#Ingriedient 5
topping_5 = "artichokes"
topping_5_cal_P100G = 47
topping_5_fat_P100G = 0.2
topping_5_fiber_P100G = 5
topping_5_protein_P100G = 3.3

#List of Supplies
print("Here are the list of pizza toppings to choose from: \n"
      + "1. marinara sauce \n"
      + "2. cheese \n"
      + "3. pepperoni \n"
      + "4. mushrooms \n"
      + "5. artichokes")
total_cals = 0.
total_fat = 0.
total_fiber = 0.
total_protein = 0.

recipe_name = input("What is the name of your recipe?: ")
serving_num = int(input("How many servings of " + recipe_name + " between 1 and 11 are you making?: "))

if serving_num <1 or serving_num > 11:
    print("Please enter a number between 1 and 11")
    exit()

# food #1 ---------------------------------------------------------
user_input_int = int(input("How many grams of " + topping_1 + "?: "))
if user_input_int < 0 or user_input_int > 1100:
    print("Error please select a number between 1 and 1100")
    exit()

# Update nutritional constants
total_cals += user_input_int * (topping_1_cal_P100G/ 100.)
total_fat += user_input_int * (topping_1_fat_P100G / 100.)
total_fiber += user_input_int * (topping_1_fiber_P100G / 100.)
total_protein += user_input_int * (topping_1_protein_P100G / 100.)

# food #2 ---------------------------------------------------------
user_input_int = int(input("How many grams of " + topping_2 + "? "))
if user_input_int < 0 or user_input_int > 1100:
    print("Error please select a number between 1 and 1100")
    exit()

# Update nutritional constants
total_cals += user_input_int * (topping_2_cal_P100G/ 100.)
total_fat += user_input_int * (topping_2_fat_P100G / 100.)
total_fiber += user_input_int * (topping_2_fiber_P100G / 100.)
total_protein += user_input_int * (topping_2_protein_P100G / 100.)

# food #3 ---------------------------------------------------------
user_input_int = int(input("How many grams of " + topping_3 + "? "))
if user_input_int < 0 or user_input_int > 1100:
    print("Error please select a number between 1 and 1100")
    exit()

# Update nutritional constants
total_cals += user_input_int * (topping_3_cal_P100G/ 100.)
total_fat += user_input_int * (topping_3_fat_P100G / 100.)
total_fiber += user_input_int * (topping_3_fiber_P100G / 100.)
total_protein += user_input_int * (topping_3_protein_P100G / 100.)

# food #4 ---------------------------------------------------------
user_input_int = int(input("How many grams of " + topping_4 + "? "))
if user_input_int < 0 or user_input_int > 1100:
    print("Error please select a number between 1 and 1100")
    exit()

# Update nutritional constants
total_cals += user_input_int * (topping_4_cal_P100G/ 100.)
total_fat += user_input_int * (topping_4_fat_P100G / 100.)
total_fiber += user_input_int * (topping_4_fiber_P100G / 100.)
total_protein += user_input_int * (topping_4_protein_P100G / 100.)

# food #5 ---------------------------------------------------------
user_input_int = int(input("How many grams of " + topping_5 + "? "))
if user_input_int < 0 or user_input_int > 1100:
    print("Error please select a number between 1 and 1100")
    exit()

# Update nutritional constants
total_cals += (user_input_int * (topping_5_cal_P100G/ 100.))
total_fat += (user_input_int * (topping_5_fat_P100G / 100.))
total_fiber += (user_input_int * (topping_5_fiber_P100G / 100.))
total_protein += (user_input_int * (topping_5_protein_P100G / 100.))


#divide the total calories by the serving number
total_cals = total_cals/serving_num
total_fat = total_fat/serving_num
total_fiber = total_fiber/serving_num
total_protein = total_protein/serving_num


#Results
print( "\n ------- Nutrition for your custom " + recipe_name + "-------" )
print("Total Calories: " + str(total_cals) + "\n"
      + "Total Fat: " + str(total_fat) + "\n"
      + "Total Fiber: " + str(total_fiber) + "\n"
      + "Total Protein: " + str(total_protein) + "\n")


"""
--------------Run--------------
C:\Users\lunal\PycharmProjects\PythonProject\.venv\Scripts\python.exe "C:\Users\lunal\PycharmProjects\PythonProject\LAB Assignment 3A - Recipe-to-Nutrition Converter.py" 
Here are the list of pizza toppings to choose from: 
1. marinara sauce 
2. cheese 
3. pepperoni 
4. mushrooms 
5. artichokes
What is the name of your recipe?: Emme's Pizza
How many servings of Emme's Pizza between 1 and 11 are you making?: 5
How many grams of marinara sauce?: 100
How many grams of cheese? 100
How many grams of pepperoni? 100
How many grams of mushrooms? 100
How many grams of artichokes? 100

 ------- Nutrition for your custom Emme's Pizza-------
Total Calories: 203.2
Total Fat: 15.8
Total Fiber: 1.56
Total Protein: 11.16


Process finished with exit code 0
"""