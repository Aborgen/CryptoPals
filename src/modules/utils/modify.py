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

