import math
from os import name, system
import random
from targets import targets as targetsOfAnyLength
from wordlist import wordlist as wordsOfAnyLength

LENGTH = 5
HUMAN_PLAYER = True

targets = []
for target in targetsOfAnyLength:
  if len(target) == LENGTH:
    targets.append(target)

wordlist = []
for word in wordsOfAnyLength:
  if len(word) == LENGTH:
    wordlist.append(word)

wordlist.sort()

def getPercentage(index: int) -> str:
  return f"{round(index / len(wordlist) * 100, 2)}%"

# choose a random target word to guess
# find where it is amongst all the words
target = wordlist.index(random.choice(targets))
closestBelow = -1
closestAbove = -1
guessIndex = -1
guessCount = 0

def printInstructions():
  print(f"The game is to guess the target {LENGTH}-letter word.")
  print("You can guess whatever words you like, but the target will always be a dictionary word.")
  print("I.e. \"GROW\" might be the target word, but not \"GROWN\" or \"GROWING\".")
  print("British spelling is preferred to American. E.g. \"Vapour\" is allowed, but not \"Vapor\".")
  print("Type in your guess and you will get a hint about how close you were.")
  print("Keep narrowing down your guesses until you find the target word.")
  print("Guess ? to give up.")
  print()
printInstructions()

def guessWord():
  global guessCount
  guessCount += 1
  if HUMAN_PLAYER:
    return input("Guess: ").lower()
  
  lo = closestBelow if closestBelow >= 0 else 0
  hi = closestAbove if closestAbove >= 0 else len(wordlist)
  return wordlist[lo + math.floor((hi - lo) / 2)]

print(f"The target is {getPercentage(target)} through the {LENGTH}-letter words")

while guessIndex != target:
  guess = guessWord()

  if (guess == 'prince'):
    print("👑 What's a mob to a king?")

  if (guess == '?'):
    print("Too bad, the target word was: " + wordlist[target])
    break
    
  if len(guess) != LENGTH:
    print(f"Please guess a {LENGTH}-letter word")
    continue

  try:
    guessIndex = wordlist.index(guess)
  except ValueError:
      print(f"⚠️ Your guess \"{guess}\" was not in the dictionary")
      continue
  
  if guessIndex == target:
    print(f"💯 Well done! You won in {guessCount} guesses!")
    continue

  if guessIndex < target and guessIndex > closestBelow:
    closestBelow = guessIndex
  elif guessIndex > target and (closestAbove == -1 or guessIndex < closestAbove):
    closestAbove = guessIndex

  if HUMAN_PLAYER:
    system('cls' if name == 'nt' else 'clear')
  
    if closestBelow >= 0:
      print(f"Closest guess below target: {wordlist[closestBelow]} ({getPercentage(closestBelow)})")

    print(f"The target is {getPercentage(target)} through the {LENGTH}-letter words")

    if closestAbove >= 0:
      print(f"Closest guess above target: {wordlist[closestAbove]} ({getPercentage(closestAbove)})")

  print(f"Your guess \"{guess}\" is {getPercentage(guessIndex)} through the {LENGTH}-letter words")