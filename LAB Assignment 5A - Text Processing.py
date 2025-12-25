#--------------------------Code--------------------------
string_min = 6
string_max = 500
new_character = "*"

def get_key_character():
    user_key = input("Please enter a SINGLE character to act as key: ")
    while len(user_key) != 1:
        user_key = input("Please enter a SINGLE character to act as key: ")
    return user_key

def get_string():
    user_string = input("Please enter a single phrase or sentence >= " + str(string_min) + " and <= " + str(string_max) + " characters: ")
    while len(user_string) < string_min or len(user_string) > string_max:
        user_string = input("Please enter a single phrase or sentence >= " + str(string_min) + " and <= " + str(string_max) + " characters: ")
    return user_string

def mask_character(user_key, user_string):
    masked_string = ""
    count = 0
    for i in user_string:
        if i == user_key:
            masked_string += new_character
            count += 1
        else:
            masked_string += i
    return masked_string, count

def replace_character(user_key, user_string):
    replaced_string = ""
    count = 0
    for i in user_string:
        if i != user_key:
            replaced_string += i
        else:
            count += 1
    return replaced_string, count

def main():
    user_key = get_key_character()
    user_string = get_string()

    masked_string, masked_count = mask_character(user_key, user_string)
    replaced_string, replaced_count = replace_character(user_key, user_string)

    print("\n--------------------------------------")
    print("String with key character, '" + user_key + "', masked:")
    print(masked_string + "\n")
    print("String with '" + user_key + "' removed:")
    print(replaced_string + "\n")
    print("# of occurrences of key character, '" + user_key + "': " + str(masked_count))
    print("--------------------------------------")

main()
