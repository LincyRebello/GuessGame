import random 

# """ Constans """
COLORS = ["R", "G","B","Y","W", "O"]
TRIES = 10
CODE_LENGTH = 4


# """ Functions """
def generate_code():
    # """ create a list """
    code = []

    for _ in range(CODE_LENGTH):
        color =  random.choice(COLORS)
        code.append(color)

    return code

# """ funcion for the user to guess the code """
# """ f string allows to embeed variables direcly in string using {} """
#  """ split removes the spaces  """  
def guess_code():

    while True: 
        guess =  input("Guess: ").upper().split(" ")   
  
    
        if len(guess) != CODE_LENGTH:
          print(f"You must guess {CODE_LENGTH} colors.")   
          continue

        for color in guess:
             if color not in COLORS:
                print(f"Invalid Colour:{color}. Try again.")
                break
        else:
             break
      
    return guess
   

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_colur, real_color in zip(guess, real_code): 
    # zip functions works in tuples
        if guess_colur == real_color:
            correct_pos += 1
            color_counts[guess_colur] -= 1

    for guess_colur, real_color in zip(guess, real_code): 
        if guess_colur in color_counts and color_counts[guess_colur] > 0:
            incorrect_pos += 1
            color_counts[guess_colur] -= 1

    return correct_pos, incorrect_pos


def logic():

    print(f"Welcome to this Guess Game, You have {TRIES} to guess the code...")
    print("The Valid colours are", *COLORS)
    
    code =  generate_code()
    for attempts in range(1, TRIES + 1):
        guess =  guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        
        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!!")
            break

        print(f"Correct Position: {correct_pos} | Incorrect positions: {incorrect_pos}")

    else:
        print("You ran out of tries the code was:", *code)
    
    # *code prints it in nice way with spaces


if __name__ == "__main__":  
    logic()




        


    

