
#FUNCTIONS
#1
#Complete the body of the following function according to its docstring.

def round_to_two_places(num):
     resultado= round(num, 2)
     return resultado

print(round_to_two_places(3.14159))

#2
#The help for round says that ndigits 
#(the second argument) may be negative. What do you think will happen when it is? Try some examples in the following cell.
def redondeo ( numero,ndigits):
    
    resultado = round(numero,ndigits)
    return resultado

numero = 3.14159
ndigits = -5

resultado = redondeo(numero,ndigits)
print( "el redondeo" , numero, "es" , resultado)

#3
#In the previous exercise, the candy-sharing friends Alice, Bob and Carol tried to split candies evenly. For the sake of their friendship, any candies left over would be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
# Below is a simple function that will calculate the number of candies to smash for any number of total candies.
# Modify it so that it optionally takes a second argument representing the number of friends the candies are being split between. If no second argument is provided, it should assume 3 friends, as before.
#Update the docstring to reflect this new behaviour.

def to_smash(total_candies,friends=3):
    """escribir en ingles que realiza esta funcion"""
    result= total_candies 
    return result % friends

final_result= to_smash(91,89)
print(final_result)


#Booleans and Conditionals
#1
#In the cell below, 
#define a function called sign which takes a numerical argument and returns -1 if it's negative, 
# 1 if it's positive, and 0 if it's 0.

def sign(number):
    if number > 0:
        return 1 
    if number < 0: 
        return -1
    else: 
        return 0

print(sign(10))

#2
#We've decided to add "logging" to our to_smash function from the previous exercise.

def to_smash(total_candies):
    if total_candies >= 1:
        print("Splitting", total_candies, "candies")
    else: total_candies = 1
    print("Splitting", total_candies, "candy")
    return total_candies % 3

to_smash(91)
to_smash(1)

#3. 🌶️
#In the tutorial, we talked about deciding whether we're prepared for the weather. I said that I'm safe from today's weather if...
# I have an umbrella...or if the rain isn't too heavy and I have a hood...
# otherwise, I'm still fine unless it's raining and it's a workday

# The function below uses our first attempt at turning this logic into a Python expression. I claimed that there was a bug in that code. Can you find it?
# To prove that prepared_for_weather is buggy, come up with a set of inputs where either:
#   the function returns False (but should have returned True), or
#   the function returned True (but should have returned False).

def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):

    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False


actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

#4.
#The function is_negative below is implemented correctly - it returns True if the given number is negative and False otherwise

def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return concise_is_negative and (number < 0) 

#5a.
#The boolean variables ketchup, mustard and onion represent whether a customer wants a particular topping on their hot dog.
#We want to implement a number of boolean functions that correspond to some yes-or-no questions about the customer's order. 

#Return whether the customer doesn't want onions.
def onionless(ketchup, mustard, onion):
    return not onion 

ketchup= True
mustard= True
onion= False
print(onionless(ketchup,mustard,onion))


#Return whether the customer wants "the works" (all 3 toppings)
def wants_all_toppings(ketchup, mustard, onion):

    return ketchup and mustard and onion


ketchup= True
mustard= True
onion=True
print( wants_all_toppings(ketchup, mustard, onion))

#5b.
# Return whether the customer wants a plain hot dog with no toppings.
def wants_plain_hotdog(ketchup, mustard, onion):
    return not (ketchup or mustard or onion)

ketchup= False
mustard= False
onion=False
print( wants_plain_hotdog(ketchup, mustard, onion))


#5c
#Return whether the customer wants either ketchup or mustard, but not both.(You may be familiar with this operation under the name "exclusive or")
  
def exactly_one_sauce(ketchup, mustard, onion):
    return (ketchup and not mustard) or (mustard and not ketchup)

#6
# Return whether the customer wants exactly one of the three available toppings on their hot dog.

def exactly_one_topping(ketchup, mustard, onion):
    return (ketchup + mustard + onion) == 1

print(exactly_one_topping(False,True,False))

#7
#In this problem we'll be working with a simplified version of blackjack (aka twenty-one). In this version there is one player (who you'll control) and a dealer. Play proceeds as follows:

#Return True if the player should hit (request another card) given the current game
# state, or False if the player should stay.
# When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
# doesn't bring the total above 21, otherwise we count them as low (with value 1). 
# For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
# and therefore set player_total=20, player_low_aces=2, player_high_aces=1.

