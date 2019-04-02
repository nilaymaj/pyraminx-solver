# Class file to solve one layer of edges
# To be used after centres are solved

class LayerSolver:
  def __init__(self, pyraminx):
    self.pyraminx = pyraminx

  # Returns the layer that is easiest to solve
  # No. of solved edges, no. of flipped edges, etc
  def optimumLayer(self):
# TODO: Implement this method
    return self.pyraminx.red_face

