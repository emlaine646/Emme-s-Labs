"""
Emme's LAB Assignment 7A - Casino with Methods and a Class:
In this lab we built on our previous labs class which creates an object of three strings.  We use this class to create
and object that stores three random strings with the options of BAR, cherries, 7, or space.  We make a function called
rand_string to make these values appear in our gambling actually randomly. The play_1 function prints and formats
the string from rand_string and the users bet from get_bet.  Finally, the main continues until play_1 returns false,
aka when the user inputs 0.
"""
#----------------------------------------------Source Code----------------------------------------------
import random
class MultipleString:
    # constants
    MIN_LEN = 1
    MAX_LEN = 50
    DEFAULT_STRING = "(undefined) "

    # constructor
    def __init__(self, string1=DEFAULT_STRING, string2=DEFAULT_STRING, string3=DEFAULT_STRING):
        # correct values if invalid
        if not self.set_string1(string1):
            self.string1 = MultipleString.DEFAULT_STRING
        if not self.set_string2(string2):
            self.string2 = MultipleString.DEFAULT_STRING
        if not self.set_string3(string3):
            self.string3 = MultipleString.DEFAULT_STRING

    # setters
    def set_string1(self, string1):
        if type(string1) != str:
            return False
        if not self.valid_string(string1):
            return False
        self.string1 = string1
        return True

    def set_string2(self, string2):
        if type(string2) != str:
            return False
        if not self.valid_string(string2):
            return False
        self.string2 = string2
        return True

    def set_string3(self, string3):
        if type(string3) != str:
            return False
        if not self.valid_string(string3):
            return False
        self.string3 = string3
        return True

    # getters
    def get_string1(self):
        return self.string1

    def get_string2(self):
        return self.string2

    def get_string3(self):
        return self.string3

    def to_string(self):
        # combines information from all three values
        return f"Str1: {self.string1} Str2: {self.string2} Str3: {self.string3}"

    def valid_string(self, the_str):
        # validate length of value
        if len(the_str) >= MultipleString.MIN_LEN and len(the_str) <= MultipleString.MAX_LEN:
            return True


MIN_BET = 1
MAX_BET = 50
EXIT_NUM = 0

#functions for gambling
def rand_string():
    #makes a string based on certain percentages
    num = random.randrange(100)
    if num < 45:
        return "BAR"
    elif num < 85:
        return "cherries"
    elif num <90:
        return "space"
    else:
        return "7"

def get_bet():
    #gets a valid bet from the user and blocks out invalid bets (aka not 0 or non ints)
    valid_bet = False
    while not valid_bet:
        bet = input("How much would you like to bet (1 - 50) or 0 to quit?")
        try:
            bet_num = int(bet)
        except ValueError:
            continue
        if bet_num == 0:
            print("Thanks for coming to Casino Laine")
            exit()
        #repromts the user if the bet num is below the min or above the max
        if bet_num < MIN_BET or bet_num > MAX_BET:
            continue
        return bet_num

def pull():
    #assins three random strings based on percentages to MultiString
    MultiStr1 = MultipleString(rand_string(), rand_string(), rand_string())
    return MultiStr1

def get_pay_multiplier(the_pull, the_bet):
    #multiplies the reward amount based on the random string
    string_1 = the_pull.get_string1()
    string_2 = the_pull.get_string2()
    string_3 = the_pull.get_string3()
    string_pull = [string_1, string_2, string_3]
    if string_1 == "cherries" and string_2 != "cherries":
        return the_bet*5
    if string_1 == "cherries" and string_2 == "cherries" and string_3 != "cherries":
        return the_bet*15
    if string_1 == "cherries" and string_2 == "cherries" and string_3 == "cherries":
        return the_bet*30
    if string_1 == "BAR" and string_2 == "BAR" and string_3 == "BAR":
        return the_bet*50
    if string_1 == "7" and string_2 == "7" and string_3 == "7":
        return the_bet*100
    return 0

def play_1(fake_bet = 0, prompt = True):
    #prints all necessary information and makes sure the bet is valid
    if prompt:
        my_bet = get_bet()
    else:
        print("The bet is:", fake_bet)
        my_bet = fake_bet
    print("whirrrrrr .... and your pull is ...")
    my_pull = pull()
    print(my_pull.to_string())
    my_pay = get_pay_multiplier(my_pull, my_bet)
    if my_pay == 0:
        print("sorry, you lose")
    else:
        print("congratulations, you win:", my_pay)
def main():
    #fake_bets = [random.randint(MIN_BET, MAX_BET) for _ in range(100)]
    #print(fake_bets)
    while True:
        play_1()
        #play_1(bet, False)

main()