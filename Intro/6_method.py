from manim import *

from _base import MyScene
from _imports import video_frame, MyColors


class Method(MyScene):
    def construct(self):
        magic_text = self.latex(
            "Saw a magic?",
            font_size=40,
            color=MyColors.highlight_color,
        )

        how_works_text = self.latex(
            "Let's see how it works in detail.",
            color=WHITE,
            font_size=15,
        )

        proposed_solution = self.latex(
            "Our proposed solution",
            color=MyColors.highlight_color,
            font_size=40,
        )

        starting_text = self.latex(
            "It all starts with a video upload.",
            color=WHITE,
            font_size=15,
        )

        lets_upload = self.latex(
            "Let's upload a video..",
            color=WHITE,
            font_size=10,
        )

        i_eng_video = video_frame()
        i_eng_video.scale(1 / 3)

        f_eng_video = video_frame()
        f_eng_video.scale(3)

        magic_text.to_edge(UP, buff=2)
        how_works_text.next_to(magic_text, DOWN, buff=1.5)
        proposed_solution.to_edge(UP, buff=1)
        starting_text.next_to(proposed_solution, DOWN, buff=1)
        lets_upload.next_to(starting_text, DOWN, buff=1)

        i_eng_video.next_to(lets_upload, DOWN, buff=1)
        f_eng_video.move_to(ORIGIN)

        self.play(Write(magic_text))
        self.wait(0.5)
        self.play(Write(how_works_text))
        self.wait(1)
        self.play(FadeOut(magic_text), FadeOut(how_works_text))
        self.wait(0.5)
        self.play(Write(proposed_solution))
        self.wait(0.5)
        self.play(Write(starting_text))
        self.wait(0.5)
        self.play(Write(lets_upload))
        self.wait(0.5)
        self.play(FadeIn(i_eng_video))
        self.wait(0.5)
        self.play(
            FadeOut(proposed_solution),
            FadeOut(starting_text),
            FadeOut(lets_upload),
            Transform(i_eng_video, f_eng_video, run_time=2),
        )
        self.wait(0.5)
