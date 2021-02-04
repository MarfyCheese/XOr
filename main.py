from base64 import b64decode, b64encode
def xordecode(message,key):
  message64 = b64decode(message)
  messagetwo = bytearray(message64)
  
  messageThree = bytearray()
  for b in messagetwo:
    messageThree.append(b ^ key)

  return(messageThree.decode("ASCII"))

def xorencode(message,key):
  bightarray = bytearray(message, encoding = 'ASCII')
  xoredarray = bytearray()
  for b in bightarray:
    xoredarray.append(b ^ key)
  return(b64encode(xoredarray))

thing = input("would you like to encode or decode\n")
if thing == "encode" or thing == "Encode":
  print(xorencode(input("please enter the thing to encode\n"), int(input("please enter the key\n"))))
elif thing == "decode" or thing == "Decode":
  print(xordecode(input("please enter the thing to decode\n"), int(input("please enter the key\n"))))
else:
  print("that is not a valid request")

