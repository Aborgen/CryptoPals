import json

def readJSON(filename):
  data = {}
  with open(filename) as jsonData:
    data = json.load(jsonData)

  return data
