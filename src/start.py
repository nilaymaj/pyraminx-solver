# Main entry point for the PyraminxSolver project

from src import cli, pUtils
from src.PyraminxSolver import PyraminxSolver
from src import OptimalSolver
import copy

def main():
  print("Welcome to the PyraminxSolver Project\n")

  # Load pyraminx configuration from file
  # pyraminx = cli.getFromFile("pyrConfig.txt")

  # Take config input from console
  pyraminx = cli.inputState()

  # Scramble pyraminx from file
  # pyraminx = cli.scramblePyraminx("scramble.txt")

  # Generate random scramble
  # scramble = pUtils.generateScramble(15)
  # print("Scramble: ", end='')
  # cli.printAlgo(scramble)
  # pyraminx = pUtils.scramble(scramble)
 # --------------------------------------

  pUtils.fixColors(pyraminx)
  origPyraminx = copy.deepcopy(pyraminx)

  # Optimal Solver
  # isValid = pUtils.checkIfValidConfig(pyraminx)
  # if isValid:
  #   algo = OptimalSolver.solve(pyraminx)
  # else:
  #   algo = []

  # Intuitive Solver
  try:
    solver = PyraminxSolver(pyraminx)
    algo = solver.solve()
    algo = pUtils.simplifyAlgo(algo)
  except:
    algo = []

  isSolved = pUtils.checkSolution(origPyraminx, algo)
  if isSolved:
    print("Solution algorithm:")
    cli.printAlgo(algo)
  else:
    print("The given configuration seems to be invalid.")

if __name__ == "__main__":
  main()
