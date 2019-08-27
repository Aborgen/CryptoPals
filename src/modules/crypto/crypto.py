from . import initCrypto
from ..utils.collections import normalizeListSize
from ..utils.convert import hex2bytes

def fixedXOR(a, b):
  aBytes = hex2bytes(a)
  bBytes = hex2bytes(b)
  normalizeListSize(aBytes, bBytes)
  encrypted = bytearray()
  for aByte, bByte in zip(aBytes, bBytes):
    encrypted.append(aByte ^ bByte)
  
  return bytes(encrypted)
    
