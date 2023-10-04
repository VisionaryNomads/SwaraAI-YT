from manim import *


def video_frame(add_subtitle=False):
    video_frame = RoundedRectangle(
        width=8.0,
        height=4.5,
        color=WHITE,
        stroke_width=2,
        fill_opacity=1.0,
        fill_color=BLACK,
        corner_radius=0.2,
    )

    status_bar = Rectangle(
        width=6.0,
        height=0.01,
        color=GRAY,
        fill_opacity=0.7,
    )

    time_label_left = Text("1:00", color=WHITE, font_size=15)
    time_label_right = Text("4:00", color=WHITE, font_size=15)
    time_label_left.next_to(status_bar, LEFT)
    time_label_right.next_to(status_bar, RIGHT)

    red_bar = Rectangle(
        width=1.5,
        height=0.01,
        color=RED_E,
        fill_opacity=0.7,
    )
    red_bar.move_to(status_bar.get_left() - LEFT * red_bar.width * 0.5)

    red_dot = Dot(color=RED_E)
    red_dot.move_to(red_bar.get_right() + RIGHT * red_dot.width * 0.5)

    bar = VGroup(status_bar, time_label_left, time_label_right, red_bar, red_dot)
    bar.move_to(video_frame.get_bottom() - DOWN * bar.height * 2)

    if add_subtitle:
        subtitle_text = Text(
            "उपशीर्षक",
            color=BLACK,
            font_size=10,
            font="Sans",
        )
        subtitle_text.set_stroke(width=0.3, color=BLACK)
        subtitle_box = Rectangle(
            width=2.5,
            height=0.18,
            color=GRAY,
            fill_opacity=0.8,
            stroke_width=0,
        )
        subtitle_text.move_to(subtitle_box.get_center())
        subtitle = VGroup(subtitle_box, subtitle_text)
        subtitle.move_to(video_frame.get_bottom() - DOWN * bar.height * 2 - DOWN * 1.35)

    play_button = RegularPolygon(
        n=3,
        fill_opacity=1.0,
        color=RED_E,
    )
    play_button.set(height=0.5)
    play_button.rotate(-TAU / 4)
    play_button.move_to(video_frame)

    video = VGroup(video_frame, bar, play_button).scale(0.4)

    if add_subtitle:
        video.add(subtitle)

    return video
