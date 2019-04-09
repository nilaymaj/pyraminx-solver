# from Pyraminx import Pyraminx
import pUtils, cli
from CentreSolver import CentreSolver

moves = ["U", "F", "R", "L"]

algorithms = []

def dfsearch(pyraminx):
  layer = []
  solvedP = pUtils.solvedPyraminx()
  if pyraminx.eq(solvedP):
    algorithms.append([])
    return
  layer.append((pyraminx, []))
  while True:
    newLayer = []
    for p in layer:
      newLayer += generateNeighbors(p[0], p[1])
    layer = newLayer
    for p in layer:
      if p[0].eq(solvedP):
        return p[1]
    if len(layer[0][1]) >= 14:
      print("No solution found. Sorry.")
      return []
  print("HOW DID WE REACH THE END OF THIS FUNCTION??!")

def generateNeighbors(pyraminx, scramble):
  neighbors = []
  for move in moves:
    neighbors.append((pyraminx.makeMove(move), scramble + [move]))
  return neighbors


def solveP(pyraminx, algo):
  solvedP = pUtils.solvedPyraminx()
  currP = pyraminx.copy()
  currP.applyAlgo(algo)
  if currP.eq(solvedP):
    algorithms.append(algo)
    return 1
  if len(algo) >= 12:
    return 0
  else:
    for moveId in moves:
      # print("Making move: " + moveId)
      newAlgo = algo[:]
      newAlgo.append(moveId)
      # cli.printAlgo(newAlgo)
      # cli.printPyraminx(pyraminx)
      solved = solveP(pyraminx, newAlgo)
      if solved:
        # print("RETURNED!!")
        return 1
    return 0

def solve(pyraminx):
  cSolver = CentreSolver(pyraminx.copy())
  tipAlgo = cSolver.solveTips()
  pyraminx.applyAlgo(tipAlgo)
  # solveP(pyraminx, [])
  algo = dfsearch(pyraminx)
  # return tipAlgo + pUtils.simplifyAlgo(algorithms[0])
  return tipAlgo + pUtils.simplifyAlgo(algo)


