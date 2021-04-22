import pygame
import tkint
import tkinter as tk
import time

pygame.init()
WIDTH, HEIGHT = 420, 420
pygame.display.set_caption('Sudoku')
screen = pygame.display.set_mode((WIDTH, HEIGHT + 100))
background_colour = (255, 255, 255)
screen.fill(background_colour)

animationTime = 0.5
bigSquareT = 5
smallSquareT = 2
focusT = 5
ratio = WIDTH / 9
boxSize = WIDTH // 9

myFont = pygame.font.SysFont("Times New Roman", WIDTH // 27)
sudoku = [[8, 1, 0, 0, 3, 0, 0, 2, 7],
         [0, 6, 2, 0, 5, 0, 0, 9, 0],
         [0, 7, 0, 0, 0, 0, 0, 0, 0],
         [0, 9, 0, 6, 0, 0, 1, 0, 0],
         [1, 0, 0, 0, 2, 0, 0, 0, 4],
         [0, 0, 8, 0, 0, 5, 0, 7, 0],
         [0, 0, 0, 0, 0, 0, 0, 8, 0],
         [0, 2, 0, 0, 1, 0, 7, 5, 0],
         [3, 8, 0, 0, 7, 0, 0, 4, 2]]


# real solving


def possible_options(x, y, l):
    for ix in range(0, 9):
        if l == sudoku[y][ix]:
            return False
    for iy in range(0, 9):
        if l == sudoku[iy][x]:
            return False
    for i in range(0, 3):
        for j in range(0, 3):
            if l == sudoku[((y // 3) * 3) + i][((x // 3) * 3) + j]:
                return False
    return True


def solve(sudoku):
    for y in range(0, 9):
        for x in range(0, 9):
            if sudoku[y][x] == 0:
                for i in range(1, 10):
                    if possible_options(x, y, i):
                        sudoku[y][x] = i
                        solve(sudoku)
                        sudoku[y][x] = 0
                return
    displaySudoku(sudoku)


def solve_animation(sudokux):
    found = False
    if not found:
        for y in range(0, 9):
            for x in range(0, 9):
                if sudokux[y][x] == 0:
                    for i in range(1, 10):
                        if possible_options(x, y, i):
                            sudokux[y][x] = i
                            displaySudoku(sudokux)
                            drawRedFocus(x, y)
                            pygame.display.update()
                            time.sleep(animationTime)
                            solve_animation(sudokux)
                            sudokux[y][x] = 0
                    return
    print("Found")
    found = True

def all(sudoku):
    for i in range(9):
        for j in range(9):
            if (sudoku[i][j] == 0):
                return False


# visulaisation
def drawGrid():
    # big squares
    for i in range(0, 4):
        pygame.draw.line(screen, (0, 0, 0), [0, i * WIDTH / 3], [WIDTH, i * WIDTH / 3], bigSquareT)
    for i in range(0, 4):
        pygame.draw.line(screen, (0, 0, 0), [i * HEIGHT / 3, 0], [i * HEIGHT / 3, HEIGHT], bigSquareT)

    # small squares
    for i in range(0, 9):
        pygame.draw.line(screen, (0, 0, 0), [0, i * ratio], [WIDTH, i * ratio], smallSquareT)
    for i in range(0, 9):
        pygame.draw.line(screen, (0, 0, 0), [i * ratio, 0], [i * ratio, HEIGHT], smallSquareT)


def displaySudoku(sudoku):
    screen.fill([255, 255, 255])
    drawGrid()
    for line in range(0, 9):
        for number in range(0, 9):
            if sudoku[line][number] != 0:
                displayNumber = myFont.render(str(sudoku[line][number]), 1, (0, 0, 0))
                screen.blit(displayNumber, (number * ratio + ratio / 2, line * ratio + ratio / 2))
    pygame.display.update()


def drawRedFocus(x, y):
    pygame.draw.line(screen, (255, 0, 0), [x * ratio, y * ratio], [x * ratio + ratio, y * ratio], focusT)
    pygame.draw.line(screen, (255, 0, 0), [x * ratio, y * ratio + ratio], [x * ratio + ratio, y * ratio + ratio],
                     focusT)
    pygame.draw.line(screen, (255, 0, 0), [x * ratio, y * ratio], [x * ratio, y * ratio + ratio], focusT)
    pygame.draw.line(screen, (255, 0, 0), [x * ratio + ratio, y * ratio], [x * ratio + ratio, y * ratio + ratio],
                     focusT)


drawGrid()
displaySudoku(sudoku)
pygame.display.update()

root = tk.Tk()
root.geometry("200x100")
root.resizable(0, 0)
app = tkint.Application(master=root)
app.mainloop()

run = True
while run:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            run = False
        # if e.type == pygame.KEYDOWN:
        #     if e.key == pygame.K_s:
        #         print(rozwiazania)
        #     if e.key == pygame.K_a:
        #         solveAnimation(sudoku)
        #         pygame.display.update()
    pygame.display.update()
    root.update()
