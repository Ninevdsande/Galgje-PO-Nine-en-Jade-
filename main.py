import random
word_list = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

def get_word():
  word = random.choice(word_list)
  return word.upper()

def display_hangman():
  aap = 1

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
    if guess in guessed_letters:
      print("Je hebt deze letter al een keer geraden.")
    elif guess not in word:
      print(guess,"komt niet in het woord voor.")
      tries -= 1
      guessed_letters.append(guess)
    else:
      print("goed gekozen," + guess + "komt in het woord voor!")
      guessed_letters.append(guess)
      word_as_list = list(word_completion)

print(get_word())