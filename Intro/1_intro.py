from manim import *
from _video import video_frame

from _base import MyScene


class Intro(MyScene):
    _title = "SwaraAI"
    _description = "Developing a software for dubbing of videos from English to other Indian regional languages."
    _ps = "SIH 1386"
    _team = "Visionary Nomads"

    def get_title(self):
        return self.latex(self._title, 80, color=YELLOW)

    def get_description(self):
        return self.latex(
            self._description,
            20,
            color=WHITE,
            tex_to_color_map={"dubbing of videos": RED},
            tex_environment="flushleft",
        ).set(width=8)

    def get_ps(self):
        return self.latex(self._ps, 8, color=GRAY_B)

    def get_team(self):
        return self.latex(self._team, 12, color=GRAY_B)

    def get_dub_animation(self):
        eng_video = video_frame()
        hin_video = video_frame(add_subtitle=True)

        # Small text below the video
        eng_text = Tex(
            "\\tiny{\\textbf{English Video}}",
            color=WHITE,
        )
        hin_text = Tex(
            "\\tiny{\\textbf{Hindi Video}}",
            color=WHITE,
        )

        eng_text.next_to(eng_video, DOWN, buff=0.2)
        hin_text.next_to(hin_video, DOWN, buff=0.2)

        eng_vid_text = VGroup(eng_video, eng_text)
        hin_vid_text = VGroup(hin_video, hin_text)

        eng_vid_text.to_corner(UR, buff=1)
        hin_vid_text.to_corner(DR, buff=1)

        # Make a arrow from eng_video to hin_video
        arrow = Arrow(
            eng_vid_text.get_bottom(),
            hin_vid_text.get_top(),
            color=GRAY_B,
            buff=0.2,
        )

        # Make a text "Dubbing" and align it to the arrow
        dubbing_text = Text("Dubbing", color=GRAY_B, font_size=15)

        # Align the text to the arrow
        # Rotate the text by 90 degrees
        dubbing_text.rotate(90 * DEGREES)

        dubbing_text.next_to(arrow, LEFT, buff=0.2)

        # Create a VGroup of the two videos
        videos = VGroup(eng_vid_text, hin_vid_text)

        # Create a VGroup of the arrow and the text
        arrow_text = VGroup(arrow, dubbing_text)

        # Create a VGroup of the videos and the arrow_text
        dubbing = VGroup(videos, arrow_text)

        return dubbing

    def construct(self):
        title = self.get_title()
        description = self.get_description()
        ps = self.get_ps()
        team = self.get_team()

        dubbing = self.get_dub_animation()

        self.play(Write(title))
        self.wait(1)

        gap = DOWN * 1.5

        title_copy = title.copy().to_corner(UL, buff=1)
        description.next_to(title_copy, gap, buff=0.5).align_to(title_copy, LEFT)
        ps.next_to(description, gap, buff=0.5).align_to(description, LEFT)
        team.next_to(ps, gap, buff=0.5).align_to(ps, LEFT)

        self.play(Transform(title, title_copy))

        self.wait(0.3)

        self.play(
            LaggedStartMap(FadeIn, description, lag_ratio=0.2),
            LaggedStartMap(FadeIn, ps, lag_ratio=0.2),
            LaggedStartMap(FadeIn, team, lag_ratio=0.2),
            # LaggedStartMap(FadeIn, dubbing, lag_ratio=0.2),
            *[LaggedStartMap(FadeIn, obj, lag_ratio=0.2) for obj in dubbing],
        )

        self.wait(0.5)
