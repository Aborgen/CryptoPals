from initChallenge import checkResult, getArgs, getFilename, jsonParse
from modules.crypto.crypto import fixedXOR
from modules.utils.convert import bytes2hex

def fixed_XOR():
  # Set up
  args = getArgs()
  challengeData = jsonParse()[getFilename(__file__)]
  if args.input:
    challengeData['values'] = args.input

  # Complete challenge
  values = challengeData['values']
  output = fixedXOR(values[0], values[1])
  challengeData['output'] = bytes2hex(output)
  return challengeData

if __name__ == '__main__':
  data = fixed_XOR()
  print(data['description'] + "\n----------")
  print(f"a:\t{data['values'][0]}")
  print(f"b:\t{data['values'][1]}")
  checkResult(data['output'], data['expectedOutput'])
