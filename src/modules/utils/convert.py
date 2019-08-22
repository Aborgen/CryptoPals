import base64

def hex2b64(hexString):
  byteArr = bytearray.fromhex(hexString)
  return base64.b64encode(byteArr)

