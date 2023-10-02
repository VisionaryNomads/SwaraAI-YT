from manim import *
import os

from _video import video_frame

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from NeuralNetwork import RenderNetwork


class RV(RenderNetwork):
    def construct(self):
        _video_frame = video_frame(True)
        final_video_move = self.get_right_coord(_video_frame)
        video_label = Text("Regional Subtitled \n    Dubbed Video").scale(0.5)
        always_redraw(lambda: video_label.next_to(_video_frame, DOWN * 2))

        video_group = VGroup(_video_frame, video_label)
        video_group_copy = video_group.copy().move_to(final_video_move)

        _video_frame.scale(3)
        video_label.next_to(_video_frame, DOWN * 2)

        self.add(video_group_copy)
        self.wait(1)
        self.play(Transform(video_group_copy, video_group))
