from Crypto.Cipher import AES
from enum import Enum
from . import initCrypto
from ..utils.collections import normalizeListSize
from ..utils.compare import isBytes
from ..utils.convert import toBytes
from ..utils.modify import pad, repeatPerCharacter

class Action(Enum):
  ENCRYPT = 0
  DECRYPT = 1

def fixedXOR(a, b):
  if not isBytes(a):
    a = toBytes(a)

  if not isBytes(b):
    b = toBytes(b)

  encrypted = bytes(aByte ^ bByte for aByte, bByte in zip(a, b))
  return encrypted

def repeatingXOR(line, key):
  if not isBytes(line):
    line = toBytes(line)

  if not isBytes(key):
    key = toBytes(key)

  return fixedXOR(line, repeatPerCharacter(key, len(line)))

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

