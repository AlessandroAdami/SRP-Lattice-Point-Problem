import os
import shutil
from manim import *

output_dir = "./media"

# Delete the folder of media you do not need
#if os.path.exists(output_dir): shutil.rmtree(output_dir)

class tCircle(Scene):
    def construct(self):
        radius = 3
        grid_range = range(-radius-1, radius+2)  # Add a buffer for display
        circle_center = ORIGIN

        # Draw coordinate grid with integer lines
        grid = NumberPlane(
            x_range=[-radius-4, radius+4, 1],
            y_range=[-radius-4, radius+4, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_opacity": 0.4,
                "stroke_width": 1,
            }
        )
        self.add(grid)

        # Draw the circle
        circle = Circle(radius=radius).move_to(circle_center)
        self.play(Create(circle))

        # Add lattice points within the circle
        points = []
        for x in grid_range:
            for y in grid_range:
                if x**2 + y**2 <= radius**2:
                    dot = Dot(point=[x, y, 0], radius=0.06, color=RED)
                    points.append(dot)

        self.play(LaggedStartMap(FadeIn, VGroup(*points), lag_ratio=0.05))
        self.wait(2)

class LatticeTranslation(Scene):
    def construct(self):
        grid = NumberPlane(
            x_range=[0, 6, 1],
            y_range=[0, 5, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_opacity": 0.3,
                "stroke_width": 1,
            },
        )
        self.add(grid)

        start = grid.coords_to_point(1.8, 1.8)
        end = grid.coords_to_point(3.8, 3.8)

        shift_vector = end - start

        radius = 1
        circle1 = Circle(radius=radius, color=WHITE).move_to(start)
        self.play(Create(circle1))

        dots = []
        target_dots = []

        for x, y in [[1, 2], [2, 1], [2, 2]]:
            orig_dot = Dot(grid.coords_to_point(x, y), color=WHITE)
            moved_dot = orig_dot.copy().shift(shift_vector)
            dots.append(orig_dot)
            target_dots.append(moved_dot)
        
        arrow = Arrow(start, end, buff=0, color=GRAY)
        self.play(Create(arrow))

        self.play(*[Create(dot) for dot in dots])

        circle2 = circle1.copy().shift(shift_vector)
        self.play(
            TransformFromCopy(circle1, circle2),
            *[TransformFromCopy(dot, moved) for dot, moved in zip(dots, target_dots)],
            run_time=2.5
        )

        self.wait(2)