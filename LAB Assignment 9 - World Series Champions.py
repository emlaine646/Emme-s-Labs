"""
Emme-Lab #9 World Series: In this lab we are given a text file of the year and
what team won the world series in that year.  We read the data and make two
dictionaries, one that saves the years and one that saves the winners.  We then
create a file called WorldSeriesWinnersND.txt that has the binary of the
winners list to make sure there are no duplicate winners.  Finally, in main I
used if statements to get in a valid year from the user and print out the year
and the team that one.
"""

#----------------------------------Source Code----------------------------------
import json

#open the world series winners txt file given
def read_data():
    try:
        with open("WorldSeriesWinnersND.txt", "r") as file:
            winners = [line.strip() for line in file if line != "\n"]
        return winners
    except IOError:
        print("Error: File could not be read.")
        return []

#makes two dictionarys, one of the winners and one of the years
def make_dictionaries(winners):
    yearD = {}
    winsD = {}
    year = 1903
    for winner in winners:
        if year == 1904 or year == 1994:
            year += 1
            continue
        yearD[year] = winner
        if winner in winsD:
            winsD[winner] += 1
        else:
            winsD[winner] = 1
        year += 1
    return yearD, winsD

#makes sure there are no duplicates in winners (using sets)
def no_duplicates(yearD):
    winner_set = set()
    for winner in yearD.values():
        winner_set.add(winner)
    return winner_set
#makes a binary file of the winsD dictionary
def create_file_no_duplicates(winsD):
    try:
        with open("WorldSeriesWinnersND.txt", "wb") as file:
            winsD_byte = bytes(json.dumps(winsD).encode("utf-8"))
            file.write(winsD_byte)
    except IOError:
        print("Error: File could not be written.")
    file.close()


#takes in user imput and makes sure it is valid
def main():
    my_list = read_data()
    yearD, winsD = make_dictionaries(my_list)
    winner_set = no_duplicates(yearD)
    create_file_no_duplicates(winsD)

    while True:
        user_input = input("\nEnter a year in the range 1903-2021: ")
        if not user_input.isdigit():
            print("Only numbers are accepted.")
            continue

        year = int(user_input)
        if year < 1903 or year > 2021:
            print(
                f"The data for the year {year} is not included in our database")
            continue

        if year == 1904 or year == 1994:
            print(f"The World Series was not played in {year}.")
            break
        #prints necessary information
        team = yearD.get(year)
        wins = winsD.get(team, 0)
        print(f"The team that won the world series in", year, "is the", team)
        print(f"They won the world series", wins, "times")
        break

#calls main
if __name__ == '__main__':
    main()
    
    