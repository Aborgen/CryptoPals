from initChallenge import checkResult, getArgs, getFilename, getData
from modules.crypto.crypto import Action, CBC_AES128
from modules.utils.file import readFile
from modules.utils.convert import b642bytes

def decrypt_CBC_AES128():
  # Set up
  args = getArgs()
  challengeData = getData()[getFilename(__file__)]
  if args.input:
    challengeData['value'] = args.input[0]

  if args.key:
    challengeData['key'] = args.key

  # Complete challenge
  f = ''.join(readFile(challengeData['value']))
  b = b642bytes(f)
  VI = bytes([0] * 16)
  output = CBC_AES128(challengeData['key'], b, VI, Action.DECRYPT)

  challengeData['output'] = output
  challengeData['bytes'] = len(b)
  return challengeData

if __name__ == '__main__':
  data = decrypt_CBC_AES128()
  print(data['description'] + "\n----------")
  print(f"Decoding {data['bytes']} bytes from {data['value']}")
  print(f"Key: {data['key']}")
  print(data['output'].decode())
