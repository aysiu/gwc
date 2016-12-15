# We need to import OrderedDict from the collections module, because dictionaries in Python usually aren't ordered
from collections import OrderedDict

# Create the ordered dictionary that pairs a day of Christmas with the set of gifts for that day
days_gifts=OrderedDict([("12th", "12 Drummers Drumming"),
                        ("11th" , "Eleven Pipers Piping"),
                        ("10th" , "Ten Lords a Leaping"),
                        ("9th" , "Nine Ladies Dancing"),
                        ("8th" , "Eight Maids a Milking"),
                        ("7th" , "Seven Swans a Swimming"),
                        ("6th" , "Six Geese a Laying"),
                        ("5th" , "Five Golden Rings"),
                        ("4th" , "Four Calling Birds"),
                        ("3rd" , "Three French Hens"),
                        ("2nd" , "Two Turtle Doves"),
                        ("1st" , "A partridge in a Pear Tree")])

# Initialize a counter starting at the end of the list
# The length is 12, but we actually want the 11th entry, because it starts counting at 0, not 1.
counter=len(days_gifts)-1

# Loop through each of the days until we get to 0 from 11
while counter >= 0:

    # Get the actual day from the ordered dictionary
    current_day=days_gifts.keys()[counter]

    # Print the intro to the day
    print "On the %s day of Christmas, my true love gave to me:" % (current_day)

    # Set up a second counter, because we do a loop within a loop until we get to the partridge in a pear tree.
    # For now, we'll make the second counter the same as the first
    second_counter=counter

    # The second counter is going to move in the other direction.
    # While the first counter is going from the end of the dictionary to the beginning of the dictionary,
    # the second counter is going from the current place to the end of the dictionary.
    while second_counter < len(days_gifts)-1:

        # Print what gifts are for the second counter
        print "%s," % days_gifts.values()[second_counter]

        # Increase second counter so we get a little closer to the end of the list (the 1st day of Christmas)
        second_counter+=1

    # Print the partridge in a pear tree by itself
    if counter == len(days_gifts)-1:
        print "%s\n" % days_gifts.values()[second_counter]
    else:
        print "and\n%s\n" % days_gifts.values()[second_counter]

    # Decrease first counter to get closer to the beginning of the list (the 12th day of Christmas)
    counter-=1
