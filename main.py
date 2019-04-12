from src import pUtils, cli
from src.PyraminxSolver import PyraminxSolver
from src import OptimalSolver
from src.Pyraminx import Pyraminx


def welcome():
  print('''

  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
              Welcome to the Pyraminx Solver
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  How to use the Pyraminx Solver:
  #1: Choose how you want to input the state of your pyraminx
  #2: Choose if you want an intuitive solution or an optimal
      solution
  #3: Get the required algorithm.
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ''')


def getFaceWiseInput():
  print("You have chosen to input face-wise configuration of the pyraminx.")
  print("Enter the pyraminx configuration: ")
  matrix = []
  for i in range(4):
    faceStr = input()
    face = [int(faceStr[j]) for j in range(9)]
    matrix.append(face)
  pyraminx = Pyraminx(matrix[0], matrix[1], matrix[2], matrix[3])
  return pyraminx


def getSolverMode():
  print('''

Now, would you want an intuitive solution (where you can see the tips, centres
and edges solving up like a normal human solves) or an optimal solution (that
takes time, sometimes upto 2 minutes, but gives a really short solution)?

    1. An intuitive solution
    2. An optimal solution

  ''')
  option = int(input("Make your choice: "))
  return option


def getScrambleInput():
  scramble = input("Enter the scramble: ")
  scramble = scramble.split()
  return pUtils.scramble(scramble)


def getInputMode():
  print('''
  There are two ways you can provide the state of your scrambled pyraminx.
  You can find detailed instructions for input in 'howto.pdf'.

    1: Enter the face-wise, piece-wise color configuration
    2: Enter the scramble algorithm

  ''')
  while True:
    option = int(input("Enter your choice (1 or 2): "))
    if option in (1, 2):
      return option
    else:
      print("God, what has happened to people nowadays...")
      print("Okay, let's try this again. Pay attention.")


def main():
  welcome()
  inputOpt = getInputMode()
  if inputOpt == 1:
    pyraminx = getFaceWiseInput()
  else:
    pyraminx = getScrambleInput()

  try:
    pyraminx = pUtils.fixColors(pyraminx)
  except:
    print("That's not a valid configuration. Aborting.")
    input()
    return

  # Check if configuration is valid
  if inputOpt == 1:
    isValid = pUtils.checkIfValidConfig(pyraminx)
    if isValid == 0:
      print("That's not a valid configuration. Aborting.")
      input()
      return

  solverOpt = getSolverMode()

  if solverOpt == 1:
    pSolver = PyraminxSolver(pyraminx)
    algo = pSolver.solve()
  else:
    print("Solving. It may take up to 2-3 minutes.")
    algo = OptimalSolver.solve(pyraminx)

  # Printing the algo
  algo = pUtils.simplifyAlgo(algo)
  if algo:
    print("The required algorithm: ", end='')
    cli.printAlgo(algo)
  else:
    print("That configuration is already a solved one.")
  # print("Satisfied? Yeah, you're welcome.")
  input()
  return


if __name__ == "__main__":
  main()
