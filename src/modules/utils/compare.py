# We are interested in knowing--when we compare the two bytes objects, byte for byte--how many
# bits are different from each other. After XORing two bytes, counting all the ones will give us this answer.
def hammingDistance(aBytes, bBytes):
  differences = [bin(aByte ^ bByte).count('1') for aByte, bByte in zip(aBytes, bBytes)]
  return sum(differences)

def isHex(hexString):
  return _validateHex(hexString)[0]
 
def _validateHex(hexString):
  isHex = True
  eInfo = ''
  if type(hexString) != str:
    isHex = False
    eInfo = "(value must be of type str)"
  else:
    try:
      int(hexString, 16)
    except ValueError as err:
      isHex = False
      eInfo = "(value can not be parsed as hex)"

    if len(hexString) % 2 != 0:
      isHex = False
      eInfo = "(numbers must be in pairs)"
 
  return (isHex, eInfo) 

def isBytes(b):
  return _validateBytes(b)

def _validateBytes(b):
  return type(b) == bytes

def encodedByUTF8(byteObject):
  status = True
  try:
    byteObject.decode('utf-8')
  except:
    status = False

  return status

