from initChallenge import checkResult, getArgs, getFilename, jsonParse
from modules.crypto.crypto import fixedXOR
from modules.utils.convert import bytes2hex

def fixed_XOR():
  # Set up
  args = getArgs()
  challengeData = jsonParse()[getFilename(__file__)]
  output = fixedXOR(challengeData['value01'], challengeData['value02'])
  challengeData['output'] = bytes2hex(output)
  return challengeData

if __name__ == '__main__':
  data = fixed_XOR()
  print(data['description'] + "\n----------")
  print(f"Input01:\t{data['value01']}")
  print(f"Input02:\t{data['value02']}")
  checkResult(data['output'], data['expectedOutput'])
