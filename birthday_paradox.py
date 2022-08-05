"""
The Birthday Paradox, also called the

Birthday Problem, is the surprisingly high

probability that two people will have the

same birthday even in a small group of people.

In a group of 70 people, there’s a 99.9 percent chance

of two people having a matching birthday. But even

in a group as small as 23 people, there’s a 50 percent

chance of a matching birthday. This program per-

forms several probability experiments to determine

the percentages for groups of different sizes. We call these types of experi-

ments, in which we conduct multiple random trials to understand the

likely outcomes, Monte Carlo experiments.

"""

"""

Birthday Paradox Simulation,

Explore the surprising probabilities of the "Birthday Paradox".

More info at https://en.wikipedia.org/wiki/Birthday_problem

Tags: short, math, simulation

"""
from ast import While
import datetime, random
from urllib import response

#   Function to generate the birthdays
def getBirthdays(numberOfBirthdays):
    """ Returns a list of number random date objects for birthdays """

    birthdays = []

    for i in range (numberOfBirthdays):
        # The year is unimportant for our simulation, as long as all
        # birthdays have the same year.
        startOfYear = datetime.date(2001,1,1)

        #   Get a random day into the year
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    
    return birthdays


#   Function to get matching birthdays
def getMatch(birthdays):
    """ Returns the date object of a date that occurs more than once in birthdays list """
    if len(birthdays) == len(set(birthdays)):
        #   Set() takes one argument, eg a list, and returns a unique list 
        # containing each element appearing only once
        return None #   Since all birthdays will be unique

    #   Compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA    #   Return matching birthday

#   Display the intro
print("""
        Birthday Paradox, by Emmanuel Munyite emunyite@gmail.com
    ----------------------------------------------------------------

The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)

""")

#   Set up a tuple of month names in order
Months = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')

while True: #   Keep asking until the user enters a valid number of birthdays
    print("How many birthdays shall I generate? (Max 100)")
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numDays = int(response)
        break # User has entered a valid amount

print()

#   Generate and display the birthdays
print(f"Here are {numDays} birthdays: ")
birthdays = getBirthdays(numDays)

for i, birthday in enumerate(birthdays):
    if i != 0:
        #   Display a comma for each birthday after the first birthday
        print(', ', end='')
        monthName = Months[birthday.month-1]
        dateText = f"{monthName} {birthday.day}"
        print(dateText,end="")


print()
print()

#   Determine if there are two birthdays that match
match = getMatch(birthdays)

#   Display the results
print("In this simulation, ",end="")

if match != None:
    monthName = Months[match.month-1]
    dateText = f"{monthName} {match.day}"
    print(f"More than one people have a birthday on {dateText}")
else:
    print("There are no matching birthdays")

print()

#   Run through 100,000 simulations
print(f"Generating {numDays} random birthdays 100,000 times...")
input("Press Enter to begin...")


print("Let's run another 100,000 simulations.")
simMatch = 0    #How many simulations had matching birthdays in them

for i in range(100_000):
    #   Report on the progress every 10,000 simulations
    if i % 10_000 == 0:
        print(f"{i} simulations ran...")

    birthday = getBirthdays(numDays)

    if getMatch(birthdays) != None:
        simMatch += 1


print("100,000 simulations run. ")

print()
# Display simulation results:

probability = round(simMatch / 100_000 * 100, 2)

print(f'Out of 100,000 simulations of {numDays} people\'s birthdays, there was a')
print(f'matching birthday in that group {simMatch} times. This means')
print(f'that {numDays} people have a {probability}% chance of')
print('having a matching birthday in their group.\n')


