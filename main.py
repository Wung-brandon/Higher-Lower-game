import random
from game_data import data
from replit import clear

def format_data(account):
    """format the account data into printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess,a_followers,b_followers):
    """Takes the user guess and followers count and return if the user guess is correct""" 
    if a_followers > b_followers:    
        return guess == "A"     #if guess =="a":
    elif b_followers > a_followers:
        return guess == "B" 
    else:
        print("Incorrect option")
        return      
 
score = 0  
account_b = random.choice(data)
continue_playing = True
#make the game repeatable
while continue_playing: 
    #generate a random account from the game_data
    account_a = account_b
    #make account at position B become the next account at position A
    account_b = random.choice(data)
    
    while account_a == account_b:
        account_b = random.choice(data)
        
    print(f"Compare A: {format_data(account_a)}")
    print("\nVS")
    print(f"\nAgainst B: {format_data(account_b)}")
    #ask user for a guess
    user_guess = input("Who has more followers? Type 'A' or 'B':").upper()

    #check if user is correct
    #get followers count from each account
    a_follower_account = account_a["followers_count"]
    b_follower_account = account_b["followers_count"]
    is_correct = check_answer(user_guess,a_follower_account,b_follower_account)
    #clear screen between rounds
    clear()
    #give user feedback on their guess
    if is_correct:
        #score keeping
        score += 1
        print(f"You got it right! Current Score: {score}")
    else:
        continue_playing = False
        print(f"Sorry, Your wrong Final Score: {score}")
        
    






