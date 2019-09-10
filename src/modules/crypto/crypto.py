from Crypto.Cipher import AES
from enum import Enum
from . import initCrypto
from ..utils.collections import normalizeListSize
from ..utils.compare import isBytes
from ..utils.convert import toBytes

class Action(Enum):
  ENCRYPT = 0
  DECRYPT = 1

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

def ECB_AES128(key, text, action):
  if not isBytes(key):
    key = toBytes(key)

  if not isBytes(text):
    text = toBytes(text)

  cipher = AES.new(key, AES.MODE_ECB)

  if action == Action.ENCRYPT:
    # ECB requires length to be a multiple of 16.
    text = pad(text, 16)
    return cipher.encrypt(text)
  elif action == Action.DECRYPT:
    return cipher.decrypt(text)
  else:
    raise ValueError

# This is an implementation of PKCS#7 padding
def pad(text, multiple):
  if not isBytes(text):
    text = toBytes(text)

  if len(text) % multiple == 0:
    return text

  missing = multiple - (len(text) % multiple)
  correctedLength = len(text) + missing
  text = text.ljust(correctedLength, bytes([missing]))
  return text
