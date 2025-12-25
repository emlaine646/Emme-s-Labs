# --------------- Source Code -----------------
"""
My name is Emme and this is assignment LAB 2A.  My program sets two variables, my_id and num_let, to integer values of
20558004 for my_id and five for num_let because the length of my last name "Laine" is five.  The first expression prints
the module of my_id by thirteen which leaves a remainder of twelve.  The second expression adds four to my_id and then modules
that sum by fourteen leaving a remainder of two.  The third expression divides my_id by the sum of num_let added with four.
The fourth expression adds the factorial of num_let.  Finally, the fifth expression takes fourteen thousand divided
by eighty plus the difference my_id subtracted by 123456 divided by the sun of num_let plus twenty squared.
"""
#setting integer values to my two variables
my_id = 20558004
num_let = len("Laine")

#1
print("#1:", my_id%13)
#2
print("#2:", (my_id+4)%14)
#3
print("#3:", my_id/(num_let+4))
#4
print("#4:", 1+2+3+4+num_let)
#5
print("#5:", 14000/(80+((my_id-123456)/(num_let+20)**2)))

# --------------- Run -----------------
"""
C:\Users\lunal\PycharmProjects\PythonProject\.venv\Scripts\python.exe "C:\Users\lunal\PycharmProjects\PythonProject\LAB Assignment 2A - Arithmetic.py" 
#1: 12
#2: 2
#3: 2284222.6666666665
#4: 15
#5: 0.4271512361415053

Process finished with exit code 0
"""