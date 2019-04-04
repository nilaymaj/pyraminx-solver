# Main entry point for the PyraminxSolver project

import cli, copy, pUtils
from PyraminxSolver import PyraminxSolver

def main():
  print("Welcome to the PyraminxSolver Project\n")

  # Load pyraminx configuration from file
  # pyraminx = cli.getFromFile("pyrConfig.txt")

  # Take config input from console
  # pyraminx = cli.inputState()

  # Scramble pyraminx from file
  # pyraminx = cli.scramblePyraminx("scramble.txt")

  # Generate random scramble
  scramble = pUtils.generateScramble(15)
  print("Scramble: ", end='')
  cli.printAlgo(scramble)
  pyraminx = pUtils.scramble(scramble)

  origPyraminx = copy.deepcopy(pyraminx)
  solver = PyraminxSolver(pyraminx)
  algo = solver.solve()
  # pyraminx = pUtils.fixColors(pyraminx)
  # cSolver = CentreSolver(pyraminx)
  # cli.printPyraminx(cSolver.pyraminx)
  # print()
  #
  # algo1 = cSolver.solveTips()
  # print("TIPS SOLVED")
  # # cli.printPyraminx(cSolver.pyraminx)
  # # print()
  #
  # algo2 = cSolver.solveCentres()
  # print("CENTRES SOLVED")
  # # cli.printPyraminx(cSolver.pyraminx)
  # print()
  #
  # lSolver = LayerSolver(cSolver.pyraminx)
  # algo3 = lSolver.solveLayer()
  #
  # edgeMap = lSolver.edgeMap
  # tSolver = TopSolver(edgeMap)
  # algo4 = tSolver.solve()
  #
  # cli.printAlgo(algo1 + algo2)
  # cli.printAlgo(algo3)
  # cli.printAlgo(algo4)
  # isSolved = lSolver.bottomLayerSolved()
  # simpleAlgo = pUtils.simplifyAlgo(algo2 + algo3 + algo4)
  # print("Simple algo:")
  # cli.printAlgo(simpleAlgo)
  # isSolved = pUtils.checkSolution(origPyraminx, algo1 + algo2 + algo3 + algo4)
  print("Solution algorithm:")
  cli.printAlgo(algo)
  isSolved = pUtils.checkSolution(origPyraminx, algo)
  print("WORKS?: " + str(isSolved))

if __name__ == "__main__":
  main()
