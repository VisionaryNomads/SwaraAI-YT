from manim import *

from _base import MyScene
from _imports import video_frame, logo_bg, logo_text, logo


class Intro(MyScene):
    _title = "SwaraAI"
    _description = "Developing a software for dubbing of videos from English to other Indian regional languages."
    _ps = "SIH 1386"
    _team = "Visionary Nomads"

    def add_title(self):
        _logo_bg = logo_bg(1).scale(1.2)
        _logo_text = logo_text()

        self.play(Write(_logo_bg, run_time=2))
        self.wait(0.5)
        self.play(
            Transform(_logo_bg, logo_bg(0.75), run_time=3),
            Write(_logo_text, run_time=4),
        )
        self.wait(1)
        logo = VGroup(_logo_bg, _logo_text)

        self.play(Transform(logo, self.get_title()), run_time=1.5)
        return logo

    def get_description(self):
        return self.latex(
            self._description,
            20,
            color=WHITE,
            tex_to_color_map={"dubbing of videos": self.highlight_color},
            tex_environment="flushleft",
        ).set(width=8)

    def get_ps(self):
        return self.latex(self._ps, 8, color=GRAY_B)

    def get_team(self):
        return self.latex(self._team, 12, color=GRAY_B)

    def get_dub_animation(self):
        eng_video = video_frame()
        hin_video = video_frame(add_subtitle=True)

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

        arrow = Arrow(
            eng_vid_text.get_bottom(),
            hin_vid_text.get_top(),
            color=GRAY_B,
            buff=0.2,
        )

        dubbing_text = Text("Dubbing", color=GRAY_B, font_size=15)
        dubbing_text.rotate(90 * DEGREES)
        dubbing_text.next_to(arrow, LEFT, buff=0.2)
        arrow_text = VGroup(arrow, dubbing_text)
        dubbing_group = VGroup(eng_vid_text, arrow_text, hin_vid_text)

        return dubbing_group

    def construct(self):
        description = self.get_description()
        ps = self.get_ps()
        team = self.get_team()

        dubbing = self.get_dub_animation()
        _e, _t, _h = dubbing

        title = self.add_title()
        self.wait(1)

        gap = DOWN * 1.5

        description.next_to(title, gap, buff=0.5).align_to(title, LEFT)
        ps.next_to(description, gap, buff=0.5).align_to(description, LEFT)
        team.next_to(ps, gap, buff=0.5).align_to(ps, LEFT)

        self.play(
            LaggedStartMap(FadeIn, description, lag_ratio=0.2),
            LaggedStartMap(FadeIn, ps, lag_ratio=0.2),
            LaggedStartMap(FadeIn, team, lag_ratio=0.2),
        )

        self.wait(0.5)

        self.play(Write(_e, run_time=1.5))
        self.wait(0.5)
        self.play(Write(_t, run_time=1.5))
        self.wait(0.5)
        self.play(Write(_h, run_time=1.5))

        self.wait(4)

        self.play(
            LaggedStartMap(FadeOut, description, lag_ratio=0.2),
            LaggedStartMap(FadeOut, ps, lag_ratio=0.2),
            LaggedStartMap(FadeOut, team, lag_ratio=0.2),
            *[LaggedStartMap(FadeOut, obj, lag_ratio=0.2) for obj in dubbing],
        )
