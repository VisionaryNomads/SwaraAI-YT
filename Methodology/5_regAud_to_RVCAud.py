from manim import *
import os

from _audio import audio_frame

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from NeuralNetwork import RenderNetwork


class RA2RVCA(RenderNetwork):
    def nn_name(self):
        return "Cloning voice to desired person using RVC"

    def nn_input(self):
        audio = audio_frame(4, 8)

        label = Text("Regional Audio")
        label.next_to(audio, DOWN).scale(0.5)

        return VGroup(audio, label)

    def nn_output(self):
        audio = audio_frame(2, 6)

        label = Text("Cloned Regional Audio")
        label.next_to(audio, DOWN).scale(0.5)

        return VGroup(audio, label)

    def fade_start(self):
        return False

    def slide_output(self):
        return True
