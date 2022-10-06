def checkSymmetry(userInput):
  lengthString = len(userInput)
  bracket = {"(":")","{":"}","[":"]"}
  oppositeBracket = {")":"(","}":"{","]":"[]"}
  #easy catch since symmetry requires an even string
  if lengthString %2 is 0:
      firstHalf = userInput[:lengthString//2]
      secondHalf = userInput[lengthString//2::]
      oppositeHalf = ""
      #if both halfs are equal, symmetrical
      if firstHalf is secondHalf:
          return True
      #iterate through second half in reverse
      for element in reversed(secondHalf):
          #find the inverse of second half
          if element in bracket.keys():
            oppositeHalf += bracket[element]
          #find the inverse of second half
          if element in oppositeBracket.keys():
            oppositeHalf += oppositeBracket[element]
      #if the reverse inverse is equal, you have symmetry
      if firstHalf is oppositeHalf:
          return True         
  else:
      return False
print(checkSymmetry("()()"))
print(checkSymmetry("((){})"))
print(checkSymmetry("({})"))