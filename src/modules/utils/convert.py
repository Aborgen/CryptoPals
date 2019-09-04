import base64
from .compare import _validateBytes, _validateHex

def hex2b64(hexString):
  b = hex2bytes(hexString)
  return base64.b64encode(b)

def hex2bytes(hexString):
  isHex, eInfo = _validateHex(hexString)
  if not isHex:
    raise ValueError(f"'{hexString}' is not valid hex {eInfo}") 

  b = bytes.fromhex(hexString)
  return b

def bytes2hex(b):
  isBytes = _validateBytes(b)
  if not isBytes:
    raise ValueError(f"'{b}' is not a bytes object")
  
  hexString = bytes.hex(b)
  return hexString

