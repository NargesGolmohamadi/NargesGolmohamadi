import tkinter as tk
import argparse
from collections import deque

from map_reader import map_reader
from graphics import SkyscraperPuzzleGUI
from CSP import CSP
from Solver import Solver


def longest_increasing_sequence(arr):
    """Find the length of the longest increasing sequence starting from the beginning."""
    length = 1
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            length += 1
            max = arr[i]
    return length


# Main part of the code to run the GUI
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Skyscraper Puzzle Solver")

    parser.add_argument(
        "-m",
        "--map",
        type=int,
        choices=[i for i in range(3, 100)],
        help="Map must be less than 100 and greater than 2",
    )
    parser.add_argument(
        "-lcv",
        "--lcv",
        action="store_true",
        help="Enable least constraint value (LCV) as a order-type optimizer"
    )
    parser.add_argument(
        "-mrv",
        "--mrv",
        action="store_true",
        help="Enable minimum remaining values (MRV) as a order-type optimizer"
    )
    parser.add_argument(
        "-MAC",
        "--maintaining_arc_consistency",
        action="store_true",
        help="Enable arc consistency as a mechanism to eliminate the domain of variables achieving an optimized solution"
    )

    args = parser.parse_args()
    clues = map_reader(args.map)  # clues= [top, bottom, left, right]
    grid_size = len(clues[0])


    """ You should implement your model building here """

    csp = CSP()

    for i in range(grid_size ):
        for j in range(grid_size ):
            var_name= f"V_{i}_{j}"
            csp.add_variable(var_name ,list(range(1 ,grid_size + 1 )))

    for i in range(grid_size ):
    csp.add_constraint(lambda vals :len(set(vals.values())) == len(vals) ,[f"V_{i}_{j}" for j in range(grid_size )])
    csp.add_constraint(lambda vals :len(set(vals.values())) == len(vals) ,[f"V_{j}_{i}" for j in range(grid_size )])


    root = tk.Tk()

    root.title("Skyscraper Puzzle")

    # Center the window
    window_width, window_height = 600, 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    solver = Solver(csp, args.lcv, args.mrv, args.maintaining_arc_consistency)

    puzzle = SkyscraperPuzzleGUI(root, grid_size, solver)

    # Adding clues to the GUI
    for j in range(1, grid_size + 1):
        puzzle.add_clue(0, j, clues[0][j - 1], "down")  # Top clue pointing down
        puzzle.add_clue(grid_size + 1, j, clues[1][j - 1], "up")  # Bottom clue pointing up
    for i in range(1, grid_size + 1):
        puzzle.add_clue(i, 0, clues[2][i - 1], "right")  # Left clue pointing right
        puzzle.add_clue(i, grid_size + 1, clues[3][i - 1], "left")  # Right clue pointing left

    root.mainloop()