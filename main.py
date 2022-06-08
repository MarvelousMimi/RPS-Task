import random
possible_options = ["R","P","S"]
options_map = {
    'R': "Rock",
    'P': "Paper",
    'S': "Scissors"
}

while True:

    print("""WELCOME TO ROCK- PAPER-SCISSORS
        Pick one of the options below:
            R- Rock;
            P- Paper;
            S- Scissors
        """)
     
    #Ask the user to pick an option
    user_choice = input("Your Choice:").upper()  #"R" 
    if user_choice not in possible_options: #checking if user is invalid
        print("[ERRROR]: Invalid option. Ty again!!") #printing the error message
        continue 
    computer_choice = random.choice(possible_options) # "S" #making computer pick randomly from the options
    user_pick =options_map.get(user_choice)     #"Rock"
    computer_pick = options_map.get(computer_choice)    # "Scissors"
    
    print("Player ("+ user_pick +"): CPU (" + computer_pick +")")
    
    if computer_pick == user_pick:        #checking if its a tie
        print("It is a TIE")            
        continue
    if (computer_pick == "Scissors"):       #when the computer picks scissors
        if (user_pick == "Rock"):
            print( "You WIN. Rock breaks scissors")
        elif (user_pick == "Paper" ):
            print("You LOSE. Scissors cuts Paper")
        break
    
    if (computer_pick == "Paper"):       #when the computer picks Paper
        if (user_pick == "Rock"):
            print( "You Lose. Paper covers Rock")
        elif (user_pick == "Scissors" ):
            print("You Win. Scissors cuts Paper")
        break
    
    if (computer_pick == "Rock"):       #when the computer picks Rock
        if (user_pick == "Paper"):
            print( "You WIN. Paper cover Rock")
        elif (user_pick == "Scissors" ):
            print("You LOSE. Rock breaks Scissors")
        break
# The End