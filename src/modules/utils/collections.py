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
