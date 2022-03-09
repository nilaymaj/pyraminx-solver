# Pyraminx Solver

Algorithmic and optimal solvers for Pyraminx, in Python.

## Details

Can enter pyraminx configuration face-wise, or just the scramble.
Two solving methods - one is the algorithmic solver (solves tips, then centres, then bottom layer, then upper layer). Other is the optimal solver - an absolutely terrible implementation of BFS.

## Usage

This section is written over 3 years after I last touched this project, so it is not very well written - sorry about that.

The PDF `cell-numbering.pdf` contains two hand-drawn figures that represent the cut-open form of a pyraminx (like geometry nets). The **net folds inwards, behind the page**. When using the program, you are expected to **orient your pyraminx** such that one of its corners faces directly towards you. One corner will be at the top, and the other two corners will be backwards left and backwards right.

In the above PDF, the first figure shows how the **9 cells of each face are ordered** for input purpose. This ordering is required when inputting a scrambled pyraminx configuration. The second figure is a helper for the internal representation of the pyraminx - refer to `src/Pyraminx.py::setUpFaces` for the associated code.

The facewise input mode requires as input 4 lines. Each line represents the cell colors of a single face and contains 9 digits (1-4). To enter a scramble:

1. Keep your physical pyraminx positioned as mentioned above and number the faces in the order Red-Green-Blue-Yellow (refer to the figures). So the face just to the right is face 1 (Red), the face to the left is face 2 (Green), the face at back is face 3 (Blue) and the face at the bottom is face 4 (Yellow). The colours here don't really mean anything - you're free to orient the pyraminx in whatever way you want.

2. Next, assign a number to each colour. I'm not sure if the colours and numbers have to match the order above (1-R 2-G 3-B 4-Y) or can be arbitrary - maybe you can check that out.

3. Now, finally entering the scramble: each line of input corresponds to one of the faces in the order above. So line 1 corresponds to face 1, and so on. For each line: type in the colours on each of the cells on that face, in the order shown in figure 1. So a possible line of input is "233122433" (without the quotes). The full input is just four such lines (one for each face) - look at `src/pyrConfig.txt` for an example.

## Specifications

Algorithmic solver returns the solution algorithm almost instantaneously.
Optimal solver may take anything from 10 seconds to 3 minutes, depending on complexity of scramble.
