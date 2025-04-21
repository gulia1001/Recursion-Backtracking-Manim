from manim import *
import numpy as np

class NQueensScene(Scene):

    def construct(self):
        N = 8
        
        title = Text("Backtracking: NQueens", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        square_size = 0.8

        solutions = self.solve_n_queens(N)
        if not solutions:
            self.play(Write(Text("No solutions found.")))
            return

        board = self.create_board(N, square_size)
        self.play(LaggedStartMap(FadeIn, board, lag_ratio=0.05), run_time=2)
        self.wait(1)

        solution = solutions[0]
        for row, col in enumerate(solution):
            queen = Text("♛")
            queen.set_color(BLACK)
            pos = np.array([
                (col - N/2 + 0.5) * square_size,
                (N/2 - row - 0.5) * square_size,
                0
            ])
            queen.move_to(pos)
            self.play(FadeIn(queen), run_time=0.5)

            arrows = self.create_threat_arrows(pos, N, square_size)
            self.play(LaggedStartMap(Create, arrows, lag_ratio=0.1), run_time=1.5)
            self.wait(0.5)
            self.play(FadeOut(arrows), run_time=0.5)
        self.wait(2)

    def solve_n_queens(self, N):

        solutions = []
        cols, diag1, diag2 = set(), set(), set()
        state = []

        def backtrack(row):
            if row == N:
                solutions.append(state.copy())
                return
            for col in range(N):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)
                state.append(col)

                backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)
                state.pop()

        backtrack(0)
        return solutions

    def create_board(self, N, square_size):

        board = VGroup()
        light_color = "#f0d9b5"
        dark_color = "#b58863"
        for i in range(N):
            for j in range(N):
                square = Square(side_length=square_size)
                square.set_fill(light_color if (i + j) % 2 == 0 else dark_color, opacity=1)
                square.set_stroke(BLACK, width=1)
                square.move_to(np.array([
                    (j - N/2 + 0.5) * square_size,
                    (N/2 - i - 0.5) * square_size,
                    0
                ]))
                board.add(square)
        return board

    def create_threat_arrows(self, pos, N, square_size):

        arrows = VGroup()
        directions = [
            RIGHT, LEFT, UP, DOWN,
            RIGHT + UP, RIGHT + DOWN,
            LEFT + UP, LEFT + DOWN
        ]
        length = N * square_size * 0.8
        for d in directions:
            arrow = Arrow(
                start=pos,
                end=pos + normalize(d) * length,
                buff=square_size * 0.1,
                stroke_width=2,
                color=RED
            )
            arrows.add(arrow)
        return arrows
