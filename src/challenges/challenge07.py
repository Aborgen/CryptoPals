from initChallenge import checkResult, getArgs, getFilename, getData
from modules.utils.convert import b642bytes
from modules.crypto.crypto import Action, ECB_AES128
from modules.utils.file import readFile

def decrypt_AES():
  # Set up
  args = getArgs()
  challengeData = getData()[getFilename(__file__)]
  if args.input:
    challengeData['value'] = args.input[0]

  if args.key:
    challengeData['key'] = args.key

  # Complete challenge
  key = challengeData['key']
  f = readFile(challengeData['value'])
  ciphertext = b642bytes(''.join(f))
  secret = ECB_AES128(key, ciphertext, Action.DECRYPT)
  
  challengeData['secret'] = secret
  challengeData['bytes'] = len(ciphertext)
  return challengeData

if __name__ == '__main__':
  data = decrypt_AES()
  print(data['description'] + "\n----------")
  print(f"Decoding {data['bytes']} bytes from {data['value']}")
  print(f"Key: {data['key']}")
  print(data['secret'].decode())
