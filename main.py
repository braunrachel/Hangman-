word = list("apple")
hidden = []
for character in word: 
  hidden.append("_")

attempts = 0
max_attempts = 4

# loop until player win or lose
isGameOver = False
while not isGameOver: 

  # display the current board, guessed lettres, and attempts left 
  print(f"You have {max_attempts - attempts} attempts remaining")
  
  print(f"The current word is: {' '.join(hidden)}")
  
  print ("     _____")
  print ("     |    |")
  print ("     |" + ("    O" if attempts > 0 else ""))
  print ("     |" + ("    V" if attempts > 1 else ""))
  print ("     |" + ("    |" if attempts > 2 else ""))
  print ("     |" + ("    ^" if attempts > 3 else ""))
  print ("_____________")
   

  # ask player for character
  letterGuessed = input ("Please guess a letter: ")
  
#if they guessed right 
  if letterGuessed in word: 
    print(f"You guessed correctly! {letterGuessed} is in the word.")
    for i in range (len(word)): 
      character = word[i]
      if character == letterGuessed: 
        hidden[i] = word[i]
        word[i] = "_"
  else:
  #if guessed wrong print failure message
    print(f"You guessed wrong.. {letterGuessed} is not in the word..")
    attempts += 1 


  # if the player has won print a win message and stop looping 
  if (all("_" == char for char in word)):
    print("Congrats! You won the game!")
    isGameOver = True
    # if the player has lost, print failing and stop looping 
  if (attempts >= max_attempts):
    print("Sorry... You lost the game!")
    isGameOver = True