from initChallenge import checkResult, getArgs, getFilename, getData
from modules.crypto.crypto import repeatingXOR

def repeating_XOR():
  # Set up
  args = getArgs()
  challengeData = getData()[getFilename(__file__)]
  if args.input:
    challengeData['value'] = args.input[0]

  if args.key:
    challengeData['key'] = args.key

  # Complete challenge
  output = repeatingXOR(challengeData['value'], challengeData['key']) 
  challengeData['output'] = output
  return challengeData

if __name__ == '__main__':
  data = repeating_XOR()
  print(data['description'] + "\n----------")
  print(f"Input:\n{data['value']}")
  print(f"Key:\t{data['key']}")
  checkResult(data['output'].hex(), data['expectedOutput'])

