from manim import *

from _imports import MyColors, latex


class WhyIndicTTS(Scene):
    _intro = "Why IndicTTS?"

    _desc = [
        "IndicTTS is a text-to-speech (TTS) system for Indian languages developed by IIT Madras.",
        "It is a state-of-the-art TTS system for Indian languages.",
        "It is a high-quality, open-source, and multilingual TTS system.",
        "It can translate text to speech in 13 Indian languages.",
    ]

    _ref = "https://www.iitm.ac.in/donlab/tts/"

    def construct(self):
        gap = DOWN * 1.5

        intro = latex(
            self._intro,
            15,
            color=WHITE,
            tex_environment="flushleft",
            tex_to_color_map={
                "IndicTTS": MyColors.highlight_color,
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
                        "text-to-speech (TTS) system for Indian languages": MyColors.highlight_color,
                        "state-of-the-art TTS system": MyColors.highlight_color,
                        "high-quality, open-source, and multilingual TTS system": MyColors.highlight_color,
                        "13 Indian languages": MyColors.highlight_color,
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
        self.wait(27)
        self.play(
            LaggedStartMap(
                FadeOut, VGroup(intro, desc, reference), lag_ratio=0.1, run_time=2
            )
        )
