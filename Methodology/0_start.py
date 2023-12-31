from manim import *

from _imports import RenderNetwork, video_frame


class EV(RenderNetwork):
    def construct(self):
        _video_frame = video_frame()
        final_video_move = self.get_left_coord(_video_frame)
        video_label = Text("English Video").scale(0.5)
        always_redraw(lambda: video_label.next_to(_video_frame, DOWN * 1.5))

        video_group = VGroup(_video_frame, video_label)
        video_group_copy = video_group.copy().move_to(final_video_move)

        _video_frame.scale(3)
        video_label.next_to(_video_frame, DOWN * 1.5)

        self.add(_video_frame)
        self.play(Write(video_label))
        self.wait(1)
        self.play(Transform(video_group, video_group_copy))
