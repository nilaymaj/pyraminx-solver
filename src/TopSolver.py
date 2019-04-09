# Class file to solve the final three edges

import pUtils

class TopSolver:
  def __init__(self, edgeMap):
    self.layer = edgeMap.map[1]

  def isSolved(self):
    if self.layer[2][0] != 1 or self.layer[1][1] != 1:
      return 0
    if self.layer[2][1] != 2 or self.layer[0][0] != 2:
      return 0
    if self.layer[1][0] != 3 or self.layer[0][1] != 3:
      return 0
    return 1

  # Returns 0, if edge is solved, 1 if edge is flipped,
  # 2 if edge is not at right place
  def edgeStatus(self, posn):
    ids = [0, 1, 2]
    ids.remove(posn)
    if sum(ids)+2 != self.layer[posn][0] + self.layer[posn][1]:
      return 2
    else:
      # Flip the self.isOriented value and return it
      return (1+self.isOriented(posn))%2

  # Checks the three edges for a solved one,
  # and returns its position
  def findSolvedEdge(self):
    for i in range(3):
      if self.edgeStatus(i) == 0:
        # print("Solved edge found")
        return i
    return -1

  # Flips two edges in the class data
  # Used for solveCaseC() since it involves two steps
  def flipTwoEdges(self, posn):
    for i in range(3):
      edge = self.layer[i]
      if i != posn:
        edge[0], edge[1] = edge[1], edge[0]

  # Detects the sub-case if one edge is found to be solved.
  # Position of solved edge to be passed as argument
  def findSubCase(self, posn):
    ids = [0, 1, 2]
    ids.remove(posn)
    if self.edgeStatus(ids[0]) == 1:
      return 1
    elif self.edgeStatus(ids[0]) == 2:
      return 2
    return 0

  # Checks the layer to determine if the edges are
  # to be rotated clockwise or anticlockwise
  # To be used ONLY if no edges are already in their place.
  def detectRotationOrder(self):
    edge0 = self.layer[0]
    sum0 = sum(edge0)
    if sum0 == 4:
      return 1
    elif sum0 == 3:
      return -1
    return 0

  # Once determined that rotation will solve the pyraminx,
  # use this method to get the final rotation algo
  def rotateSolve(self):
    order = self.detectRotationOrder()
    if not order:
      print("detectRotationOrder() rule disobeyed.")
    elif order == 1:
      return ["R", "U'", "R'", "U'", "R", "U'", "R'"]
    else:
      return ["R", "U", "R'", "U", "R", "U", "R'"]

  # Determines if given edge is correctly oriented,
  # even if its not at right place
  def isOriented(self, posn):
    edge = self.layer[posn]
    diff = edge[1] - edge[0]
    if diff == 1 or diff == -2:
      return 1
    else: return 0

  # Get how many stickers (0, 1, 2) are matching up with faces
  def stickersMatching(self, posn):
    edge = self.layer[posn]
    if posn == 1:
      match1 = 1 if (edge[0] == 3) else 0
      match2 = 1 if (edge[1] == 1) else 0
    elif posn == 2:
      match1 = 1 if (edge[0] == 1) else 0
      match2 = 1 if (edge[1] == 2) else 0
    else:
      match1 = 1 if (edge[0] == 2) else 0
      match2 = 1 if (edge[1] == 3) else 0
    # print(f"stickersMatching({posn}) returns {match1 + match2}")
    return match1 + match2

  # Below methods are for checking each case
  # Note that subsequent cases should be checked only when
  # previous cases are eliminated
  def checkCaseA(self):
    return self.isSolved()
  def checkCaseB(self):
    ans = self.findSolvedEdge()
    if ans == -1:
      return 0, 0
    else:
      return 1, ans
  def checkCaseC(self):
    sumScores = 0
    for i in range(3):
      sumScores += self.stickersMatching(i)
    if sumScores == 2:
      return 1
    return 0
  def checkCaseD(self):
    for i in range(3):
      if self.edgeStatus(i) != 2:
        return 0
    return 1

  def solveCaseB(self):
    posn = self.findSolvedEdge()
    fullRots = 0
    if posn == 0:
      fullRots = 1
    elif posn == 2:
      fullRots = -1
    algo = ["F", "U'", "F'", "U", "F'", "L", "F", "L'"]
    algo = pUtils.modifyAlgoForOrientation(algo, fullRots)
    return algo
  def solveCaseC(self):
    brokenEdge = 0
    for i in range(3):
      if self.stickersMatching(i) == 0:
        brokenEdge = i
        break
    fullRots = 0
    if brokenEdge == 0:
      fullRots = 1
    elif brokenEdge == 2:
      fullRots = -1
    algo1 = ["L", "F'", "L'", "F", "U'", "F", "U", "F'"]
    algo1 = pUtils.modifyAlgoForOrientation(algo1, fullRots)
    self.flipTwoEdges(brokenEdge)
    algo2 = self.solveCaseD()
    return algo1 + algo2
  def solveCaseD(self):
    return self.rotateSolve()

  # Solve the last three edges!
  def solve(self):
    # print(self.layer)
    if self.checkCaseA():
      # print("Case A detected")
      return []
    if self.checkCaseB()[0]:
      # print("Case B detected")
      return self.solveCaseB()
    if self.checkCaseC():
      # print("Case C detected")
      return self.solveCaseC()
    if self.checkCaseD():
      # print("Case D detected")
      return self.solveCaseD()