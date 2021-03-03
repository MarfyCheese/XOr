from base64 import b64decode, b64encode
def xordecode(message,key):
  message64 = b64decode(message)
  messagetwo = bytearray(message64)
  
  messageThree = bytearray()
  for b in messagetwo:
    messageThree.append(b ^ key)
  try:
    return(messageThree.decode('ASCII'))
  except:
    pass

def key_scoring(message):
  listOfScores = []
  for i in range(256):
    keyScore = 0
    try:
      thing = xordecode(message,i)
    except UnicodeDecodeError:
      pass
    try:
      for i in range(len(thing)):
        keyScore += english_score(thing[i])
      listOfScores.append(keyScore)
      print(len(listOfScores))
    except:
      pass


  best = 0
  best2 = 1
  best3 = 2
  best4 = 3
  best5 = 4

  for i in range(128):
    if listOfScores[i] < listOfScores[best]:
      best = i
    elif listOfScores[i] > listOfScores[best] and listOfScores[i] < listOfScores[best2] and i != best:
      best2 = i
    elif listOfScores[i] > listOfScores[best2] and listOfScores[i] < listOfScores[best3] and i != best2:
      best3 = i
    elif listOfScores[i] > listOfScores[best3] and listOfScores[i] < listOfScores[best4] and i != best3:
      best4 = i
    elif listOfScores[i] > listOfScores[best4] and listOfScores[i] < listOfScores[best5] and i != best4 :
      best5 = i
  
  print(best)
  print(best2)
  keysToReturn = []
  keysToReturn.append(best)
  keysToReturn.append(best2)
  keysToReturn.append(best3)
  keysToReturn.append(best4)
  keysToReturn.append(best5)
  return keysToReturn

def english_score(letter):
  capitalList = ["E","T","A","O","I","N","S","H","R","D","L","C","U","M","W","F","G","Y","P","B","V","K","J","X","Q","Z"]
  lowerList = ["e","t","a","o","i","n","s","h","r","d","l","c","u","m","w","f","g","y","p","b","v","k","j","x","q","z"]
  ltbs = letter
  if ord(ltbs) == 32:
    return 0
  elif ord(ltbs) > 122 or ord(ltbs) < 65 or 90 < ord(ltbs) < 97 :
    return 100
  else: 
      if 64 < ord(ltbs) < 91:
        for i in range(26):
          if ltbs == capitalList[i]:
            return int(i + 1)
      else:
        for i in range(26):
          if ltbs == lowerList[i]:
            return int(i + 1)
  
def xorencode(message,key):
  bightarray = bytearray(message, encoding = 'ASCII')
  xoredarray = bytearray()
  for b in bightarray:
    xoredarray.append(b ^ key)
  return(b64encode(xoredarray))

def main():
  thing = input("would you like to encode or decode\n")
  
  if thing == "encode" or thing == "Encode":
    print(xorencode(input("please enter the thing to encode\n"), int(input("please enter the key\n"))))
  elif thing == "decode" or thing == "Decode":
    decodeMessage = input("please enter the thing to decode\n")
    listOfKeys = key_scoring(decodeMessage)
    for i in range(5):
      print(xordecode(decodeMessage,listOfKeys[i]))
  else:
    print("that is not a valid request")

main()