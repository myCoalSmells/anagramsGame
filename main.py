###########DEFINE&IMPORT##############
import random
import time
guessedwords = []
playersdone=0
points=0
def openFilePopulateWordList():
    tempList = []
    f = open('speech.txt', 'r')
    for line in f:
        words = line.split()
        for w in words:
            tempList.append(w)
    return tempList
findWords = ["peace"]

wordList = openFilePopulateWordList()

def filterlength(length,list):
  blanku=[]
  for i in list:
    if len(i) == length:
      blanku.append(i)
  return blanku

def checkifGuessed(Guess,listofWords):
  if Guess in guessedwords:
    isitUsed = True
  else:
    isitUsed = False
  if isitUsed:
    print 'Word already used!'
  else:
      guessedwords.append(Guess)
      print "Your guessed words are "+ str(guessedwords)
      checkAnagram(Guess,listofWords)
      

def checkAnagram(Guess1,wordList):
  x=len(Guess1)
  if Guess1 in filterlength(x,wordList):
    global points
    points = points + (x*x)*500-(2900*x)+4400
    print "Nice!"
    print "Points: "+str(points)
  else:
    print Guess1+" is not a word!"
      
  
  

#####################################


#######START THE GAME######
print "Welcome to anagrams! In this game, you will be given 6 random letters. Unscramble them and make as many words as possible!"
print ""
print " ***IMPORTANT: YOU MUST USE CAPITAL LETTERS.***"
print ""
print "3 letters = 200"
print "4 letters = 800"
print "5 letters = 2,400"
print "6 letters = 5,000!"
print ""
go = "no"
while go != "YES":
  go = raw_input("type [YES] to continue.")
print "Game start! Here are your letters!"
gameon="true"
###########################

########ASSIGN LETTERS#########
vowels=["A","E","I","O","U"]
chosenletterlist=[]
letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
letter1=(random.choice(vowels))
chosenletterlist.append(letter1)
letter2=(random.choice(letters))
while letter2 == chosenletterlist[0]:
  letter2=(random.choice(letters))
chosenletterlist.append(letter2)
letter3=(random.choice(vowels))
for givenletters in chosenletterlist:
    while givenletters == letter3:
      letter3=(random.choice(vowels))
chosenletterlist.append(letter3)
letter4=(random.choice(letters))
for givenletters in chosenletterlist:
    while givenletters == letter4:
      letter4=(random.choice(letters))
chosenletterlist.append(letter4)
letter5=(random.choice(letters))
for givenletters in chosenletterlist:
    while givenletters == letter5:
      letter5=(random.choice(letters))
chosenletterlist.append(letter5)
letter6=(random.choice(letters))
for givenletters in chosenletterlist:
    while givenletters == letter6:
      letter6=(random.choice(letters))
print letter1+" "+letter2+" "+letter3+" "+letter4+" "+letter5+" "+letter6
ingameletters=[letter1,letter2,letter3,letter4,letter5,letter6]
#################################
while gameon=="true":
  guess=""
  guess=raw_input("Unscramble letters: ")
  listedGuess=list(guess)
  if all(guessletter in ingameletters for guessletter in listedGuess):
    isitAnagram = True
  else:
    isitAnagram = False
  if isitAnagram == True:
    checkifGuessed(guess,wordList)
  else:
    print "This word is not made from your original letters!"