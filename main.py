import random
ph=random.randint(1,12)
dh=random.randint(1,20)
hit=random.randint(1,12)
hitph=hit+ph
money=10
bet=0
invalid=True
fg=True #variable for things I only want displayed on the first game
    
print("Welcome to the 21 game. Your goal is to have a bigger hand than the dealer while not exceding 21. You lose when you have no money left.")

while money>0:
    while invalid==True:
        if fg==True:
            a=input(f"Your hand is {ph}. How much would you like to bet? You can bet up to $100 more than what you have. Your current balence is ${money}.\n")
            fg=False
        else:
            a=input(f"Your hand is {ph}. How much would you like to bet? Your current balence is ${money}.\n")
        if int(a) <= money+100:
            bet=int(a)
            invalid=False
        else:
            print("You cannot bet more than $100 that you have")
            
    win=money+bet
    loss=money-bet
    a=input("Would you like to hit or stand?\n")
    if "hit" in a:
        print(f"You draw a {str(hit)}.\nYour new hand is {hitph}.\n\nDealer's hand:{dh}")
        if hitph>21 or hitph<dh:
            print("Dealer wins.")
            money=loss
        elif hitph>dh:
            print("You win!")
            money=win
        else:
            print("Draw.")
    elif "stand" in a:
        print(f"Dealer's hand:{dh}")
        if ph<dh:
            print("Dealer wins.")
            money=loss
        elif ph>dh:
            print("You win!")
            money=win
        else:
            print("draw")
    invalid=True
    if money > 0:
        print(f"\n You have ${money}.\nAnd another game begins.\n")
    else:
        print(f"You have ${money}. You are broke.")
