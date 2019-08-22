from initChallenge import checkResult, getArgs, jsonParse
from modules.utils.convert import hex2b64
# Convert hex to base64

def convert_hex_to_base64():
  # Set up
  args = getArgs()
  challengeData = jsonParse()['challenge01']
  value = ''
  # If user is supplying value to be converted
  if args.input:
    value = args.input
  else:
    value = challengeData['value']

  output = hex2b64(value)
  challengeData['output'] = output.decode()
  challengeData['value'] = value
  return challengeData

if __name__ == '__main__':
  data = convert_hex_to_base64()
  print(data['description'] + "\n----------")
  print(f"Input:\t{data['value']}")
  checkResult(data['output'], data['expectedOutput'])
