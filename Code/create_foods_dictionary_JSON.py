import sys
import json

def make_food_pairs_dictionary(file_name):
    food_pairs_file = open(file_name)                                  						# opening the file containing the food pairs
        
    food_pairs = {}                                             							# initialize an empty dictionary

    for line in food_pairs_file:	# for each line in the sentiment file
        food1, food2, similarity = line.replace("_", " ").replace("\n", "").split(",", 3)	# split it into foods and similarity components
        food_pairs.setdefault(food1, set()).add((food2,similarity))							# add each food as a key
        food_pairs.setdefault(food2, set()).add((food1,similarity))							#	with value the set of food-score pairs
        
    return food_pairs																		# return the dictionary
    
def main():        
    foods = make_food_pairs_dictionary(sys.argv[1])        									# make dictionary of food pairs with scores
    
    with open('foods_dictionary.json', 'w') as f: 
        f.write(json.dumps(foods))															# save the dictionary in a file in JSON format

if __name__ == '__main__':
    main()    
