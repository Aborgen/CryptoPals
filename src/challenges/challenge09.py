from initChallenge import checkResult, getArgs, getFilename, getData
from modules.crypto.crypto import pad
def pad_with_PKCS7():
  # Set up
  args = getArgs()
  challengeData = getData()[getFilename(__file__)]
  if args.input:
    challengeData['value'] = args.input[0]

  # Complete challenge
  output = pad(challengeData['value'], challengeData['length'])
  challengeData['output'] = output
  return challengeData

if __name__ == '__main__':
  data = pad_with_PKCS7()
  print(data['description'] + "\n----------")
  print(f"Padding to {data['length']} bytes...")
  print(f"Input:\t{data['value'].encode()}")
  checkResult(data['output'], data['expectedOutput'].encode())
