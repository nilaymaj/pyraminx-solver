# This is for testing the solver. The solver's final exam, basically.

from src import cli, pUtils
from src.PyraminxSolver import PyraminxSolver
# from src import OptimalSolver
import copy

def main():
  print("Welcome to the PyraminxSolver Testing Ground\n")
  print("Starting the infinite test: \n")
  numDone = 0
  while True:
    scramble = pUtils.generateScramble(15)
    pyraminx = pUtils.scramble(scramble)

    origPyraminx = copy.deepcopy(pyraminx)
    solver = PyraminxSolver(pyraminx)
    algo = solver.solve()
    # algo = OptimalSolver.solve(pyraminx)

    isSolved = pUtils.checkSolution(origPyraminx, algo)
    if isSolved:
      numDone += 1
      print(f"Successfully solved scramble #{numDone}")
    else:
      print(f"Failed on scramble #{numDone+1} given below:")
      cli.printAlgo(scramble)
      print("Aborted.")
      break

if __name__ == "__main__":
  main()