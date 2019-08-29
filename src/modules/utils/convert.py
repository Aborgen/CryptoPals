import base64

def hex2b64(hexString):
  b = hex2bytes(hexString)
  return base64.b64encode(b)

def hex2bytes(hexString):
  isHex, eInfo = validateHex(hexString)
  if not isHex:
    raise ValueError(f"'{hexString}' is not valid hex {eInfo}") 

  b = bytes.fromhex(hexString)
  return b

def bytes2hex(b):
  isBytes = validateBytes(b)
  if not isBytes:
    raise ValueError(f"'{b}' is not a bytes object")
  
  hexString = bytes.hex(b)
  return hexString
 
def validateHex(hexString):
  isHex = True
  eInfo = ''
  if type(hexString) != str:
    isHex = False
    eInfo = "(value must be of type str)"
  try:
    int(hexString, 16)
  except ValueError as err:
    isHex = False
    eInfo = "(value can not be parsed as hex)"

  if len(hexString) % 2 != 0:
    isHex = False
    eInfo = "(numbers must be in pairs)"
 
  return (isHex, eInfo) 

def validateBytes(b):
  return type(b) == bytes
