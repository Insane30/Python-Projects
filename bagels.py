import random
#function to compare the numbers
def provide_hint(secret_number, guess):
    feedback = ""
    count = 0
    c = 0
    
    for i in range(len(secret_number)):
        if secret_number[i] == str(guess)[i]:
            count += 1
        if secret_number[i] in str(guess):
            c += 1
    
    if count == 3 and c == 3:
        feedback += "Great! You got it"
        return True, feedback
    elif c == 0:
        feedback += "Bagel"
    else:
        feedback += "Fermi " * count + "Pico " * (c - count)
    
    print(feedback)
    return False, feedback

def play_game():
    print("Bagels, A deductive logic game.")
    print("By Ayush Kachhap(2241011004).")
    print('''I am thinking of 3-digit number. Try to guess what it is.
    Here are some clues:
    When i say:     That means:
     Pico           One digit is correct but in the wrong position.
     Fermi          One digit is correct and in the right position.
     Bagels         No digit is correct
    I have thought up a number.
     You have 10 guesses to get it.''')

    secret_number = generate_secret_number()
    game =0
    for i in range(10):
        guess = int(input(f"Guess #{i+1} : "))
        if len(str(guess)) > 3:
            print("Enter the digits within the range !")
            play_game()
        success, feedback = provide_hint(secret_number, guess)
        
        if success:
            print(feedback)
            print(f"You guessed the number in {i + 1} tries!")
            game+=1
            break

        if i == 9:
            print(f"Sorry, you're out of tries. The secret number was {secret_number}")
            again = input("Do you want to play again? ")
            if again == 'yes':
                play_game()
            else:
                print("Thanks for playing!")
    if game ==1:
        again = input("Great ! Do you want to play again? ")
        if again == 'yes':
            play_game()
        else:
            print("Thanks for playing!")

    
# Function to generate a secret number
def generate_secret_number():
    numbers = list(range(100, 999))
    random_num = random.sample(numbers,1)[0]
    return str(random_num)

# Main
play_game()
