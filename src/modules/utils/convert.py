import base64

def hex2b64(hexString):
  b = hex2bytes(hexString)
  return base64.b64encode(b)

def hex2bytes(hexString):
  isHex = validateHex(hexString)
  if not isHex:
    raise ValueError("'${hexString}' is not valid hex")

  b = bytes.fromhex(hexString)
  return b

def bytes2hex(b):
  isBytes = validateBytes(b)
  if not isBytes:
    raise ValueError("'${b}' is not a bytes object")
  
  hexString = bytes.hex(b)
  return hexString
 
def validateHex(hexString):
  try:
    int(hexString, 16)
  except ValueError as err:
    return false

  return len(hexString) % 2 == 0

def validateBytes(b):
  return type(b) == bytes
