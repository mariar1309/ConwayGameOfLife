# ConwayGameOfLife

Game whose evolution is determined by its initial input with no further changes required. Cells turn on and off following predetermined rules that depend on the state of other surrounding cells (an example of cellular automation.)

Suggests evolution of complex structures through simple rules w/o following a preset pattern"

Starter code: "Python Playground" by Mahesh Venkitachalam

Personal Modifications:
Emergence: Fractal Patterns in Snowflakes
Gamescrafters logo

"
    Initial condition of the system can be set to either a random distribution or a predesigned pattern.

    A system consists of the following components:
    - A property defined in a one- or two-dimensional space
    - A mathematical rule to change this property for each step in the simulation
    - A way to capture or display the state of the system as it evolves
"

Game is captured on an NxN grid of cells, where each cell has a coordinate [i,j]. A cell is either ON or OFF. Conway's Game of Life has 4 rules by which cells switch their condition:
" 
    1. If a cell is ON and has fewer than 2 neighbors that are ON, it turns OFF
    2. If a cell is ON and has either 2 or 3 neighbors that are ON, it remains ON
    3. If a cell is ON and has more than 3 neighbors that are ON, it turns OFF
    4. If a cell is OFF and has exactly 3 neighbors that are ON, it turns ON.
"

Employing Toroidal Boundary Conditions --> the square grid wraps around and joins edges so that it's shape is a torus. Allows all cells to have neighbors (for the 4 rules to function properly) because the shape has no edges. (Similar to how boundaries work in Pac-Man).
Example:
[1][2][3]
[4][5][6]  --> the neighbors of [1] would be [2],[4],[5] but also [7] and [3]
[7][8][9]