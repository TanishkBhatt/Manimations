from manim import *    # type: ignore

class ConstructSphere(ThreeDScene):
    def construct(self):
        axis = ThreeDAxes()
        labels = axis.get_axis_labels(Text("X-AXIS").scale(0.3),
                                      Text("Y-AXIS").scale(0.3),
                                      Text("Z-AXIS").scale(0.3))

        sphere = Sphere(center=ORIGIN,
                        radius=1,
                        resolution=(32, 32),
                        color=BLUE)
        sphere.set_opacity(0.6)

        self.set_camera_orientation(70*DEGREES, 45 *DEGREES)
        self.play(Create(axis), run_time=2)
        self.play(Create(labels), run_time=1)
        self.play(Create(sphere), run_time=2)
        self.wait()