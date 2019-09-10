from .modify import pad

# If the provided lists are not the same length,
# the longer will be truncated to match the shorter.
def normalizeListSize(aList, bList):
  aLength, bLength = len(aList), len(bList)
  if aLength == bLength:
    return
  elif aLength > bLength:
    del aList[bLength - 1:]
  else:
    del bList[aLength - 1:]

# One liner from Denis Otkidach (https://stackoverflow.com/a/1541827)
# If there are any duplicates, the length of the set will be less than the length of the list.
def anyDuplication(valueList):
  return len(valueList) != len(set(valueList))

def countDuplication(valueList):
  return len(valueList) - len(set(valueList))

def splitToBlocks(text, length):
  # Ensure text can be broken up into equal length blocks
  if len(text) % length != 0:
    text = pad(text) 

  return [text[i:i + length] for i in range(0, len(text), length)]

