from initChallenge import checkResult, getArgs, getFilename, getData
from modules.breakThings.crack import Candidate, crackXOR, XORType

def crack_single_XOR():
  # Set up
  args = getArgs()
  challengeData = getData()[getFilename(__file__)]
  if args.input:
    challengeData['values'] = args.input
  
  if not args.dictionaryFile:
    raise Exception('This challenge must be provided a json data file with -d')

  # Complete challenge
  candidate = crackXOR(challengeData['values'][0], args.dictionaryFile, XORType.SINGLE)
  challengeData['candidate'] = candidate
  return challengeData

if __name__ == '__main__':
  data = crack_single_XOR()
  candidate = data['candidate']
  print(data['description'] + "\n----------")
  print(f"Input:\t{data['values'][0]}")
  goodResult = checkResult(candidate.secret.decode(), data['expectedOutput'])
  if goodResult:
    print(f"Key:\t{candidate.key.hex()}")
    print(f"Score:\t{candidate.score}")
    
