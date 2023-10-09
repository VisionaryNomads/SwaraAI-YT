#!/usr/bin/env python3

import argparse
import os

from helpers import (
    load_scene_info,
    load_render_settings,
    parse_args_and_kwargs,
    render_scene,
)


parser = argparse.ArgumentParser(description="SwaraAI-YT Manim Render")
parser.add_argument(
    "class_name",
    help="Name of the class to be rendered. Use 'all' to render all scenes.",
)

parser.add_argument(
    "-r",
    "--resolution",
    help="Resolution of the video to be rendered",
    default="",
    choices=["l", "m", "h", "p", "k"],
)

parser.add_argument(
    "-p",
    "--preview",
    help="Preview the animation before rendering",
    action="store_true",
)

parser.add_argument(
    "-f",
    "--folder",
    help="Folder name from which to render",
    default="",
)

parser.add_argument(
    "-a",
    "--args",
    help="Additional arguments to pass to Manim",
    default="",
)

parser.add_argument(
    "--force",
    help="Forcefully render scenes without checking timestamps",
    action="store_true",
)

args = parser.parse_args()
class_name = args.class_name
resolution = args.resolution
preview = args.preview
folder = args.folder
additional_args_str = args.args
force_render = args.force

scenes = load_scene_info()
render_settings = load_render_settings()

if resolution == "":
    resolution = render_settings.get("resolution", "m")
preview = render_settings.getboolean("preview", False)

FLAGS = f"-q{resolution}"
if preview:
    FLAGS += " -p"

additional_args, additional_kwargs = parse_args_and_kwargs(additional_args_str)

manim_command = "manim {} {} "
manim_command += f"{FLAGS} {' '.join(additional_args)}"

success_render = []
error_render = []

add_status = (
    lambda scene, is_rendered: success_render.append(scene)
    if is_rendered
    else error_render.append(scene)
)

if class_name in scenes:
    scene = scenes[class_name]
    is_rendered = render_scene(
        scene, class_name, resolution, manim_command, force_render
    )
    add_status(class_name, is_rendered)
    os.system("python3 export.py")
    print(f"Exported {class_name}")

elif class_name == "all":
    folder_name = lambda scene: scenes[scene].split("/")[0]

    should_render = lambda scene: scene != "Test" and (
        folder == "" or (folder != "" and folder == folder_name(scene))
    )

    for scene in scenes:
        if not should_render(scene):
            continue
        is_rendered = render_scene(
            scenes[scene], scene, resolution, manim_command, force_render
        )
        add_status(scene, is_rendered)

    os.system("python3 export.py")

    if len(success_render) > 0:
        print("Rendered scenes:")
        for scene in success_render:
            print(scene)

    if len(error_render) > 0:
        print("Error rendering scenes:")
        for scene in error_render:
            print(scene)

else:
    print(f"Scene {class_name} not found")
