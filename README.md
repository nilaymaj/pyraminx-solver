# Pyraminx Solver
Algorithmic and optimal solvers for Pyraminx, in Python.
Haven't added information on how to use this yet, sorry about that.

## Details
Can enter pyraminx configuration face-wise, or just the scramble.
Two solving methods - one is the algorithmic solver (solves tips, then centres, then bottom layer, then upper layer). Other is the optimal solver - an absolutely terrible implementation of BFS.

## Specifications
Algorithmic solver returns the solution algorithm almost instantaneously.
Optimal solver may take anything from 10 seconds to 3 minutes, depending on complexity of scramble.
