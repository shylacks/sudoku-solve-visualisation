import tkinter as tk
import main

class Application(tk.Frame):
    def __init__(self, master=None, width=500, height=500):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.width = width
        self.height = height

    def create_widgets(self):
        self.solve = tk.Button(self, text="Quick Solve", command=self.solveSudoku)
        self.solve.pack(side="top")
        self.solveAnim = tk.Button(self, text="Solve with Animation", command=self.solveSudokuAnim)  # command=self.master.destroy             -        close
        self.solveAnim.pack(side="top")
        self.solve = tk.Button(self, text="Reset", command=self.displaySudoku)
        self.solve.pack()
        self.solve = tk.Button(self, text="Next", command=self.displaySudoku)
        self.solve.pack(side="bottom")
    def solveSudoku(self):
        main.solve(main.sudoku)

    def solveSudokuAnim(self):
        main.solve_animation(main.sudoku)
        print("No other solution found")

    def displaySudoku(self):
        main.displaySudoku(main.sudoku)

class anotherSolution():
    def __init__(self, master=None, width=500, height=500):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.pack()
        self.create_widgets()
        self.width = width
        self.height = height

    def create_widgets(self):
        self.solve = tk.Button(self, text="Looking for another solution?")
        self.solve.pack(side="top")
        self.solveAnim = tk.Button(self, text="I'm done")  # command=self.master.destroy             -        close
        self.solveAnim.pack(side="top")




