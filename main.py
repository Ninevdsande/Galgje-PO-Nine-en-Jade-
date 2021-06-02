import random
word_list = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

def get word(word_list):
  word = random.choice(word_list)
  return word.upper


def play(word):
  word_completion = "_" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 5
  print("Je gaat galgje spelen!")
  print(display_hangman(tries))
  print(word_completion)
  print("\n")
  while not guessed and tries > 0:
    guess = input("kies een letter:").upper()
    if len(guess) == 1 


