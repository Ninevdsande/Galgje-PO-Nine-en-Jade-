import random
word_list = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

def get_word():
  word = random.choice(word_list)
  return word.upper()



def play(word):
  print ()
  naam = input ('Hoe heet je? ')
  print ()
  print ("Hallo,", naam,"we spelen galgje, leuk dat je mee doet!" )
  print ()
  print("Je wint door letters te raden en zo achter het woord te komen, als je denkt het hele woord te weten moet je deze helemaal intypen.")
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
  counter = 0
  tries = 5
  
 

  print(word_completion)
  print("\n")

  while not guessed and counter < 5:
    guess = input("kies een letter/ typ het hele woord in:").upper()
    if guess == word:
      print("Goed gedaan! Je hebt het woord " + word + " goed geraden!")
      print("Dit is het einde van het spel, klik op Run om het spel nog een keer te spelen!")
      break

    elif guess in word:
      print("goed gekozen, " + guess + " komt in het woord voor!")
      
      guessed_letters.append(guess)    
      word_as_list = list(word_completion) 
      indices = [i for i, letter in enumerate(word) if letter == guess]
      for index in indices: 
        word_as_list[index] = guess
      word_completion = "".join(word_as_list) 
      
     
    elif guess not in word:
      print(guess," komt niet in het woord voor.")
      tries -= 1
      guessed_letters.append(guess)
      print("Je hebt nog " + str(tries) + " beurten over")
      counter= counter + 1
      if counter== 1:
        print("""____
     |
     |
     |
     |
     |
_____|""")
    if counter == 2:
      print("""  ____
  | \|
     |
     |
     |
     |
_____|""")
    if counter == 3:
      print ("""  ____
  | \|
  0  |
  |  |
     |
     |
_____|""")
    if counter == 4:
      print ("""  ____
  | \|
  0  |
 /|\ |
     |
     |
_____|""")
    if counter == 5:
      print("""  ____
  | \|
  0  |
 -|- |
 / \ |
     |
_____|""")
  

  if counter ==5:
    print("Jammer!Je hebt het woord niet geraden. Het woord was "+ word +" Volgende keer beter! Als je het nog een keer wilt proberen klik dan op run.")

  
play(get_word())
print(get_word())





