"""
Emme's Lab 6B - A Multiple String Class
In this lab we make a class called Multiple String that takes in three strings and returns false if these string's len
is less than 1 and greater than 50 (also if the main calls the class and has a string have a value besides a string).
My valid_String does this, and if the values of the string is invalid the __init__ function resets the string.  
My main function prints the required displayed objects and mutate the object to test the set and get methods.
"""


# ---------------- SOURCE ----------------------------------------
class MultipleString:
    """ encapsulates a 3-string object """

    # intended class constants ------------------------------------
    MAX_LEN = 50
    MIN_LEN = 1
    DEFAULT_STRING = "(undefined)"


    # constructor method ------------------------------------
    def __init__(self, string1=DEFAULT_STRING, string2=DEFAULT_STRING, string3=DEFAULT_STRING):
        if not self.set_string1(string1):
            self._string1 = MultipleString.DEFAULT_STRING
        if not self.set_string2(string2):
            self._string2 = MultipleString.DEFAULT_STRING
        if not self.set_string3(string3):
            self._string3 = MultipleString.DEFAULT_STRING

    def to_string(self):
        return f"{self._string1} {self._string2} {self._string3}"


    # mutator ("set") methods -------------------------------
    def get_string1(self):
        return self._string1
    def get_string2(self):
        return self._string2
    def get_string3(self):
        return self._string3

    # accessor ("get") methods -------------------------------
    def set_string1(self, the_str):
        if not self.valid_string(the_str):
            return False
        else:
            self._string1 = the_str
            return True
    def set_string2(self, the_str):
        if not self.valid_string(the_str):
            return False
        else:
            self._string2 = the_str
            return True
    def set_string3(self, the_str):
        if not self.valid_string(the_str):
            return False
        else:
            self._string3 = the_str
            return True


    # helper methods for entire class -----------------
    def valid_string(self, the_str):
        if type(the_str) != str:
            return False
        if len(the_str) >= MultipleString.MAX_LEN or len(the_str) <= MultipleString.MIN_LEN:
            return False
        else:
            return True



# ------------- CLIENT --------------------------------------------------

def main():
    #Instantiate four or more MutilpleString objects, some of them using the default values, some using arguments.
    test_string1 = MultipleString()
    test_string2 = MultipleString("emme", "is", "cool")
    test_string3 = MultipleString("emme", "is", 16)
    test_string4 = MultipleString("", "Toby", "cute                                                                ")
    #Immediately display all objects.
    print("-------------Construct and Print Initial Objects-----------------")
    print(test_string1.to_string())
    print(test_string2.to_string())
    print(test_string3.to_string())
    print(test_string4.to_string())
    #Mutate one or more members of every object.
    test_string1.set_string1("Toby")
    test_string1.set_string2("is")
    test_string1.set_string3("cute")
    test_string2.set_string3("amazing")
    test_string3.set_string3("sixteen")
    test_string4.set_string1("My cat")
    test_string4.set_string3("cute")
    print("-------------Print all Objects-----------------")
    #Display all objects a second time.
    print(test_string1.to_string())
    print(test_string2.to_string())
    print(test_string3.to_string())
    print(test_string4.to_string())
    #Do two explicit mutator tests. For each, call a mutator in an if/else statement which prints one message if the
    # call is successful and a different message if the call fails.
    print("-------------Test Set String-----------------")
    if test_string4.set_string3("is adorable"):
        print("The input was valid.")
    else:
        print("The input was invalid.")
    if test_string1.set_string1(100):
        print("The input was valid.")
    else:
        print("The input was invalid.")
    #Make two accessor calls to demonstrate that they work.
    print("---------------Reprint Tested String---------------")
    print(test_string4.to_string())
    print(test_string1.to_string())


main()
