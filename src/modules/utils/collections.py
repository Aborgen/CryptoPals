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
