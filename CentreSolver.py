# Class file for the CentreSolver class
# Solves the tips and centres, and then returns the edge position data
# of the pyraminx.

class CentreSolver:

  def __init__(self, pyraminx):
    self.pyraminx = pyraminx
    self.algo = []

  # Find difference of color ids of each tip with the corresponding centre.
  # Rotate each tip accordingly.
  def solveTips(self):
    algo = []

    # Solve the top tip
    diff = self.pyraminx.red_face[0][0] - self.pyraminx.red_face[1][0]
    if diff == 1 or diff == -2:
      algo.append("u")
    elif diff == 2 or diff == -1:
      algo.append("u'")

    # Solve the front tip
    diff = self.pyraminx.red_face[0][1] - self.pyraminx.red_face[1][1]
    if diff == 1 or diff == 2 or diff == -3:
      algo.append("f'")
    elif diff == 3 or diff == -1 or diff == -2:
      algo.append("f")

    # Solve the right tip
    diff = self.pyraminx.red_face[0][2] - self.pyraminx.red_face[1][2]
    if diff == 2 or diff == 1 or diff == -3:
      algo.append("r")
    elif diff == 3 or diff == -1 or diff == -2:
      algo.append("r'")

    # Solve the left tip
    diff = self.pyraminx.green_face[0][2] - self.pyraminx.green_face[1][2]
    if diff == 1 or diff == -2:
      algo.append("l'")
    elif diff == 2 or diff == -1:
      algo.append("l")
  
    # Apply the algorithm to the pyraminx
    self.pyraminx.applyAlgo(algo)
    return algo

  # Method same as solveTips, except now we are comparing
  # with the base colour of the face rather than color of some piece.
  # That's why the 1's and the 2 in diff. 1 for red, 2 for green
  def solveCentres(self):
    algo = []

    # Solve the top centre
    diff = self.pyraminx.red_face[0][0] - 1
    if diff == 1:
      algo.append("U")
    elif diff == 2:
      algo.append("U'")

    # Solve the front centre
    diff = self.pyraminx.red_face[0][1] - 1
    if diff == 1:
      algo.append("F'")
    elif diff == 3:
      algo.append("F")

    # Solve the right centre
    diff = self.pyraminx.red_face[0][2] - 1
    if diff == 2:
      algo.append("R")
    elif diff == 3:
      algo.append("R'")

    # Solve the left centre
    # print("FROM CSOLVER L-STEP: " + str(self.pyraminx.green_face[0][2]))
    diff = self.pyraminx.green_face[0][2] - 2
    if diff == 1:
      algo.append("L'")
    elif diff == 2:
      algo.append("L")
    # print("FROM CSOLVER L-STEP: " + str(diff))
    # Apply the algorithm to the pyraminx
    self.pyraminx.applyAlgo(algo)
    return algo
