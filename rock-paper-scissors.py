import random

def rock_paper_scissors():
    
    # // count wins //
    
    
    # // rock - paper - scissors // 
    game_attributes = ['scissors', 'rock', 'paper']
    
    computer_wins = 0
    user_wins = 0
    
    
    # // the hash map for the game //
    while True:
        u_input = input('Lets play rock-paper-scissors. What will you pick (q to quit): ').lower()
        c_input = random.choice(game_attributes)
        
        if u_input == 'q':
            break 
        
        if u_input not in game_attributes:
            print('Choose between the three only: scissors or rock or paper')
        
        if u_input == c_input:
            print("Computer chose: ", c_input)
            print(":3 Its a tie! :3")
            
        
        elif u_input == 'rock' and c_input == 'scissors':
            print('Computer chose: ', c_input)
            print(':3 You win! :3 ')
            user_wins+=1
            
        
        elif u_input == 'rock' and c_input == 'paper':
            print('Computer chose: ', c_input)
            print(':3 You lose! :3')
            computer_wins+=1
            
        
        elif u_input == 'scissors' and c_input == 'paper':
            print('Computer chose: ', c_input)
            print(':3 You win! :3')
            user_wins+=1
           
        
        elif u_input == 'scissors' and c_input == 'rock':
            print('Computer chose: ', c_input)
            print(':3 You lose! :3')
            computer_wins+=1
            
        elif u_input == 'paper' and c_input == 'rock':
            print('Computer chose: ', c_input)
            print(':3 You win! :3')
            user_wins+=1
        
        
        elif u_input == 'paper' and c_input == 'scissors':
            print('Computer chose: ', c_input)
            print(':3 You lose! :3 ')
            computer_wins+=1
            
        elif u_input == 'q':
            break
    print("The Computer won", computer_wins, 'times.')
    print("You won", user_wins, 'times.')
    
       
        
        
while True:
    y_n = input("Do you want to play? (Y or N) ").lower()
    if y_n == 'y':
        rock_paper_scissors()
    elif y_n == 'n':
        print('Alright see you next time!')
        break