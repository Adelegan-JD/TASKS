# TASK 2: Unique Name Collector

# Solution
# Step 1: create an empty set
# Step 2: Ask the attendees to input their names, and add it to the set
# Step 3: Sort the set list in an alphabetical order

attendee_list = set()
attendee_list.add(input("Kindly input your name if you attended the programme: "))
attendee_list.add(input("Kindly input your name if you attended the programme: "))
attendee_list.add(input("Kindly input your name if you attended the programme: "))
attendee_list.add(input("Kindly input your name if you attended the programme: "))
print("The names of people who attended the seminar are: ", sorted(attendee_list))

