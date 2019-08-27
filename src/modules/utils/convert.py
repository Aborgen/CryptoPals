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

def validateHex(hexString):
  try:
    int(hexString, 16)
  except ValueError as err:
    return false

  return len(hexString) % 2 == 0
