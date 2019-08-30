from initChallenge import checkResult, getArgs, getFilename, getData
from modules.breakThings.crack import Candidate, crackXOR, XORType

def crack_single_XOR(scoreFile):
  # Set up
  args = getArgs()
  challengeData = getData()[getFilename(__file__)]
  if args.input:
    challengeData['values'] = args.input

  # Complete challenge
  candidate = crackXOR(challengeData['values'][0], scoreFile, XORType.SINGLE)
  challengeData['candidate'] = candidate
  return challengeData

if __name__ == '__main__':
  scoreFile = 'resources/en_characterFrequency.txt'
  data = crack_single_XOR(scoreFile)
  candidate = data['candidate']
  print(data['description'] + "\n----------")
  print(f"Input:\t{data['values'][0]}")
  goodResult = checkResult(candidate.secret.decode(), data['expectedOutput'])
  if goodResult:
    print(f"Key:\t{candidate.key}")
    print(f"Score:\t{candidate.score}")
    