def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    if player_total <= 11:
        return True
    elif player_total == 12 and dealer_total >= 4 and dealer_total <= 6:
        return False
    elif player_total <= 16 and dealer_total >= 7:
        return True
    elif player_total <= 17 and dealer_total <= 6:
        return True
    elif player_total == 18:
        if dealer_total >= 9:
            return True
        elif dealer_total <= 6 and player_high_aces > 0:
            return True
        else:
            return False
    else:
        return False
    
dealer_total = 5
player_total = 14
player_low_aces = 0
player_high_aces = 1

decision = should_hit(dealer_total, player_total, player_low_aces, player_high_aces)
print("Decision:", decision)

#List
#1
# You are analyzing sports teams. Members of each team are stored in a list. The Coach is the first name in the list, the captain is the second name in the list, and other players are listed after that. These lists are stored in another list, which starts with the best team and 
#proceeds through the list to the worst team last. Complete the function below to select the captain of the worst team.

def losing_team_captain(teams):
        if len(teams) > 0:
            last_team= teams [-1]
            if len(last_team) >= 2:
                return last_team[1]
            return None
        
result=losing_team_captain(teams)
print(result)

#2
#We're using lists to record people who attended our party and what order they arrived in. For example, the following list represents a party with 7 guests, in which Adela showed up first and Ford was the last to arrive:

#party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']

#A guest is considered 'fashionably late' if they arrived after at least half of the party's guests. However, they must not be the very last guest (that's taking it too far).
#In the above example, Mona and Gilbert are the only guests who were fashionably late.

def fashionably_late(arrivals, name):
    total_guests = len(arrivals)
    arrival_index = arrivals.index(name)
    return arrival_index >= total_guests / 2 and arrival_index != total_guests - 1


arrivals = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
print(fashionably_late(arrivals, 'Mona'))  
print(fashionably_late(arrivals, 'Gilbert'))  
print(fashionably_late(arrivals, 'Ford'))  


#Loops

#1



#Given a list of meals served over some period of time, return True if the
# same meal has ever been served two days in a row, and False otherwise.

def menu_is_boring(meals):

    for i in range(len(meals) - 1):
        if meals[i] == meals[i+1]:
            return True
    return False

q3.check()
print(menu_is_boring(['Spaghetti', 'Salad', 'Salad', 'Pizza']))  
print(menu_is_boring(['Chicken', 'Beef', 'Fish', 'Tofu']))  
print(menu_is_boring(['Soup', 'Soup', 'Soup', 'Soup']))  


#Next to the Blackjack table, the Python Challenge Casino has a slot machine. 
# You can get a result from the slot machine by calling play_slot_machine(). 
# The number it returns is your winnings in dollars. Usually it returns 0. 
# But sometimes you'll get lucky and get a big payday. 


def estimate_average_slot_payout(n_runs):
    payouts = [play_slot_machine()-1 for i in range(n_runs)]
    avg_payout = sum(payouts) / n_runs
    return avg_payout

avg_payout = estimate_average_slot_payout(10000000)
print("Average net profit per run:", avg_payout)

#Strings and Dictionaries

#1
#A researcher has gathered thousands of news articles. But she wants to focus her attention on articles including a specific word. 
#Complete the function below to help her filter her list of articles.

#Your function should meet the following criteria:
#Do not include documents where the keyword string shows up only as a part of a larger word. For example, if she were looking for the keyword “closed”, you would not include the string “enclosed.”
#She does not want you to distinguish upper case from lower case letters. So the phrase “Closed the case.” would be included when the keyword is “closed”
#Do not let periods or commas affect what is matched. “It is closed.” would be included when the keyword is “closed”.
#  But you can assume there are no other types of punctuation.


def word_search(doc_list, keyword):
    indices = [] 
    for i, doc in enumerate(doc_list):
        tokens = doc.split()
        normalized = [token.rstrip('.,').lower() for token in tokens]
        if keyword.lower() in normalized:
            indices.append(i)
    return indices

#2
#.Now the researcher wants to supply multiple keywords to search for.

def multi_word_search(documents, keywords):
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(documents, keyword)
    return keyword_to_indices

documents = ["The quick brown fox", "jumps over the lazy dog", "The brown cat"]
keywords = ["brown", "fox", "cat"]

result = multi_word_search(documents, keywords)
print(result)


documents = ["The quick brown fox", "jumps over the lazy dog", "The brown cat"]
search_keyword = "brown"

result = word_search(documents, search_keyword)
print("Indices where the keyword appears:", result)