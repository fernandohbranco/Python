from random import *


name = input("What is your name? ").title()
d = {1: 'James', 2: 'Robert', 3: 'John', 4: 'Michael', 5: 'William', 6: 'David', 7: 'Richard', 8: 'Joseph', 9: 'Thomas',
     10: 'Charles', 11: 'Christopher', 12: 'Daniel', 13: 'Matthew', 14: 'Anthony', 15: 'Mark', 16: 'Donald', 17: 'Steven',
     18: 'Paul', 19: 'Andrew', 20: 'Joshua', 21: 'Kenneth', 22: 'Kevin', 23: 'Brian', 24: 'George', 25: 'Edward', 26: 'Ronald',
     27: 'Timothy', 28: 'Jason', 29: 'Jeffrey', 30: 'Ryan', 31: 'Jacob', 32: 'Gary', 33: 'Nicholas', 34: 'Eric', 35: 'Jonathan',
     36: 'Stephen', 37: 'Larry', 38: 'Justin', 39: 'Scott', 40: 'Brandon', 41: 'Benjamin', 42: 'Samuel', 43: 'Gregory', 44: 'Frank',
     45: 'Alexander', 46: 'Raymond', 47: 'Patrick', 48: 'Jack', 49: 'Dennis', 50: 'Jerry', 51: 'Tyler', 52: 'Aaron', 53: 'Jose',
     54: 'Adam', 55: 'Henry', 56: 'Nathan', 57: 'Douglas', 58: 'Zachary', 59: 'Peter', 60: 'Kyle', 61: 'Walter', 62: 'Ethan',
     63: 'Jeremy', 64: 'Harold', 65: 'Keith', 66: 'Christian', 67: 'Roger', 68: 'Noah', 69: 'Gerald', 70: 'Carl', 71: 'Terry',
     72: 'Sean', 73: 'Austin', 74: 'Arthur', 75: 'Lawrence', 76: 'Jesse', 77: 'Dylan', 78: 'Bryan', 79: 'Joe', 80: 'Jordan',
     81: 'Billy', 82: 'Bruce', 83: 'Albert', 84: 'Willie', 85: 'Gabriel', 86: 'Logan', 87: 'Alan', 88: 'Juan', 89: 'Wayne',
     90: 'Roy', 91: 'Ralph', 92: 'Randy', 93: 'Eugene', 94: 'Vincent', 95: 'Russell', 96: 'Elijah', 97: 'Louis', 98: 'Bobby',
     99: 'Philip', 100: 'Johnny', 101: 'Mary', 102: 'Patricia', 103: 'Jennifer', 104: 'Linda', 105: 'Elizabeth', 106: 'Barbara',
     107: 'Susan', 108: 'Jessica', 109: 'Sarah', 110: 'Karen', 111: 'Nancy', 112: 'Lisa', 113: 'Betty', 114: 'Margaret', 115: 'Sandra',
     116: 'Ashley', 117: 'Kimberly', 118: 'Emily', 119: 'Donna', 120: 'Michelle', 121: 'Dorothy', 122: 'Carol', 123: 'Amanda',
     124: 'Melissa', 125: 'Deborah', 126: 'Stephanie', 127: 'Rebecca', 128: 'Sharon', 129: 'Laura', 130: 'Cynthia', 131: 'Kathleen',
     132: 'Amy', 133: 'Shirley', 134: 'Angela', 135: 'Helen', 136: 'Anna', 137: 'Brenda', 138: 'Pamela', 139: 'Nicole', 140: 'Emma',
     141: 'Samantha', 142: 'Katherine', 143: 'Christine', 144: 'Debra', 145: 'Rachel', 146: 'Catherine', 147: 'Carolyn', 148: 'Janet',
     149: 'Ruth', 150: 'Maria', 151: 'Heather', 152: 'Diane', 153: 'Virginia', 154: 'Julie', 155: 'Joyce', 156: 'Victoria', 157: 'Olivia',
     158: 'Kelly', 159: 'Christina', 160: 'Lauren', 161: 'Joan', 162: 'Evelyn', 163: 'Judith', 164: 'Megan', 165: 'Cheryl', 166: 'Andrea',
     167: 'Hannah', 168: 'Martha', 169: 'Jacqueline', 170: 'Frances', 171: 'Gloria', 172: 'Ann', 173: 'Teresa', 174: 'Kathryn', 175: 'Sara',
     176: 'Janice', 177: 'Jean', 178: 'Alice', 179: 'Madison', 180: 'Doris', 181: 'Abigail', 182: 'Julia', 183: 'Judy', 184: 'Grace',
     185: 'Denise', 186: 'Amber', 187: 'Marilyn', 188: 'Beverly', 189: 'Danielle', 190: 'Theresa', 191: 'Sophia', 192: 'Marie', 193: 'Diana',
     194: 'Brittany', 195: 'Natalie', 196: 'Isabella', 197: 'Charlotte', 198: 'Rose', 199: 'Alexis', 200: 'Kayla'}

print(f"Hello {name}, let's play the Hangman. Good luck!")


dict_size = len(d) # Identify the size of the dictionary
random_number = randint(1, dict_size) # Get a random key
secret_name = (d[random_number]).upper() # Get the value related to the random key
guesses = "" # Create a variable with an empty value
turns = 5 # Number of turns

# While loop to check if the number of turns are more then zero
while turns > 0:
    failed = 0

    print("")

    for char in secret_name: # for every charcter in secret_name

        if char in guesses:
            print(char,end=" ")
        else:
            print("_",end=" ")
            failed += 1

    print("")

    if failed == 0:
        print("")
        print(f"Congratulations {name}, you won the game!")
        break

    if turns > 1:
        last = "guesses"
    else:
        last = "guess"

    print(f"You have {turns} {last}. {guesses}")

    guess = input("> Guess a character: ").upper()

    while len(guess) != 1:
        guess = input("> Guess a character (It must have 1 character): ").upper()

    guesses += guess

    if guess not in secret_name:
        turns -= 1

        print("")
        print("")
        print("TRY AGAIN.")

    if turns == 0:
        print(f"The secret name was {secret_name}.")
        print("You failed. More luck next time!")