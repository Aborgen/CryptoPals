import argparse
import json
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

def getArgs():
  parser = argparse.ArgumentParser('Each challenege is set up to run on it\'s own, using value(s) located in data.json. This can be changed by using the --input flag')
  parser.add_argument('-i', '--input', help = 'The text to be processed', type = str)
  args = parser.parse_args()
  return args

# It is assumed that any callers will pass in __file__ (file.py).
def getFilename(filename):
  return os.path.splitext(filename)[0]

def jsonParse():
  data = {}
  with open('data.json') as jsonData:
    data = json.load(jsonData)

  return data

def checkResult(actualOutput, expectedOutput):
  if (actualOutput != expectedOutput):
    challengeMismatch(actualOutput, expectedOutput)
  else:
    print(f"Output:\t{actualOutput}") 

def challengeMismatch(actualOutput, expectedOutput):
  print("~~~~! Mismatch !~~~~~")
  print("Expected: {}".format(expectedOutput)) 
  print("Actual:   {}".format(actualOutput)) 
  print("~~~~!          !~~~~~")
