from initChallenge import checkResult, getArgs, getFilename, getData
from modules.breakThings.detect import PossibleEncryption, maybeECB_AES128
from modules.crypto.crypto import Action, ECB_AES128
from modules.utils.convert import bytes2hex
from modules.utils.file import readFile

def decrypt_AES():
  # Set up
  args = getArgs()
  challengeData = getData()[getFilename(__file__)]
  if args.input:
    challengeData['value'] = args.input[0]

  # Complete challenge
  cipherBlocks = readFile(challengeData['value'])
  bestGuess = PossibleEncryption('', 0)
  for block in cipherBlocks:
    guess = maybeECB_AES128(block)
    if guess and guess.repetition > bestGuess.repetition:
      bestGuess = guess
  
  challengeData['guess'] = bestGuess
  challengeData['blockNumber'] = len(cipherBlocks)
  return challengeData

if __name__ == '__main__':
  data = decrypt_AES()
  print(data['description'] + "\n----------")
  print(f"Any encryption within {data['blockNumber']} blocks from {data['value']}?")

  ciphertext, repetition = data['guess']
  ciphertext = bytes2hex(ciphertext)
  if ciphertext == '':
    print("No.")
  else:
    print(f"Possible encrypted text found with a total of {repetition} repeat 16-byte chunks!\n{ciphertext}")
