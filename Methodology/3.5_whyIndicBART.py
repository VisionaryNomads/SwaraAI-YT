from manim import *

from _imports import MyColors, latex


class WhyIndicBART(Scene):
    _intro = "Why IndicBART?"

    _desc = [
        "IndicBART is a multilingual sequence-to-sequence model for Indian languages.",
        "It currently supports 11 Indian languages which covers 95 percent of the Indian population.",
        "It is trained on large Indic language corpora (452 million sentences and 9 billion tokens).",
    ]

    _ref = "https://ai4bharat.iitm.ac.in/indicbart/"

    def construct(self):
        gap = DOWN * 1.5

        intro = latex(
            self._intro,
            15,
            color=WHITE,
            tex_environment="flushleft",
            tex_to_color_map={
                "IndicBART": MyColors.highlight_color,
            },
        ).to_corner(UL, buff=1)

        down_shift = 0
        desc = VGroup()
        for line in self._desc:
            line = (
                latex(
                    line,
                    16,
                    color=WHITE,
                    tex_environment="flushleft",
                    tex_to_color_map={
                        "multilingual sequence-to-sequence model": MyColors.highlight_color,
                        "11 Indian languages": MyColors.highlight_color,
                        "95 percent": MyColors.highlight_color,
                        "452 million sentences": MyColors.highlight_color,
                        "9 billion tokens": MyColors.highlight_color,
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
