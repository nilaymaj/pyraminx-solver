# Main entry point for the PyraminxSolver project
import cli
# from Pyraminx import Pyraminx
from CentreSolver import CentreSolver
import pUtils

def main():
  print("Welcome to the PyraminxSolver Project\n")
  # pyraminx = cli.inputState()
  pyraminx = cli.getFromFile("pyrConfig.txt")
  print("---PYRAMINX READ FROM FILE---")
  pyraminx = pUtils.fixColors(pyraminx)
  cSolver = CentreSolver(pyraminx)
  cli.printState(cSolver.pyraminx)
  print()

  algo1 = cSolver.solveTips()
  print("After solving tips: ")
  cli.printState(cSolver.pyraminx)
  print()

  algo2 = cSolver.solveCentres()
  cli.printState(cSolver.pyraminx)
  print()

  cli.printAlgo(algo1 + algo2)
  # cSolver.pyraminx.fixFaces()
  # print("\n\nAFTER FIXING FACES\n")
  # cli.printState(cSolver.pyraminx)

if __name__ == "__main__":
  main()
