# Encapsulates the various solver classes for each step

from src.CentreSolver import CentreSolver
from src.LayerSolver import LayerSolver
from src.TopSolver import TopSolver
from src import pUtils
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
