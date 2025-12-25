"""
Emme's LAB Assignment 8- Computer Dating: In this lab we great a class called
Date Profile were we create dating profiles and then compare their "fit numbers" to other
users.  Then, you print each profile, different attributes of the profile, and their fit
score with each user.
"""

#------------------------------Source Code-------------------------------------
class DateProfile:
    MIN_NUMBER = 1
    MAX_NUMBER = 10
    MIN_NAME_LEN = 2
    DEFAULT_GENDER = "F"
    DEFAULT_SEARCH_GENDER = "M"
    DEFAULT_ROMANCE = 5
    DEFAULT_FINANCE = 5
    DEFAULT_DISTANCE = 5
    DEFAULT_NAME = "Jane Doe"

    #__init__ method
    def __init__(self, gender=DEFAULT_GENDER,
                 search_gender=DEFAULT_SEARCH_GENDER,
                 romance=DEFAULT_ROMANCE, finance=DEFAULT_FINANCE,
                 distance=DEFAULT_DISTANCE, name=DEFAULT_NAME):
        self.set_defaults()
        self.set_gender(gender)
        self.set_search_gender(search_gender)
        self.set_romance(romance)
        self.set_finance(finance)
        self.set_distance(distance)
        self.set_name(name)
    #set_all methode
    def set_all(self, gender, search_gender, romance, finance, distance, name):
        self.set_gender(gender)
        self.set_search_gender(search_gender)
        self.set_romance(romance)
        self.set_finance(finance)
        self.set_distance(distance)
        self.set_name(name)
    #restores profile to default values
    def set_defaults(self):
        self.gender = self.DEFAULT_GENDER
        self.search_gender = self.DEFAULT_SEARCH_GENDER
        self.romance = self.DEFAULT_ROMANCE
        self.finance = self.DEFAULT_FINANCE
        self.distance = self.DEFAULT_DISTANCE
        self.name = self.DEFAULT_NAME
    #setters
    def set_gender(self, gender):
        if self.valid_gender(gender):
            self.gender = gender
            return True

    def set_search_gender(self, search_gender):
        if self.valid_gender(search_gender):
            self.search_gender = search_gender
            return True

    def set_romance(self, romance):
        if self.valid_number(romance):
            self.romance = romance
            return True

    def set_finance(self, finance):
        if self.valid_number(finance):
            self.finance = finance
            return True

    def set_distance(self, distance):
        if self.valid_number(distance):
            self.distance = distance
            return True

    def set_name(self, name):
        if self.valid_string(name):
            self.name = name
            return True
    #getters
    def get_gender(self):
        return self.gender

    def get_search_gender(self):
        return self.search_gender

    def get_romance(self):
        return self.romance

    def get_finance(self):
        return self.finance

    def get_distance(self):
        return self.distance

    def get_name(self):
        return self.name
    #helper methods to validate if the string/number/gender inputted is valid
    def valid_gender(self, gender):
        if gender == "M":
            return True
        elif gender == "F":
            return True
        else:
            return False

    def valid_number(self, number):
        if number >= DateProfile.MIN_NUMBER:
            if number <= DateProfile.MAX_NUMBER:
                return True
        return False

    def valid_string(self, string):
        if len(string) >= self.MIN_NAME_LEN:
            return True
        return False
    #fit methods calculate a number between 0 and 1 based on difference between
    #a partner profile
    def determine_gender_fits(self, partner):
        if (self.gender == partner.get_search_gender() and self.search_gender
                == partner.get_gender()):
            return 1.0
        else:
            return 0.0

    def determine_romance_fit(self, partner):
        return round(1.0 - abs(self.romance - partner.romance) / 9, 3)

    def determine_finance_fit(self, partner):
        return round(1.0 - abs(self.finance - partner.finance) / 9, 3)

    def determine_distance_fit(self, partner):
        return round(1.0 - abs(self.distance - partner.distance) / 9, 3)

    def fit_value(self, partner):
        if not self.determine_gender_fits(partner):
            return 0.0
        romance_fit = self.determine_romance_fit(partner)
        distance_fit = self.determine_distance_fit(partner)
        finance_fit = self.determine_finance_fit(partner)
        return round((romance_fit + distance_fit + finance_fit) / 3, 3)

    def __str__(self):
        return self.to_string()

    def to_string(self):
        return (f"Date Profile:\n  {self.name}({self.gender}) searching for "
                f"{self.search_gender}, w/fin={self.finance}, rom={self.romance}, and dist={self.distance}.")


def display_two_profiles(profile_1, profile_2):
    print("Fit between", profile_1.get_name(), "and", profile_2.get_name(), ":",
          profile_1.fit_value(profile_2))


#Make your profiles
profile_1 = DateProfile("F", "F", 7, 4, 10, "Sarah Somebody")
profile_2 = DateProfile("M", "F", 5, 2, 9, "Steve Nobody")
profile_3 = DateProfile("F", "F", 2, 10, 4, "Jane Peabody")
profile_4 = DateProfile("F", "M", 7, 4, 6, "Lilly Nobody")

#create list of profiles to index for each best fit
profiles = [profile_1, profile_2, profile_3, profile_4]
for profile in profiles:
    print(profile.to_string())

for a in profiles:
    print("\n")
    for b in profiles:
        display_two_profiles(a, b)