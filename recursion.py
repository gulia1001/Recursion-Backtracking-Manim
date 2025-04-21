from manim import *
import numpy as np

class BinaryTree(MovingCameraScene):
    def construct(self):
        title = Text("Recursion: Binary Tree", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        self.camera.frame.save_state()
        self.camera.frame.scale(3)
        self.camera.frame.shift(10*UP)

        group = VGroup()

        def tree(length, angle, point, angle1):
            line = Line(ORIGIN, length * UP, color=GREEN, stroke_width=4)
            line.shift(point)
            line.rotate(angle, about_point=point)
            group.add(line)
            if length > 0.2:
                tree(length / 1.5, angle + angle1 * DEGREES, line.get_end(), angle1)
                tree(length / 1.5, angle - angle1 * DEGREES, line.get_end(), angle1)
            return group

        tr = tree(7, 0, ORIGIN, 30)
        self.play(AnimationGroup(*[Create(m) for m in tr], lag_ratio=0.01))
        self.wait()



class Dragon(MovingCameraScene):
    def construct(self) -> None:

        title = Text("Recursion: Dragon Curve Fractal", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        line = Line(ORIGIN, RIGHT)
        point = line.get_end()
        self.add(line)
        for i in range(10):
            c = VGroup(*[line.copy() for _ in range(2)])
            self.add(c[0].set_color(RED))
            c[1].set_color(YELLOW)
            self.play(c[1].animate.rotate(90 * DEGREES, about_point=point))
            line = c
            point = list(reversed(c[1].get_all_points()))[-1]
            self.camera.frame.scale(1.3)
            self.camera.frame.move_to(c)
        self.wait(2)



class trinagle_fractal(MovingCameraScene):
    def construct(self):
        title = Text("Recursion: Sierpiński Triangle", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        self.camera.frame.save_state()
        frame=self.camera.frame
        tri=Triangle()
        for i in range(10):
            triangle = VGroup(*[tri.copy() for _ in range(3)])
            triangle[1].next_to(triangle[0], RIGHT)
            new_t = VGroup(triangle[0], triangle[1])
            triangle[2].next_to(new_t, UP)
            self.play(frame.animate.move_to(triangle.get_center()).set_height(triangle.get_height()*1.5))
            self.play(Create(triangle))
            self.wait(1)
            tri=triangle
