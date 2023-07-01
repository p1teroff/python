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
    

    


while True:
    y_n = input("Do you want to play? (Y or N) ").lower()
    if y_n == 'y':
        guessing_number_game()
    elif y_n == 'n':
        print('Alright see you next time!')
        break
    else:
        print('Write only y or n!')
