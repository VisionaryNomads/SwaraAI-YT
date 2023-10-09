from manim import *

from _base import MyScene
from _imports import latex


class Business(MyScene):
    _intro = "Business Model"

    _desc = [
        "A 2021 study by Google found that websites with multilingual support had a 13 percent higher conversion rate than websites that only supported English. This study was conducted in India and included over 100,000 websites.",
        "According to a 2022 report by Statista, 66 percent of internet users in India prefer to consume content in their own language. This suggests that websites with multilingual support are likely to gain more attention in India than websites that only support English.",
    ]

    _desc_2 = [
        "Since this is a dubbing software multiple collaborations are possible across the country for Regional Language Voice-over artists and global recognition from English speaking voiceover artists. A voice-over artist expert in more than one Indian Regional Language can have exposure to dubbing high quality videos from his/her hometown.",
        "Since dubbing is required in education, entertainment, promotions and creating public awareness this software will not attract only a certain category of users but a wide range of users. This will help us to reach a wider audience and gain more popularity.",
    ]

    def construct(self):
        gap = DOWN * 1.5

        title = self.get_title()
        intro = (
            latex(
                self._intro,
                10,
                color=WHITE,
                tex_environment="flushleft",
            )
            .next_to(title, gap, buff=0.5)
            .align_to(title, LEFT)
        )

        down_shift = 0
        desc = VGroup()
        for line in self._desc:
            line = (
                latex(
                    line,
                    12,
                    color=WHITE,
                    tex_environment="flushleft",
                    tex_to_color_map={
                        "13 percent higher conversion rate": self.highlight_color,
                        "66 percent of internet users in India prefer to consume content in their own language": self.highlight_color,
                    },
                )
                .set(width=9)
                .next_to(intro, gap, buff=0.5)
                .shift(down_shift)
                .align_to(intro, LEFT)
            )
            desc.add(line)
            down_shift -= line.height + 0.2

        down_shift = 0
        desc_2 = VGroup()
        for line in self._desc_2:
            line = (
                latex(
                    line,
                    12,
                    color=WHITE,
                    tex_environment="flushleft",
                    tex_to_color_map={
                        "Regional Language Voice-over artists": self.highlight_color,
                        "English speaking voiceover artists": self.highlight_color,
                        "voice-over artist expert in more than one Indian Regional Language": self.highlight_color,
                        "dubbing high quality videos from his/her hometown": self.highlight_color,
                        "dubbing is required in education, entertainment, promotions and creating public awareness": self.highlight_color,
                    },
                )
                .set(width=9)
                .next_to(intro, gap, buff=0.35)
                .shift(down_shift)
                .align_to(intro, LEFT)
            )
            desc_2.add(line)
            down_shift -= line.height + 0.2

        business_model = (
            SVGMobject("images/business.svg", fill_color=GRAY_B)
            .set(width=3)
            .next_to(desc, RIGHT, buff=0.5)
        )

        self.play(
            FadeIn(title),
            LaggedStartMap(FadeIn, intro, lag_ratio=0.2, run_time=1),
            LaggedStartMap(FadeIn, desc, lag_ratio=0.2, run_time=2),
        )
        self.play(Write(business_model))

        self.wait(4)

        self.play(
            LaggedStartMap(FadeOut, desc, lag_ratio=0.2, run_time=1),
            LaggedStartMap(FadeIn, desc_2, lag_ratio=0.2, run_time=3),
        )

        self.wait(4)

        self.play(
            LaggedStartMap(FadeOut, intro, lag_ratio=0.2, run_time=1),
            LaggedStartMap(FadeOut, desc_2, lag_ratio=0.2, run_time=2),
            FadeOut(business_model),
        )
