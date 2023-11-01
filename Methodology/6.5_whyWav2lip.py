from manim import *

from _imports import MyColors, latex


class WhyWav2Lip(Scene):
    _intro = "Why Wav2Lip?"

    _desc = [
        "Wav2Lip is a lip-syncing algorithm that can accurately map lip movements from an audio input to a video of a face.",
        "It is a state-of-the-art lip-syncing algorithm that can be used to create deepfakes.",
        "It is created by researchers at the Indian Institute of Information Technology, Hyderabad (IIIT-H).",
    ]

    _ref = "http://bhaasha.iiit.ac.in/lipsync/"

    def construct(self):
        gap = DOWN * 1.5

        intro = latex(
            self._intro,
            15,
            color=WHITE,
            tex_environment="flushleft",
            tex_to_color_map={
                "Wav2Lip": MyColors.highlight_color,
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
                        "lip-syncing algorithm": MyColors.highlight_color,
                        "state-of-the-art lip-syncing algorithm": MyColors.highlight_color,
                        "create deepfakes": MyColors.highlight_color,
                        "Indian Institute of Information Technology, Hyderabad (IIIT-H)": MyColors.highlight_color,
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
        self.wait(13)
        self.play(
            LaggedStartMap(
                FadeOut, VGroup(intro, desc, reference), lag_ratio=0.1, run_time=2
            )
        )
