# Objective - To practice the use of shorthand if statements
# Task 1 Code Correction
# You are provided with a Python script that is supposed
# to help in event planning, but it has errors. 
# Identify and fix them.

# Buggy Code:
#attendees = input("Enter number of attendees: ")
#venue = "large hall" if attendees > 100 else "conference room"
#print(venue)

### Fixed code ### hashing code to expand for Task 2 and Task 3

#attendees = int(input("Enter number of attendees:"))
#if attendees >= 100:
#    print("Book a large hall")
#else:
#    print("Reserve the conference room")

##### Task 2 Venue Selection ######
# Based on the corrected code from Task 1, further enhance your code 
# to recommend additional things like "audio system" or "projector" 
# based on the number of attendees.

#### Enhanced code #### Hashed as comments to expand in Task 3

#attendees = int(input("Enter number of attendees:"))
#if attendees >= 100:
#    print("Book a large hall. An audio system is also recommended.")
#else:
#    print("Reserve the conference room. A projector is also recommended.")

###### Task 3 Catering Choices #####
# Ask the user if they want "vegetarian" food. 
# Recommend "Veggie Delight Caterers" if yes,
# otherwise recommend "Gourmet Meals Caterers".

attendees = int(input("Enter number of attendees:"))
if attendees >= 100:
    print("Book a large hall. An audio system is also recommended.")
else:
    print("Reserve the conference room. A projector is also recommended.")
meals = input("Do you want vegetarian food? (yes/no):")
if meals == "yes":
    print("We recommend Veggie Delight Caterers.")
else:
    print("We recommend Gourmet Meals Caterers.")