from . import initBreak
from enum import Enum
from modules.crypto.crypto import fixedXOR
from modules.utils.file import readJSON
from typing import NamedTuple

class XORType(Enum):
  SINGLE = 0
  REPEATING = 1

class Candidate(NamedTuple):
  score:  int
  key:    str
  secret: str

def crackXOR(hexString, scoreFile, EType):
  if EType == XORType.SINGLE:
    return crackSingleXOR(hexString, scoreFile)
  elif EType == XORType.REPEATING:
    raise NotImplementedError
    #return crackRepeatingXOR(hexString)
  else:
    raise NotImplementedError

def crackSingleXOR(hexString, scoreFile):
  bestCandidate = Candidate(0, '', '')
  frequentLetters = {key.encode(): value for key, value in readJSON(scoreFile).items()}
  # We skip 0, since XORing against a bunch of 0s isn't going to do anything
  for i in range(1, 256):
    # The string interpolation will convert i into hex, and pad it with 0 if need be.
    possibleKey = f'{i:02x}' * (len(hexString) // 2)
    secret = fixedXOR(hexString, possibleKey)
    score = calculateScore(secret, frequentLetters)
    if score > bestCandidate.score:

  return bestCandidate

def calculateScore(secret, keyList):
  score = 0
  for key, value in keyList.items():
    score += (secret.count(key) * value)
  
  return round(score, 4)
