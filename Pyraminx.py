# Class file for the Pyraminx class
# Stores the configuration state of the Pyraminx

import pUtils

class Pyraminx:
  def __init__(self, red_face, green_face, blue_face, yellow_face):
    self.red_face = []
    self.green_face = []
    self.blue_face = []
    self.yellow_face = []
    self.setUpFaces(red_face, green_face, blue_face, yellow_face)

  def setUpFaces(self, red_face, green_face, blue_face, yellow_face):
    # Add the tips information
    self.red_face.append([red_face[0], red_face[4], red_face[8]])
    self.green_face.append([green_face[8], green_face[0], green_face[4]])
    self.blue_face.append([blue_face[4], blue_face[8], blue_face[0]])
    self.yellow_face.append([yellow_face[0], yellow_face[8], yellow_face[4]])

    # Add the centres information
    self.red_face.append([red_face[2], red_face[5], red_face[7]])
    self.green_face.append([green_face[7], green_face[2], green_face[5]])
    self.blue_face.append([blue_face[5], blue_face[7], blue_face[2]])
    self.yellow_face.append([yellow_face[2], yellow_face[7], yellow_face[5]])

    # Add the edges information
    self.red_face.append([red_face[6], red_face[3], red_face[1]])
    self.green_face.append([green_face[1], green_face[6], green_face[3]])
    self.blue_face.append([blue_face[3], blue_face[1], blue_face[6]])
    self.yellow_face.append([yellow_face[6], yellow_face[1], yellow_face[3]])

    print("Pyraminx state set.")

  # Returns face according to faceId
  def face(self, faceId):
    switcher = {
      1: self.red_face,
      2: self.green_face,
      3: self.blue_face,
      4: self.yellow_face
    }
    return switcher[faceId]

  # Tip rotations
  def u(self):
    self.red_face[0][0], self.green_face[0][1], self.blue_face[0][2] = \
    self.blue_face[0][2], self.red_face[0][0], self.green_face[0][1]
  def f(self):
    self.red_face[0][1], self.green_face[0][0], self.yellow_face[0][2] = \
    self.green_face[0][0], self.yellow_face[0][2], self.red_face[0][1]
  def r(self):
    self.red_face[0][2], self.blue_face[0][0], self.yellow_face[0][1] = \
    self.yellow_face[0][1], self.red_face[0][2], self.blue_face[0][0]
  def l(self):
    self.green_face[0][2], self.blue_face[0][1], self.yellow_face[0][0] = \
    self.blue_face[0][1], self.yellow_face[0][0], self.green_face[0][2]
  def uInv(self):
    self.u()
    self.u()
  def fInv(self):
    self.f()
    self.f()
  def rInv(self):
    self.r()
    self.r()
  def lInv(self):
    self.l()
    self.l()

  # Deep rotations (two-layer)
  def U(self):
    self.u()
    # Rotate the centres
    self.red_face[1][0], self.green_face[1][1], self.blue_face[1][2] = \
    self.blue_face[1][2], self.red_face[1][0], self.green_face[1][1]
    # Rotate first (left) set of edges
    self.red_face[2][2], self.green_face[2][0], self.blue_face[2][1] = \
    self.blue_face[2][1], self.red_face[2][2], self.green_face[2][0]
    # Rotate second (right) set of edges
    self.red_face[2][1], self.green_face[2][2], self.blue_face[2][0] = \
    self.blue_face[2][0], self.red_face[2][1], self.green_face[2][2]
  def F(self):
    self.f()
    # Rotate the centres
    self.red_face[1][1], self.yellow_face[1][2], self.green_face[1][0] = \
    self.green_face[1][0], self.red_face[1][1], self.yellow_face[1][2]
    # Rotate first (left) set of edges
    self.red_face[2][0], self.yellow_face[2][1], self.green_face[2][2] = \
    self.green_face[2][2], self.red_face[2][0], self.yellow_face[2][1]
    # Rotate second (right) set of edges
    self.red_face[2][2], self.yellow_face[2][0], self.green_face[2][1] = \
    self.green_face[2][1], self.red_face[2][2], self.yellow_face[2][0]
  def R(self):
    self.r()
    # Rotate the centres
    self.red_face[1][2], self.blue_face[1][0], self.yellow_face[1][1] = \
    self.yellow_face[1][1], self.red_face[1][2], self.blue_face[1][0]
    # Rotate first (left) set of edges
    self.red_face[2][1], self.blue_face[2][2], self.yellow_face[2][0] = \
    self.yellow_face[2][0], self.red_face[2][1], self.blue_face[2][2]
    # Rotate second (right) set of edges
    self.red_face[2][0], self.blue_face[2][1], self.yellow_face[2][2] = \
    self.yellow_face[2][2], self.red_face[2][0], self.blue_face[2][1]
  def L(self):
    self.l()
    # Rotate the centres
    self.green_face[1][2], self.yellow_face[1][0], self.blue_face[1][1] = \
    self.blue_face[1][1], self.green_face[1][2], self.yellow_face[1][0]
    # Rotate first (left) set of edges
    self.green_face[2][1], self.yellow_face[2][2], self.blue_face[2][0] = \
    self.blue_face[2][0], self.green_face[2][1], self.yellow_face[2][2]
    # Rotate second (right) set of edges
    self.green_face[2][0], self.yellow_face[2][1], self.blue_face[2][2] = \
    self.blue_face[2][2], self.green_face[2][0], self.yellow_face[2][1]
  def UInv(self):
    self.U()
    self.U()
  def FInv(self):
    self.F()
    self.F()
  def LInv(self):
    self.L()
    self.L()
  def RInv(self):
    self.R()
    self.R()

  # Method to apply step depending on string argument.
  def move(self, moveId):
    if moveId == "u":
      self.u()
      return
    if moveId == "f":
      self.f()
      return
    if moveId == "r":
      self.r()
      return
    if moveId == "l":
      self.l()
      return
    if moveId == "u'":
      self.uInv()
      return
    if moveId == "f'":
      self.fInv()
      return
    if moveId == "r'":
      self.rInv()
      return
    if moveId == "l'":
      self.lInv()
      return

    if moveId == "U":
      self.U()
      return
    if moveId == "F":
      self.F()
      return
    if moveId == "R":
      self.R()
      return
    if moveId == "L":
      self.L()
      return
    if moveId == "U'":
      self.UInv()
      return
    if moveId == "F'":
      self.FInv()
      return
    if moveId == "R'":
      self.RInv()
      return
    if moveId == "L'":
      self.LInv()
      return

  # Method to replace a face of the pyraminx by a given face-matrix
  def setFace(self, faceId, face):
    if faceId == 1:
      self.red_face = face
    elif faceId == 2:
      self.green_face = face
    elif faceId == 3:
      self.blue_face = face
    else:
      self.yellow_face = face

  # Apply an algorithm given as a list
  def applyAlgo(self, algo):
    for step in algo:
      self.move(step)

  # Fix the face colors
  def fixFaceColors(self):
    self = pUtils.fixColors(self)