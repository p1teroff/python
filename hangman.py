import random

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
        hangman()
    elif y_n == 'n':
        print('Alright see you next time!')
        break
    else:
        print('Write only y or n!')



    

    