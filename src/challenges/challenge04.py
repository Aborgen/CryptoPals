from initChallenge import checkResult, getArgs, getFilename, getData
from modules.breakThings.crack import Candidate, crackXOR, XORType
from modules.utils.file import readFile

def identify_single_XOR():
  # Set up
  args = getArgs()
  challengeData = getData()[getFilename(__file__)]
  if args.input:
    challengeData['values'] = args.input

  if not args.dictionaryFile:
    raise Exception('This challenge must be provided a json data file with -d')

  # Complete challenge
  hexStrings = readFile(challengeData['values'][0])
  scoreBoard = [Candidate(0, b'', b'', b'')] * (args.candidates if args.candidates else 1)
  for hexString in hexStrings:
    candidate = crackXOR(hexString, args.dictionaryFile, XORType.SINGLE)
    for idx, finalist in enumerate(scoreBoard):
      if candidate.score > finalist.score:
        scoreBoard[idx] = candidate
        break

  challengeData['stringNumber'] = len(hexStrings)
  challengeData['scoreBoard'] = scoreBoard
  return challengeData
  
if __name__ == '__main__':
  data = identify_single_XOR()
  scoreBoard = data['scoreBoard']
  print(data['description'] + "\n----------")
  print(f"{data['values'][0]}: {data['stringNumber']} strings tried")

  candidateCount = len(scoreBoard)
  if candidateCount == 0:
    print("There are no likely solutions! Maybe something went wrong?")
  else:
    if candidateCount == 1:
      print("This is the most likely solution:")
    else:
      print(f"These are the {len(scoreBoard)} most likely solutions:")

    print('\n', end = '')
    for idx, finalist in enumerate(scoreBoard, start=1):
      print(f"{idx})")
      print(f"Score:\t{finalist.score}")
      print(f"Key:\t{finalist.key.hex()}")
      print(f"Base:\t{finalist.base.hex()}")
      print(f"Secret:\t{finalist.secret.decode().rstrip()}")
      print("----------")
