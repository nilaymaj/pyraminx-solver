# Class file to solve one layer of edges
# To be used after centres are solved

from EdgeMap import EdgeMap
import pUtils
import cli

class LayerSolver:
  def __init__(self, pyraminx):
    self.edgeMap = EdgeMap(pyraminx)
    self.pyraminx = pyraminx
    # TODO: Try to remove necessity of self.pyraminx

  # Inserts edge into bottom layer when given src and dest layer-wise positions
  def insertEdge(self, currLoc, destLoc):
    algo = []
    onRight = 0
    if self.edgeMap.map[1][currLoc][1] == 4:
      onRight = 1
    initRots = (3-destLoc)%3
    currLoc = (currLoc + initRots)%3
    self.edgeMap.rotateLayer(2, initRots)


    # If edge is to be inserted on right
    if onRight:
      # print("On right")
      if currLoc == 0:
        topRots = 1
      elif currLoc == 1:
        topRots = 0
      else:
        topRots = 2
      self.edgeMap.rotateLayer(1, topRots)
      algo = ["U", "R", "U'", "R'"]
      self.edgeMap.applyAlgo(algo)
      self.edgeMap.rotateLayer(1, -topRots)
      algo = pUtils.fixAlgoWithRots(algo, topRots)
      # print("Unaltered algo: " + str(algo))

    # If edge is to be inserted on left
    elif not onRight:
      # print("On left")
      if currLoc == 0:
        topRots = 2
      elif currLoc == 1:
        topRots = 1
      else:
        topRots = 0
      self.edgeMap.rotateLayer(1, topRots)
      algo = ["U'", "F'", "U", "F"]
      self.edgeMap.applyAlgo(algo)
      self.edgeMap.rotateLayer(1, -topRots)
      algo = pUtils.fixAlgoWithRots(algo, topRots)
      # print("Unaltered algo: " + str(algo))

    # Rotate pyraminx to original orientation
    self.edgeMap.rotateLayer(2, -initRots)
    # Fix algo for the total rotations we did at start
    algo = pUtils.modifyAlgoForOrientation(algo, initRots)
    return algo

  def findSolvableEdge(self):
    topLayer = self.edgeMap.map[1]
    # print(topLayer)
    for i in range(3):
      edge = topLayer[i]
      if edge[0] == 4:
        return i, edge[1]
      if edge[1] == 4:
        return i, edge[0]
    return -1, 0

  # Checks if bottom layer is solved
  def bottomLayerSolved(self):
    layer = self.edgeMap.map[0]
    for i in range(3):
      if layer[i][0] != 4 or layer[i][1] != i+1:
        return 0
    return 1

  # Method to solve bottom layer
  def solveLayer(self):
    finalAlgo = []
    # print("WHILE LOOP STARTING")
    for i in range(3):
      edge = self.findSolvableEdge()
      # print("EDGE FOUND: " + str(edge))
      # Check for easy solvability
      if edge[0] == -1:
        if not self.bottomLayerSolved():
          location, color = self.findStuckEdge()
          finalAlgo += self.solveStuckEdge(location, color)
        else:
          return finalAlgo
      else:
        finalAlgo += self.insertEdge(edge[0], edge[1]-1)
    # print("WHILE LOOP ENDED")
    return finalAlgo

  # Rescue yellow edges stuck on bottom layer
  def rescueStuckEdge(self, posn):
    # print("RESCUING STUCK EDGE: " + str(posn))
    fullRots = 0
    if posn == 1:
      fullRots = 2
    elif posn == 2:
      fullRots = 1
    self.edgeMap.rotateLayer(2, fullRots)
    algo = ["U'", "F'", "U", "F"]
    self.edgeMap.applyAlgo(algo)
    self.edgeMap.rotateLayer(2, -fullRots)
    algo = pUtils.modifyAlgoForOrientation(algo, fullRots)
    currLoc = (-fullRots)%3
    # print("RESCUED")
    # cli.printEdgeMap(self.edgeMap)
    return algo, currLoc
    pass

  # Method to find edge stuck on bottom layer
  def findStuckEdge(self):
    layer = self.edgeMap.map[0]
    for i in range(3):
      if layer[i][1] == 4:
        return i, layer[i][0]
      if layer[i][0] == 4 and layer[i][1] != i+1:
        return i, layer[i][1]
    return -1, 0

  # Method to solve edge stuck on bottom layer
  def solveStuckEdge(self, posn, color):
    algo1, currLoc = self.rescueStuckEdge(posn)
    # print("PLUGGING IN RESCUED EDGE")
    algo2 = self.insertEdge(currLoc, color-1)
    # print("PLUGGED IN")
    return algo1 + algo2