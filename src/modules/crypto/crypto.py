from . import initCrypto
from ..utils.collections import normalizeListSize
from ..utils.compare import isBytes
from ..utils.convert import toBytes

def fixedXOR(a, b):
  if not isBytes(a):
    a = toBytes(a)

  if not isBytes(b):
    b = toBytes(b)

  encrypted = bytearray()
  for aByte, bByte in zip(a, b):
    encrypted.append(aByte ^ bByte)
  
  return bytes(encrypted)

def repeatingXOR(line, key):
  return fixedXOR(line, key * len(line))
