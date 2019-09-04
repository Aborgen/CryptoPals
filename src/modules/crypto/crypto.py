from . import initCrypto
from ..utils.collections import normalizeListSize
from ..utils.compare import isBytes, isHex
from ..utils.convert import hex2bytes

def fixedXOR(a, b):
  if not isBytes(a):
    a = hex2bytes(a) if isHex(a) else a.encode()

  if not isBytes(b):
    b = hex2bytes(b) if isHex(b) else b.encode()

  encrypted = bytearray()
  for aByte, bByte in zip(a, b):
    encrypted.append(aByte ^ bByte)
  
  return bytes(encrypted)

def repeatingXOR(line, key):
  return fixedXOR(line, key * len(line))
