from . import initBreak
from enum import Enum
from modules.crypto.crypto import fixedXOR
from modules.utils.file import readFile
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
  frequentLetters = [x.encode() for x in readFile(scoreFile)[0].split(', ')]
  bestCandidate = Candidate(0, '', '')
  # We skip 0, since XORing against a bunch of 0s isn't going to do anything
  for i in range(1, 256):
    # The string interpolation will convert i into hex, and pad it with 0 if need be.
    possibleKey = f'{i:02x}' * (len(hexString) // 2)
    secret = fixedXOR(hexString, possibleKey)
    score = calculateScore(secret, frequentLetters)
    if score > bestCandidate.score:
      bestCandidate = Candidate(score, possibleKey, secret)

  return bestCandidate

def calculateScore(secret, keyList):
  score = 0
  for key in keyList:
    score += secret.count(key)
  
  return score
