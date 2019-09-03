from . import initCrypto
from ..utils.collections import normalizeListSize
from ..utils.convert import hex2bytes, isBytes, isHex

def fixedXOR(a, b):
  if not isBytes(a):
    a = hex2bytes(a) if isHex(a) else a.encode()

  if not isBytes(b):
    b = hex2bytes(b) if isHex(b) else b.encode()

  encrypted = bytearray()
  for aByte, bByte in zip(a, b):
    encrypted.append(aByte ^ bByte)
  
  return bytes(encrypted)

