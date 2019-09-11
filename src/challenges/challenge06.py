from initChallenge import getArgs, getFilename, getData
from modules.breakThings.crack import crackXOR, XORType
from modules.utils.convert import b642hex
from modules.utils.file import readFile

def repeating_XOR():
  # Set up
  args = getArgs()
  challengeData = getData()[getFilename(__file__)]
  if args.input:
    challengeData['value'] = args.input[0]

  if not args.dictionaryFile:
    raise Exception('This challenge must be provided a json data file with -d')

  # Complete challenge
  f = readFile(challengeData['value'])
  hexString = b642hex(''.join(f))
  candidate = crackXOR(hexString, args.dictionaryFile, XORType.REPEATING)

  challengeData['candidate'] = candidate
  challengeData['lines'] = len(f)
  return challengeData

if __name__ == '__main__':
  data = repeating_XOR()
  print(data['description'] + "\n----------")
  print(f"Decoding {data['lines']} lines from {data['value']}")
  print(f"Key: {data['candidate'].key.decode()}\n")
  print(data['candidate'].secret.decode())
