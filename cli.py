# Methods for taking command-line input and output

from Pyraminx import Pyraminx

# TODO: Create README.md, must include the CLI input instructions.
def printInputInstructions():
  print('''\n
  ----------INSTRUCTIONS FOR INPUTTING PYRAMINX STATE------------
  1. Input should be four lines, one for each face.
  2. The order is RED - GREEN - BLUE - YELLOW
  3. The colours are represented by RED: 1, GREEN: 2, BLUE: 3, YELLOW: 4
  4. Instructions on how to fill each face are in README.md.\n
  ENTER THE STATE OF YOUR PYRAMINX:\n
  ''')

def inputState():
  printInputInstructions()
  matrix = []
  for i in range(4):
    faceStr = input()
    face = [int(faceStr[j]) for j in range(9)]
    matrix.append(face)
  pyraminx = Pyraminx(matrix[0], matrix[1], matrix[2], matrix[3])
  return pyraminx

def printState(pyraminx):
  print(pyraminx.red_face)
  print(pyraminx.green_face)
  print(pyraminx.blue_face)
  print(pyraminx.yellow_face)

def toNumArray(string):
  array = []
  for char in string:
    if char != '\n':
      array.append(int(char))
  return array

def getFromFile(filename):
  file = open(filename, "r")
  faces = file.readlines()
  for i in range(4):
    faces[i] = toNumArray(faces[i])
  pyraminx = Pyraminx(faces[0], faces[1], faces[2], faces[3])
  file.close()
  return pyraminx

def printAlgo(algo):
  for step in algo:
    print(step, end=" ")
  print()

