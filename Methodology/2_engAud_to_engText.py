from manim import *
import os

from _video import video_frame
from _audio import audio_frame

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from NeuralNetwork import RenderNetwork


class EA2ET(RenderNetwork):
    def nn_name(self):
        return "Google Speech-to-Text"

    def nn_input(self):
        audio = audio_frame(0, 4)

        label = Text("English Audio")
        label.next_to(audio, DOWN).scale(0.5)

        return VGroup(audio, label)

    def nn_output(self):
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

    def fade_start(self):
        return False

    def slide_output(self):
        return True
