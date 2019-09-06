from initChallenge import checkResult, getArgs, getFilename, getData
from modules.breakThings.crack import crackXOR, XORType
from modules.crypto.crypto import repeatingXOR
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
  key = crackXOR(hexString, args.dictionaryFile, XORType.REPEATING).hex()
  secret = repeatingXOR(hexString, key)

  challengeData['key'] = key
  challengeData['secret'] = secret
  challengeData['lines'] = len(f)
  return challengeData

if __name__ == '__main__':
  data = repeating_XOR()
  key = bytes.fromhex(data['key']).decode()
  print(data['description'] + "\n----------")
  print(f"Decoding {data['lines']} lines from {data['value']}")
  print(f"Key: {key}\n")
  print(data['secret'].decode())
