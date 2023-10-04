from manim import *

from _imports import RenderNetwork, audio_wave


class RT2RA(RenderNetwork):
    def nn_name(self):
        return "Text to Speech using IndicTTS"

    def nn_input(self):
        text = Paragraph(
            "अनुवादित भारतीय क्षेत्रीय",
            "      भाषा पाठ",
            alignment="center",
            font_size=20,
            line_spacing=0.8,
            font="Sans",
        )

        border = SurroundingRectangle(text, buff=0.2)
        border.set_stroke(width=0.5).set_color(YELLOW)

        label = Text("Regional Text")
        label.next_to(border, DOWN).scale(0.5)

        return VGroup(border, text, label)

    def nn_output(self):
        audio = audio_wave(4, 8)

        label = Text("Regional Audio")
        label.next_to(audio, DOWN).scale(0.5)

        return VGroup(audio, label)

    def fade_start(self):
        return False

    def slide_output(self):
        return True
