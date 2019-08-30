import json

def readJSON(filename):
  data = {}
  with open(filename) as jsonData:
    data = json.load(jsonData, parse_float=float)
  
  if '//' in data:
    del data['//']

  return data

def readFile(filename):
  lines = []
  with open(filename) as f:
    for line in f:
      # It is a comment, ignore it.
      if line.startswith('#'):
        continue

      lines.append(line)

  # Remove unnecessary whitespace
  return [line.rstrip() for line in lines]
