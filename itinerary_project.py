# project.py - making an itinerary for a user's travel plans with input,
# output, strings, numerical values, conditionals, and loops.

# Purpose:
# Problem - The user has won a free flight to Paris. However, they must pay for everything
# there (except their transportation) on their own.
# Solution: The final itinerary prints out their name, destination, hotel,
# activities for three days, food budget, and total sum of it all.
# How - The user is prompted for their name, hotel from the list with provided prices,
# three activities with provided prices, and a daily food budget that is totaled at the end.
# Everything prints nicely at the end with their full total of how much their trip should
# cost. 

# print_list: This function has one parameter which is meant to be the lists, whether
# it's the pre-made ones or the user-made ones, and prints them out into columns with
# spaces between. It should print them in two columns because of how I set up my lists.
# This function can fail (mess up) if the list given does not have enough items to
# properly format when it prints.

def print_list(the_list):
    print("")
    length = [len(element) for r in the_list for element in r]
    column_width = max(length)
    for r in the_list:
        r = "".join(element.ljust(column_width + 25) for element in r)
        print(r)

# The first and second list contain the the names of hotels/activities and prices within
# their own brackets. The third and fourth list are empty lists for the user to
# add to via their inputs.


hotels_and_prices_list = [["Hotels", "Prices"], ["Walt Le Paris", "$300"],
                          ["Pullman Paris Tour Eiffel", "$250"],
                          ["Hyatt Regency Paris Etoile", "$150"]]

activities_and_prices_list = [["Activities", "Prices"],
                              ["Louvre Museum Tour", "$250"],
                              ["Eiffel Tower Guided Tour", "$200"],
                              ["Mont Daint Michel Trip", "$400"],
                              ["Lido de Paris Cabaret Show", "$150"],
                              ["Normandy D-Day Beaches Tour", "$100"]]

user_total = []

user_activities_list = []

# This text introduces the user to the situatio they're in. They get prompted for their
# name, preferably their full name. Their name prints and they get a print out of the
# hotel and price list in two nice columns. Then they are prompted for their hotel
# choice by entering the first word.

print('''Congratulations! You have won the annual Knightrola Region's Small Monster
Collectors' sweepstakes of a free flight to Paris!
However, you do have to pay for everything else (except transportation).
So let's plan out your 3-day trip!''')

name = input("\nLet's start off by getting to know your full name! ")

print(f"\nHi {name}! Let's pick a hotel for you to stay at!")

print("")
print_list(hotels_and_prices_list)
print("")
user_hotel = input('''Above are a list of hotels for you to choose from. Which would
you like to stay at? Please enter the first word. ''').lower()

# Depending on the user's input, the hotel name will print in the following line
# since it is stored in the variable. The total price will add to the user_total list. 

if user_hotel == "walt":
    user_hotel = "Walt Le Paris"
    user_total.append(3 * 300)
elif user_hotel == "pullman":
    user_hotel = "Pullman Paris Tour Eiffel"
    user_total.append(3 * 250)
elif user_hotel == "hyatt":
    user_hotel = "Hyatt Regency Paris Etoile"
    user_total.append(3 * 150)

# The user's hotel choice prints and then they are introduced to picking activities. 

print("")
print(f"Nice choice going with {user_hotel}!")
print("")
print("Let's pick three fun activities to do while you're there!")
print("")

# In this while loop, the user's activity list is supposed to equal three items. The user
# is prompted for three activities. If they do not enter three, they are prompted for more.
# If they enter more than three, they are asked to drop one. Once there is three,
# the loop ends and it moves on to the next piece of code.

while len(user_activities_list) != 3:
    print_list(activities_and_prices_list)
    if len(user_activities_list) < 3:
        print("")
        activities_to_add = str(input('''What activities would you like to take? Please enter the first
word of each separated by a comma. ''')).split(",")
        print("")
        for activities in activities_to_add:
            activities = activities.strip().capitalize()
            if activities not in user_activities_list:
                user_activities_list.append(activities)
    elif len(user_activities_list) > 3:
        activities_to_drop = str(input("What activities would you like to drop? ")).split(",")
        print("")
        for activities in activities_to_drop:
            print("")
            activities = activities.strip().capitalize()
            if activities in user_activities_list:
                user_activities_list.remove(activities)

# For each first term entered, the first word is dropped and then the full activity
# name is added to the user activity list. The cost of the selected activity is
# added to the user_total list. 

if "Louvre" in user_activities_list:
    user_activities_list.remove("Louvre")
    user_activities_list.append("Louvre Museum Tour")
    user_total.append(250)
if "Eiffel" in user_activities_list:
    user_activities_list.remove("Eiffel")
    user_activities_list.append("Eiffel Tower Guided Tour")
    user_total.append(200)
if "Mont" in user_activities_list:
    user_activities_list.remove("Mont")
    user_activities_list.append("Mont Daint Michel Trip")
    user_total.append(400)
if "Lido" in user_activities_list:
    user_activities_list.remove("Lido")
    user_activities_list.append("Lido de Paris Cabaret Show")
    user_total.append(150)
if "Normandy" in user_activities_list:
    user_activities_list.remove("Normandy")
    user_activities_list.append("Normandy D-Day Beaches Tour")
    user_total.append(100)

# This chunk of code allows the user to create a general food budget. They get prompted
# for their breakfast, lunch, snacks, and dinner budget. They all get added together
# and multiplied by three. This amount is added to the user_total list.

print("")
print("Great! Let's let's plan out a 3-day budget! Please enter a number for each. ")
print("")
print("")
breakfast = int(input("How much would you like to spend on breakfast on average per day? "))
print("")
lunch = int(input("Lunch? "))
print("")
snacks_and_treats = int(input("Snacks and treats? "))
print("")
dinner = int(input("Dinner? "))
print("")
food_total = 3 * (breakfast + lunch + snacks_and_treats + dinner)
user_total.append(food_total)

# The final_list prints the final itinerary by printing the user's name, destination, hotel,
# activities, food budget, transportation, and final total in two columns.

final_list = [["Full Name:", f"{name}"], ["Destination:", "Paris, France"], ["Hotel:", f"{user_hotel}"],
              ["Activities:", f"{user_activities_list[0]}"], ["", f"{user_activities_list[1]}"],
              ["", f"{user_activities_list[2]}"],
              ["Total Food Budget:", f"${food_total}"], ["Transportation:", "Free"], ["", ""],
              ["Total:", f"${sum(user_total)}"]]

print("")
print("Here is your final itinerary!")
print("")
print_list(final_list)
