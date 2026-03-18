from manim import *     # type: ignore

class AreaOfCircle(Scene):
    def construct(self):
        circle = Circle(radius=2.5, color=BLUE)
        center = circle.get_center()
        point = circle.point_at_angle(PI/4.5)
        radius = Line(center, point, color=YELLOW)
        label = Text("r").scale(0.75).next_to(radius, DOWN)
        formula = Text("A = πr²").to_edge(UP)

        self.play(Create(circle), run_time=2.5)
        self.play(GrowFromCenter(radius), run_time=1.5)
        self.play(Write(label), run_time=1)
        self.play(Write(formula), run_time=1)
        self.wait()