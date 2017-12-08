#!/usr/bin/python

## Function that checks the input value against a dictionary and then assigns a point for the corresponding house
def tally_response(question, test_dict, score_dict):
	# Temporarily set response to something non-sensical to enter the while loop
	response = None

	# Append an opening parenthesis to the question
	question = question + ' ('

	# Append the options to the question
	for item in test_dict:
		question = question + ' ' + item
	
	# Append a closing parenthesis to the question
	question = question + ' ) '
	
	# Create a while loop that asks for a response until a proper one is given
	while response not in test_dict:
		if response != None:
			print("\nPlease input a response from the choices listed")
		response = raw_input(question).title()
	
	# Find house of response
	house = test_dict[response]
	
	# Add the response's corresponding house to the score dictionary
	score_dict[house] = score_dict[house] + 1

	return house

## Function that determines what house based on the score dictionary. This is a bit tricky, because there are four houses but only three questions. It'd be quite easy for someone to pick a Gryffindor color, a Hufflepuff animal, and a Slytherin trait. One way around this is to value a particular type of question more than another.
def determine_house(score_dict, trait_house):
	# Create a variable to store the highest-scoring house
	contender_house = ''
	
	# Create a variable to store the highest score so far
	contender_score = 0
	
	# Let's loop through the list and see what house scored highest
	for house in score_dict:
		if score_dict[house] > contender_score:
			contender_house = house
			contender_score = score_dict[house]
	
	# Now it's possible that the highest score is just 1 (evenly distributed among three houses). If that's the case, we'll weigh the trait more heavily than the color or animal.
	if contender_score == 1:
		contender_house = trait_house
	return contender_house

## Main function
def main():
	### Initialize a dictionary of scores for each house
	scores = { "Gryffindor": 0, "Hufflepuff": 0, "Ravenclaw": 0, "Slytherin": 0 }

	### Define dictionaries for each type of question

	# Color
	colors = { "Red": "Gryffindor", "Yellow": "Hufflepuff", "Blue": "Ravenclaw", "Green": "Slytherin" }

	# Animal
	animals =  { "Lion": "Gryffindor", "Badger": "Hufflepuff", "Eagle": "Ravenclaw", "Snake": "Slytherin" }

	# Trait
	traits =  { "Bravery": "Gryffindor", "Loyalty": "Hufflepuff", "Wisdom": "Ravenclaw", "Cunning": "Slytherin" }

	### Display a message about what the quiz is
	print "\nThis is a short quiz to determine what Hogwarts house you're best suited for."

	### For color and animal, we're just asking and tallying without needing any value returned
	tally_response("\nWhat color do you prefer?", colors, scores)
	tally_response("\nWhat animal do you most identify with", animals, scores)

	### For the trait, we want to actually record what the trait was, because it may tip the scales if it's a tie all around
	trait_house = tally_response("\nWhat do you value most?", traits, scores)

	### Display what house the sorting hat has sorted the user into
	print "\nThe sorting hat says you'd better be... %s\n" % determine_house(scores, trait_house)

if __name__ == '__main__':
        main()
