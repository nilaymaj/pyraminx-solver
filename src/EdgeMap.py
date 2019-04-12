# Class file for the EdgeMap class
# Has methods to manipulate the edges of the Pyraminx
# To be used only on a Pyraminx with centres and tips solved
# import cli
import copy
from src import pUtils

class EdgeMap:
  def __init__(self, pyraminx):
    self.map = [[], []]
    self.setUpMap(pyraminx)

  def setUpMap(self, pyraminx):
    self.map[0] = [] # For bottom layer
    self.map[1] = [] # For upper layer
     # Set up map[0]
    # First element of each two-elem list is for bottom color, second for upper face color
    self.map[0].append([pyraminx.yellow_face[2][0], pyraminx.red_face[2][0]])
    self.map[0].append([pyraminx.yellow_face[2][1], pyraminx.green_face[2][1]])
    self.map[0].append([pyraminx.yellow_face[2][2], pyraminx.blue_face[2][2]])
    # Set up map[1]
    self.map[1].append([pyraminx.green_face[2][0], pyraminx.blue_face[2][0]])
    self.map[1].append([pyraminx.blue_face[2][1], pyraminx.red_face[2][1]])
    self.map[1].append([pyraminx.red_face[2][2], pyraminx.green_face[2][2]])
    return

  # Standard move methods
  def U(self):
    self.rotateLayer(1, 1)
  def UInv(self):
    self.rotateLayer(1, -1)
  def F(self):
    newMap = copy.deepcopy(self.map)
    # Top-front to bottom-right
    newMap[0][0][0], newMap[0][0][1] = \
    self.map[1][2][0], self.map[1][2][1]
    # Bottom-left to top-front
    newMap[1][2][0], newMap[1][2][1] = \
    self.map[0][1][1], self.map[0][1][0]
    # Bottom-right to bottom-left
    newMap[0][1][0], newMap[0][1][1] = \
    self.map[0][0][1], self.map[0][0][0]
    # Replace self.map with new map
    self.map = newMap
  def FInv(self):
    self.F()
    self.F()
  def R(self):
    newMap = copy.deepcopy(self.map)
    # Top-right to bottom-back
    newMap[0][2][0], newMap[0][2][1] = \
      self.map[1][1][0], self.map[1][1][1]
    # Bottom-right to top-right
    newMap[1][1][0], newMap[1][1][1] = \
      self.map[0][0][1], self.map[0][0][0]
    # Bottom-back to bottom-right
    newMap[0][0][0], newMap[0][0][1] = \
      self.map[0][2][1], self.map[0][2][0]
    # Replace self.map with new map
    self.map = newMap
  def RInv(self):
    self.R()
    self.R()
  def L(self):
    newMap = copy.deepcopy(self.map)
    # Top-left to bottom-left
    newMap[0][1][0], newMap[0][1][1] = \
      self.map[1][0][0], self.map[1][0][1]
    # Bottom-back to top-left
    newMap[1][0][0], newMap[1][0][1] = \
      self.map[0][2][1], self.map[0][2][0]
    # Bottom-left to bottom-back
    newMap[0][2][0], newMap[0][2][1] = \
      self.map[0][1][1], self.map[0][1][0]
    # Replace self.map with new map
    self.map = newMap
  def LInv(self):
    self.L()
    self.L()

  # Method to apply algo
  def applyAlgo(self, algo):
    switcher = {
      "U": self.U, "U'": self.UInv,
      "F": self.F, "F'": self.FInv,
      "R": self.R, "R'": self.RInv,
      "L": self.L, "L'": self.LInv
    }
    for step in algo:
      func = switcher[step]
      func()
    return

  # Checks if the edge map is easy to solve, ie
  # there are one or more bottom layer edges in top layer
  def checkIfEasy(self):
    topLayer = self.map[0]
    for i in range(3):
      for j in range(2):
        if topLayer[i][j] == 4:
          return 1
    return 0

  # In layerId, pass 0 for bottom layer,
  # 1 for top layer, and anything else for both
  def rotateLayer(self, layerId, rotations):
    if layerId == 0:
      self.map[0] = pUtils.rotateList(self.map[0], rotations)
    elif layerId == 1:
      self.map[1] = pUtils.rotateList(self.map[1], rotations)
    else:
      self.map[0] = pUtils.rotateList(self.map[0], rotations)
      self.map[1] = pUtils.rotateList(self.map[1], rotations)
    return