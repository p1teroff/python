import random

def guessing_number_game():   
    random_number = random.randint(0, 100)

    print("The computer have choosen a random number from 0 to 100. Try to guess it.")
    
    while True:
        
        try:
            user_input_number = int(input('Write a number here: '))
            difference = random_number - user_input_number
            
            if difference < 0:
                difference*=-1
            
            if difference == 0:
                print('You have guessed the number')
                print(random_number)
                break
            
            elif difference >= 50:
                print('You are too far. (+-50)')
            
            elif difference >= 30:
                print('You are still too far. (+-30')
            
            elif difference >=10:
                print('You are almost there. (+-10')
            
            elif difference >=5:
                print('You are almost there. (+-5)')
        
        except ValueError:
            print('Input integer! Try again!')
    
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
         
def hangman():
    
    words = [
        "ability", "absence", "academy", "accident", "accuracy", "achievement", "acknowledge",
        "acquire", "activity", "addition", "adequate", "adjustment", "administration", "adult",
        "adventure", "advocate", "aesthetic", "aggregate", "algorithm", "alliance", "ambiguity",
        "amplitude", "analogous", "analysis", "anomaly", "antenna", "antiquity", "apology", 
        "apparatus", "appetite", "applicable", "appointment", "appreciate", "approach",
        "aquarium", "arbitrary", "architecture", "artificial", "assessment", "assignment",
        "assumption", "atmosphere", "attachment", "autonomy", "avalanche", "bachelor", "bacteria",
        "balloon", "bankruptcy", "barrier", "beverage", "billionaire", "biography", "blackberry",
        "bluetooth", "bravery", "breakfast", "broccoli", "brotherhood", "brutality", "budget",
        "butterfly", "calculator", "camouflage", "campaign", "candidate", "cappuccino", "carpenter",
        "casualty", "catastrophe", "celebrity", "censorship", "challenge", "championship", "character",
        "charismatic", "cherry", "chocolate", "citizenship", "classification", "clever", "clothing",
        "coconut", "cognitive", "coincidence", "collaborate", "collective", "colloquium", "combination",
        "comfortable", "commander", "commemorate", "commercial", "communist", "community", "comparable",
        "compassionate", "compatible", "compliment", "comprehensive", "compromise", "concentrate", 
        "conceptual", "confidence", "consequence", "conservative", "considerable", "consistency",
        "constructive", "contemporary", "contribution", "convenience", "cooperative", "coordinate",
        "correlation", "countryside", "credibility", "cucumber", "curiosity"
    ]

    HANGMANPICS = ['''
                   
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
   
    print("Lets play Hangman, i give you a word you guess it")
    random_word = (random.choice(words))

     
    # word list
    empty_word_list = []
    for i in range(len(random_word)):
        empty_word_list.append(random_word[i])


    # the _________ word
    string_word = ""
    for i in range(len(random_word)):
        string_word+="_"
    print('')

    print(string_word)
    list_string_word = list(string_word)
    n = 0
    game = True
    
    while game:
        letter=input("Input a letter of the word: ")
        if letter in random_word:
            indices = [i for i, c in enumerate(random_word) if c == letter]
            
            for i in range(len(indices)):
                list_string_word[indices[i]] = letter
            
            new_list_string_word = ''.join(list_string_word)
            
            print(new_list_string_word)
            print(HANGMANPICS[n])
            
            if '_' not in new_list_string_word:
                print('CONGRATZ MY GUY, YOU WON FOR REAL')
                break
        
        else:
            try:
                try:
                    n+=1
                    print(new_list_string_word)
                    print(HANGMANPICS[n])
                except UnboundLocalError:
                    print('Write only 1 letter')
                
            except IndexError:
                print("YOU LOSE TRY AGAIN!")
                break

while True:
    y_n = input("Do you want to play? (Y or N) ").lower()
    if y_n == 'y':
        guessing_number_game() or rock_paper_scissors() or hangman()
    elif y_n == 'n':
        print('Alright see you next time!')
        break
    else:
        print('Write only y or n!')