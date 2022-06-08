"""Restaurant rating lister."""


# put your code here

def process_scores():
    """Read scores file and return dictionary of {restaurant-name: score}"""

    scores_txt = open('scores.txt') #scores.text is our text file with restaurants/scores

    scores = {}

    for line in scores_txt:
        line = line.rstrip()
        #Python rstrip() method removes all the trailing characters from the string.
        restaurant, score = line.split(":")
        #The .split() method in Python returns a list of the words in the string/line , separated by the delimiter string. This method will return one or more new strings. All substrings are returned in the list datatype.
        
        scores[restaurant] = int(score)

    return scores

def add_restaurant(scores):
    """add a restaurant and rating."""

    print("please add a rating for your favorite restaurant")
    restaurant = input("Restaurant name> ")
    rating = int(input("rating> "))

    scores[restaurant] = rating

def print_sorted_scores(scores):
    """print restaurants and ratings, sorted."""

    for restaurant, rating in sorted(scores.items()):
        print(f"{restaurant} is rated at {rating}.")

#read existing scores in from file
scores = process_scores()

#allow user to add a restaurant/rating pair
add_restaurant(scores)

#print an alphabetical list of all rated restaurants and their ratings
print_sorted_scores(scores)
