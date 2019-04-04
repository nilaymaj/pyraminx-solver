# Encapsulates the various solver classes for each step

from CentreSolver import CentreSolver
from LayerSolver import LayerSolver
from TopSolver import TopSolver
import pUtils
import copy

class PyraminxSolver:
  def __init__(self, pyraminx):
    self.pyraminx = pUtils.fixColors(pyraminx)

  def solve(self):
    solution = []

    # Solve tips and centres
    cSolver = CentreSolver(self.pyraminx)
    solution += cSolver.solveTips()
    solution += cSolver.solveCentres()
    self.pyraminx = copy.deepcopy(cSolver.pyraminx)

    # Solve bottom layer
    lSolver = LayerSolver(self.pyraminx)
    solution += lSolver.solveLayer()
    edgeMap = lSolver.edgeMap

    # Solve top edges
    tSolver = TopSolver(edgeMap)
    solution += tSolver.solve()

    return solution
