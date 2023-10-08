from manim import *


class Tester(Scene):
    def construct(self):
        shift = LEFT * 0.2 + DOWN * 0.2

        frame = RoundedRectangle(
            width=8.0,
            height=4.5,
            color=WHITE,
            stroke_width=2,
            fill_opacity=1.0,
            fill_color=BLACK,
            corner_radius=0.2,
        )

        frame_2 = frame.copy().shift(shift)
        frame_3 = frame.copy().shift(shift * 2)
        frame_4 = frame.copy().shift(shift * 3)

        frames = VGroup(frame, frame_2, frame_3, frame_4)
        frames.move_to(ORIGIN)

        self.add(frames)

        self.wait(1)
