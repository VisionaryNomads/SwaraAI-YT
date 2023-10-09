from manim import *

from _imports import MyColors, latex


class WhyRVC(Scene):
    _intro = "Why Realistic Voice Cloning (RVC)?"

    _desc = [
        "RVC is an advanced AI technology that excels in creating highly realistic AI voice models. It utilizes deep learning algorithms to analyze and replicate human voices with astonishing accuracy.",
        "RVC V2 takes the voice cloning technology to the next level by providing a more realistic and natural voice. It requires less than 10 minutes of audio to create a voice model.",
    ]

    _ref = "https://www.topmediai.com/text-speaker/rvc-ai-voice/"

    def construct(self):
        gap = DOWN * 1.5

        intro = latex(
            self._intro,
            15,
            color=WHITE,
            tex_environment="flushleft",
            tex_to_color_map={
                "Realistic Voice Cloning (RVC)": MyColors.highlight_color,
            },
        ).to_corner(UL, buff=1)

        down_shift = 0
        desc = VGroup()
        for line in self._desc:
            line = (
                latex(
                    line,
                    14,
                    color=WHITE,
                    tex_environment="flushleft",
                    tex_to_color_map={
                        "excels": MyColors.highlight_color,
                        "analyze and replicate human voices": MyColors.highlight_color,
                        "realistic and natural voice": MyColors.highlight_color,
                        "less than 10 minutes of audio": MyColors.highlight_color,
                    },
                )
                .set(width=8)
                .next_to(intro, gap, buff=0.5)
                .shift(down_shift)
                .align_to(intro, LEFT)
            )
            desc.add(line)
            down_shift -= line.height + 0.2

        ref = latex(
            self._ref,
            4,
            color=MyColors.reference_color,
            tex_environment="flushleft",
        )

        ref_ul = Underline(
            ref,
            buff=0.05,
            stroke_width=1,
            color=MyColors.reference_color,
        )

        reference = VGroup(ref, ref_ul)
        reference.to_corner(DL, buff=1)

        self.play(Write(intro))
        self.play(
            LaggedStart(
                *[FadeIn(line, shift=UP * 0.5) for line in desc],
                lag_ratio=0.1,
                run_time=3,
            )
        )
        self.play(FadeIn(reference))
        self.wait(5)
        self.play(
            LaggedStartMap(
                FadeOut, VGroup(intro, desc, reference), lag_ratio=0.1, run_time=2
            )
        )
