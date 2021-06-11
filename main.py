import random
counter = 0
word_list = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

def get_word():
  word = random.choice(word_list)
  return word.upper()



def play(word):
  print ()
  naam = input ('Hoe heet je? ')
  print ()
  print ("Hallo,", naam,"We spelen galgje, leuk dat je mee doet!" )
  print ()
  print("Je wint door letters te raden en zo achter het woord te komen.")
  print( )
  print("Je hebt 5 levens en als deze levens op zijn ben je dood.")
  print( )
  print("Laten we beginnen!")
  print( )
  print("Het eerste woord heeft " + str(len(word)) + " letters")

  word_completion = "_" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 5

  


  print(word_completion)
  print("\n")

  while not guessed and tries > 0:
    guess = input("kies een letter:").upper()
    if guess == word:
      print("Goed gedaan! Je hebt het woord" + word + "goed geraden!")
      print("Dit is het einde van het spel, klik op Run om het spel nog een keer te spelen!")
      break

    if guess in guessed_letters:
      print("Je hebt deze letter al een keer geraden.")

    elif guess not in word:
      print(guess,"komt niet in het woord voor.")
      tries -= 1
      guessed_letters.append(guess)
      print("Je hebt nog " + str(tries) + " beurten over")
     if tries -= 1
          print("""____
     |
     |
     |
     |
     |
_____|""")
    if tries -= 2
    print("""  ____
  | \|
     |
     |
     |
     |
_____|""")
    if tries -=3
    print ("""  ____
  | \|
  0  |
  |  |
     |
     |
_____|""")
    if tries -=4
    print ("""  ____
  | \|
  0  |
 /|\ |
     |
     |
_____|""")
    if tries -=5
    print("""  ____
  | \|
  0  |
 -|- |
 / \ |
     |
_____|""")
      


    else:
      print("goed gekozen, " + guess + " komt in het woord voor!")
      guessed_letters.append(guess)
      word_as_list = list(word_completion) 
     

     


play(get_word())
print(get_word())




