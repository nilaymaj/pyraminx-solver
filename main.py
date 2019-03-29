# Main entry point for the PyraminxSolver project
import cli
from Pyraminx import Pyraminx
from CentreSolver import CentreSolver

def main():
  print("Welcome to the PyraminxSolver Project\n")
  pyraminx = cli.inputState()
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

if __name__ == "__main__":
  main()
