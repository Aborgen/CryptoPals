
# If the provided lists are not the same length,
# the longer will be truncated to match the shorter.
def normalizeListSize(aList, bList):
  if len(aList) == len(bList):
    return
  # Ensure that aList is the longer of the two lists
  if len(aList) < len(bList):
    aList, bList = bList, aList

  aList = aList[0:len(bList) - 1]
