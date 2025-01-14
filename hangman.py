import random
from inputimeout import inputimeout
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

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra elephant alligator cheetah ').split()



while True:

    
    mode=input("Do you want to play hard mode or easy mode? Type h for hard and e for easy Type quit to quit game ")

    if mode=="quit":
        break
    word=random.choice(words)
    blanks = ["_" for i in word]
    if mode=="e":

        lives=6
        pic=0


        while lives > 0:

            if "_" not in blanks:
                print(HANGMANPICS[pic])
                print(" ".join(blanks))
                print("You Win!")
                break
            print(HANGMANPICS[pic])
            print(" ".join(blanks))
            guess=input("Guess a letter ")
            if guess in word:
                print("correct!")
                for i in range(len(word)):
                    if guess==word[i]:
                        blanks[i]=guess
            else:
                print("wrong!")
                lives-=1
                pic+=1

        if "_" in blanks:
            print(HANGMANPICS[pic])
            print(" ".join(blanks))
            print("You Lose! The word was " + word)


    else:

        lives=6
        pic=0


        while lives > 0:
            timeout=False
            if "_" not in blanks:
                print(HANGMANPICS[pic])
                print(" ".join(blanks))
                print("You Win!")
                break
            print(HANGMANPICS[pic])
            print(" ".join(blanks))

            try:
                guess=inputimeout(prompt="Guess a letter ",timeout=5)
            except Exception:
                guess="!"
                print("Time Over!")
                timeout=True
            if guess in word:
                print("correct!")
                for i in range(len(word)):
                    if guess==word[i]:
                        blanks[i]=guess
            else:
                if not timeout:
                    print("wrong!")
                lives-=1
                pic+=1

        if "_" in blanks:
            print(HANGMANPICS[pic])
            print(" ".join(blanks))
            print("You Lose! The word was " + word)
