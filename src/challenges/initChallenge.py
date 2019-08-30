import argparse
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from modules.utils.file import readJSON

def getArgs():
  parser = argparse.ArgumentParser('Each challenege is set up to run on it\'s own, using value(s) located in data.json. This can be changed by using the --input flag')
  parser.add_argument('-i', '--input', nargs = '*', help = 'The text to be processed. Accepts 0 to many inputs.', type = str)
  parser.add_argument('-d', '--dictionaryFile', help = 'For challenges that need the contects of some file to complete', type = str)
  parser.add_argument('-c', '--candidates', help = 'For challenges that need to guess, output information for n of the best guesses', type = int, default = 1)
  args = parser.parse_args()
  return args

# It is assumed that any callers will pass in __file__ (file.py).
def getFilename(filename):
  return os.path.splitext(filename)[0]

def getData():
  filename = './resources/data.json'
  return readJSON(filename)

def checkResult(actualOutput, expectedOutput):
  if (actualOutput != expectedOutput):
    challengeMismatch(actualOutput, expectedOutput)
    return False

  print(f"Output:\t{actualOutput}") 
  return True

def challengeMismatch(actualOutput, expectedOutput):
  print("~~~~! Mismatch !~~~~~")
  print("Expected: {}".format(expectedOutput)) 
  print("Actual:   {}".format(actualOutput)) 
  print("~~~~!          !~~~~~")
