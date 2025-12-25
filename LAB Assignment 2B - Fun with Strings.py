"""
Foothill College CS 2B
Professor Jesse Ci
Lab 2A Fun with Strings
Emmeline Laine

Summary: Create four variables with the values of my first and last names, the length of my last name, and my age.
I then print out my variables with the strings of my first and last names and then printed my age.  Next I
printed the 2nd index of my last name (corresponds to the third letter).  Finally,I made one sentence with three
different uses of the \
"""
# --------------- Source Code -----------------
first_name = "Emme"
last_name = "Laine"
len_last = len(last_name)
my_age = 16

print("My first name is: ", first_name)
print("My last name is: ", last_name)
print("My age is: ", str(my_age))
length = len(last_name)
print(last_name[2])
print(last_name.upper())
print("I printed \"  on the first line \n"
      + "and \\ on the second line")

# --------------- Run -----------------
"""
C:\Users\lunal\PycharmProjects\PythonProject\.venv\Scripts\python.exe "C:\Users\lunal\PycharmProjects\PythonProject\LAB Assignment 2B - Fun with Strings.py" 
My first name is:  Emme
My last name is:  Laine
My age is:  16
i
LAINE
I printed "  on the first line 
and \ on the second line

Process finished with exit code 0
"""