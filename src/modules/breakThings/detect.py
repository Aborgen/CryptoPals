from typing import NamedTuple
from . import initBreak
from ..utils.collections import countDuplication
from ..utils.compare import isBytes
from ..utils.convert import toBytes

class PossibleEncryption(NamedTuple):
  ciphertext: str 
  repetition: int

def maybeECB_AES128(ciphertext):
  if not isBytes(ciphertext):
    ciphertext = toBytes(ciphertext)

  ECB = 16
  blocks = [ciphertext[i:i + ECB] for i in range(0, len(ciphertext), ECB)]
  repetition = countDuplication(blocks)
  if repetition == 0:
    return False

  return PossibleEncryption(ciphertext, repetition)
