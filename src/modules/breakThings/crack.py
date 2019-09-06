from . import initBreak
from enum import Enum
from modules.crypto.crypto import fixedXOR
from modules.utils.convert import hex2bytes
from modules.utils.file import readJSON
from typing import NamedTuple

class XORType(Enum):
  SINGLE = 0
  REPEATING = 1

class Candidate(NamedTuple):
  score:  int
  key:    str
  base:   str
  secret: str

def crackXOR(byteObject, scoreFile, EType):
  if not isBytes(byteObject):
    byteObject = hex2bytes(byteObject) if isHex(byteObject) else byteObject.encode()

  if EType == XORType.SINGLE:
    return _crackSingleXOR(byteObject, scoreFile)
  elif EType == XORType.REPEATING:
    raise NotImplementedError
    #return crackRepeatingXOR(hexString)
  else:
    raise NotImplementedError

def _crackSingleXOR(byteObject, scoreFile):
  if not isBytes(byteObject):
    raise ValueError("Input must be a bytes object")

  frequentLetters = {key.encode(): value for key, value in readJSON(scoreFile).items()}
  bestCandidate = Candidate(0, '', '', '')
  # We skip 0, since XORing against a bunch of 0s isn't going to do anything
  byteLength = len(byteObject)
  for i in range(1, 256):
    # The string interpolation will convert i into hex, and pad it with 0 if need be.
    possibleKey = f'{i:02x}' * byteLength
    secret = fixedXOR(byteObject, possibleKey)
    score = calculateScore(secret, frequentLetters)
    if score > bestCandidate.score:
      encodedByUTF8 = True
      try:
        secret.decode()
      except:
        encodedByUTF8 = False

      if encodedByUTF8:
        bestCandidate = Candidate(score, possibleKey, byteObject, secret)

  return bestCandidate

def calculateScore(secret, keyList):
  score = 0
  for key, value in keyList.items():
    score += (secret.count(key) * value)
  
  return round(score, 4)
