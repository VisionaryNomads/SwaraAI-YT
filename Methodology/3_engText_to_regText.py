from manim import *

from _imports import RenderNetwork


class ET2RT(RenderNetwork):
    def nn_name(self):
        return "English Text to Regional Text using IndicBART"

    def nn_input(self):
        text = Paragraph(
            "Transcription of English",
            "Audio into English Text",
            alignment="center",
            font_size=20,
            line_spacing=0.8,
            font="Sans",
        )

        border = SurroundingRectangle(text, buff=0.2)
        border.set_stroke(width=0.5).set_color(YELLOW)

        label = Text("English Text")
        label.next_to(border, DOWN).scale(0.5)

        return VGroup(border, text, label)

    def nn_output(self):
        text = Paragraph(
            "अनुवादित भारतीय क्षेत्रीय",
            "     भाषा    पाठ",
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

    def fade_start(self):
        return True

    def fade_end(self):
        return True
