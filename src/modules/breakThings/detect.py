from typing import NamedTuple
from . import initBreak
from ..utils.collections import countDuplication, splitToBlocks
from ..utils.compare import isBytes
from ..utils.convert import toBytes

class PossibleEncryption(NamedTuple):
  ciphertext: str 
  repetition: int

def maybeECB_AES128(ciphertext):
  if not isBytes(ciphertext):
    ciphertext = toBytes(ciphertext)

  blocks = splitToBlocks(ciphertext, 16)
  repetition = countDuplication(blocks)
  if repetition == 0:
    return False

  return PossibleEncryption(ciphertext, repetition)
