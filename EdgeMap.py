# Class file for the EdgeMap class
# Has methods to manipulate the edges of the Pyraminx
# To be used only on a Pyraminx with centres and tips solved

class EdgeMap:
  def __init__(self, pyraminx):
    self.map = {}
    self.setUpMap(pyraminx)

  def setUpMap(self, pyraminx):
    pass