
# We are interested in knowing--when we compare the two bytes objects, byte for byte--how many
# bits are different from each other. After XORing two bytes, counting all the ones will give us this answer.
def hammingDistance(aBytes, bBytes):
  differences = [bin(aByte ^ bByte).count('1') for aByte, bByte in zip(aBytes, bBytes)]
  return sum(differences)
