from manim import *
import os

from _video import video_frame
from _audio import audio_frame

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from NeuralNetwork import RenderNetwork


class EV2EA(RenderNetwork):
    def nn_name(self):
        return "Video to Audio"

    def nn_input(self):
        video = video_frame()

        video_label = Text("English Video")
        video_label.next_to(video, DOWN).scale(0.5)

        return VGroup(video, video_label)

    def nn_output(self):
        audio = audio_frame(0, 4)

        label = Text("English Audio")
        label.next_to(audio, DOWN).scale(0.5)

        return VGroup(audio, label)

    def slide_output(self):
        return True
