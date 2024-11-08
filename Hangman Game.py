import random

# List of words to choose from
words = ["quiz", "myth", "twig", "flock", "frost", "gold", "zebra"]

# Choose a random word from the list and convert it to a list of characters
secret = list(random.choice(words))

# Initialize a list to store the guessed letters, initially all underscores
guessed = ['_'] * len(secret)

# Initialize the number of chances
chance = 6  # Assuming 6 chances, you didn't define it

# Define the hangman stages
stages = [  # You didn't define this, I added a simple one
    """
  +---+
  |   |
      |
      |
      |
      |
========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========"""
]

# Function to display the current state of the word
def display(word):
    print(' '.join(word))

# Main game loop
while True:
    # Ask the user to guess a letter
    letter = input("Guess a letter (a-z): ").lower()  # Convert to lowercase

    # Check if the letter is in the secret word
    if letter in secret:
        # Find the position of the letter in the secret word
        pos = secret.index(letter)
        # Update the guessed word with the correct letter
        guessed[pos] = letter
        # Display the current state of the word
        display(guessed)
        # Check if the user has guessed the entire word
        if guessed == secret:
            print("Congratulations! You guessed it right!")
            break
    else:
        # Reduce a chance
        chance -= 1
        # Display the current hangman stage
        print(stages[6 - chance - 1])  # Adjusted to match the chance variable
        # Check if the user has run out of chances
        if chance == 0:
            print("You lost the game. The correct word was : ", end='')
            display(secret)
            break
