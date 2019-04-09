# import OptimalSolver
import pUtils, cli, copy
import Pyraminx

def main():
  solvedP = pUtils.solvedPyraminx()
  currP = solvedP.copy()
  currP.applyAlgo(["U"])
  cli.printPyraminx(currP)
  print()
  cli.printPyraminx(solvedP)

if __name__ == "__main__":
  main()