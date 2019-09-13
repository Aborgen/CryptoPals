from . import initBreak
from collections import deque
from enum import Enum
from itertools import combinations, compress
from math import inf as infinity
from modules.crypto.crypto import fixedXOR
from modules.utils.compare import encodedByUTF8, hammingDistance, isBytes, isHex
from modules.utils.convert import hex2bytes
from modules.utils.file import readJSON
from modules.utils.modify import repeatPerCharacter
from typing import NamedTuple

class XORType(Enum):
  SINGLE = 0
  REPEATING = 1

class Candidate(NamedTuple):
  score:  int
  key:    bytes
  base:   bytes
  secret: bytes

def crackXOR(byteObject, scoreFile, EType):
  if not isBytes(byteObject):
    byteObject = hex2bytes(byteObject) if isHex(byteObject) else byteObject.encode()

  if EType == XORType.SINGLE:
    return _crackSingleXOR(byteObject, scoreFile)
  elif EType == XORType.REPEATING:
    return _crackRepeatingXOR(byteObject, scoreFile, keySizeRange = (2, 40), blockNumber = 4)
  else:
    raise NotImplementedError

def _crackSingleXOR(byteObject, scoreFile):
  if not isBytes(byteObject):
    raise ValueError("Input must be a bytes object")

  frequentLetters = {key.encode(): value for key, value in readJSON(scoreFile).items()}
  bestCandidate = Candidate(0, b'', b'', b'')
  # We skip 0, since XORing against a bunch of 0s isn't going to do anything
  byteLength = len(byteObject)
  for i in range(1, 256):
    possibleKey = repeatPerCharacter(bytes([i]), byteLength)
    secret = fixedXOR(byteObject, possibleKey)
    score = calculateScore(secret, frequentLetters)
    if score > bestCandidate.score and encodedByUTF8(secret):
      bestCandidate = Candidate(score, possibleKey, byteObject, secret)

  return bestCandidate

def calculateScore(secret, keyList):
  score = 0
  for key, value in keyList.items():
    count = secret.count(key)
    score += (count * value) + count
  
  return round(score, 4)

def _crackRepeatingXOR(byteObject, scoreFile, keySizeRange, blockNumber):
  if not isBytes(byteObject):
    raise ValueError("Input must be a bytes object")

  rangeStart, rangeEnd = keySizeRange
  stringLength = len(byteObject)
  # We need at least two chunks of bytes with rangeEnd length.
  if rangeEnd > stringLength:
    rangeEnd = stringLength 

  bestDistance = infinity
  bestKeySize = 0
  for keySize in range(rangeStart, rangeEnd + 1):
    blockList = []
    for i in range(blockNumber):
      sliceStart = keySize * i
      sliceEnd = keySize * (i + 1)
      if sliceStart > stringLength - 1 or sliceEnd > stringLength:
        break

      b = byteObject[sliceStart:sliceEnd]
      blockList.append(b)
    
    distance = averageDistance(blockList, keySize)
    if distance < bestDistance:
      bestDistance = distance
      bestKeySize = keySize

  blocks = divideIntoBlocks(byteObject, bestKeySize)
  key = bytearray()
  for block in blocks:
    candidate = _crackSingleXOR(block, scoreFile)
    key.append(candidate.key[0])

  key = bytes(key)
  secret = fixedXOR(byteObject, repeatPerCharacter(key, len(byteObject)))
  return Candidate(-1, key, byteObject, secret)

def averageDistance(blockList, keySize):
  blockPairs = combinations(blockList, 2)
  distances = [hammingDistance(a, b) for a, b in blockPairs]
  return sum(distances) / keySize

# The intent of this function is to create n blocks consisting of every n bytes
# for a total of len(bytes) / n elements.
#
# The below diagram demonstrates what the purpose of the mask is.
# If we had 18 bytes and we wanted 3 blocks comprised of every 3 of them:
# (Arranged for readability. In reality, the 1s and 0s are Trues and Falses within a flat deque)
# Block 0
#   1 0 0  1 0 0
#   1 0 0  1 0 0
#   1 0 0  1 0 0
#
# Block 1
#   0 1 0  0 1 0
#   0 1 0  0 1 0
#   0 1 0  0 1 0
#
# Block 2
#   0 0 1  0 0 1
#   0 0 1  0 0 1
#   0 0 1  0 0 1
#
# As can be seen above, each block consists of 18 / 3, or 6, elements.
def divideIntoBlocks(byteObject, blockNumber):
  # Fill with null bytes to ensure each block will have the same length, if necessary
  if len(byteObject) % blockNumber != 0:
    fixedLength = len(byteObject) + (blockNumber - (len(byteObject) % blockNumber))
    byteObject = byteObject.ljust(fixedLength, b'\00')

  mask = deque(True if idx % blockNumber == 0 else False for idx in range(len(byteObject)))
  blocks = []
  for _ in range(blockNumber):
    # Compress returns only bytes whose corresponding mask index houses a truthy value
    block = bytes(compress(byteObject, mask))
    blocks.append(block)
    # This idiom shifts all True values to the right, as in the diagram above
    mask.appendleft(False)
    mask.pop()

  return blocks

