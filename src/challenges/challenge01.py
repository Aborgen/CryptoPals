from initChallenge import checkResult, getArgs, getFilename, jsonParse
from modules.utils.convert import hex2b64
# Convert hex to base64

def convert_hex_to_base64():
  # Set up
  args = getArgs()
  challengeData = jsonParse()[getFilename(__file__)]
  if args.input:
    challengeData['values'] = args.input

  # Complete challenge
  value = challengeData['values'][0]
  output = hex2b64(value)
  challengeData['output'] = output.decode()
  return challengeData

if __name__ == '__main__':
  data = convert_hex_to_base64()
  print(data['description'] + "\n----------")
  print(f"Input:\t{data['values'][0]}")
  checkResult(data['output'], data['expectedOutput'])
