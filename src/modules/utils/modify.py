from itertools import cycle
from .compare import isBytes
from .convert import toBytes

def pad(text, length):
  if len(text) % length == 0:
    return text

  paddedText = _padBytes(text, length)
  return paddedText if isBytes(text) else paddedText.decode()

# This is an implementation of PKCS#7 padding
def _padBytes(text, length):
  if not isBytes(text):
    text = toBytes(text)

  missing = length - (len(text) % length)
  correctedLength = len(text) + missing
  return text.ljust(correctedLength, bytes([missing]))

# Text will be repeated until its length matches the provided length
# text = 'text', length = 10
# 'texttextte'
def repeatPerCharacter(text, length):
  c = cycle(text)
  repeatText = [next(c) for _ in range(length)]

  return bytes(repeatText) if isBytes(text) else ''.join(repeatText)
