from manim import *

from _imports import RenderNetwork, audio_wave


class RA2RVCA(RenderNetwork):
    def nn_name(self):
        return "Cloning voice to desired person using RVC"

    def nn_input(self):
        audio = audio_wave(4, 8)

        label = Text("Regional Audio")
        label.next_to(audio, DOWN).scale(0.5)

        return VGroup(audio, label)

    def nn_output(self):
        audio = audio_wave(2, 6)

        label = Text("Cloned Regional Audio")
        label.next_to(audio, DOWN).scale(0.5)

        return VGroup(audio, label)

    def fade_start(self):
        return False

    def slide_output(self):
        return True
