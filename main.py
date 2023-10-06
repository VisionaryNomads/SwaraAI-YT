#!/usr/bin/env python3

import argparse
import os
import json
import configparser


def load_scene_info():
    with open("scenes.json", "r") as json_file:
        return json.load(json_file)


def load_render_settings():
    config = configparser.ConfigParser()
    config.read("settings.cfg")
    return config["RenderSettings"]


def parse_args_and_kwargs(args_str):
    args_list = args_str.split()
    args = []
    kwargs = {}
    for arg in args_list:
        if "=" in arg:
            key, value = arg.split("=")
            kwargs[key] = value
        else:
            args.append(arg)
    return args, kwargs


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
    "-a",
    "--args",
    help="Additional arguments to pass to Manim",
    default="",
)

args = parser.parse_args()
class_name = args.class_name
resolution = args.resolution
preview = args.preview
additional_args_str = args.args

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

if class_name in scenes:
    scene = scenes[class_name]
    exit_code = os.system(manim_command.format(scene, class_name))
    if exit_code == 0:
        print(f"Rendered {class_name}")
        os.system("python3 export.py")
        print(f"Exported {class_name}")
    else:
        print(f"Error rendering {class_name}")

elif class_name == "all":
    for scene in scenes:
        if scene == "Test":
            continue
        exit_code = os.system(manim_command.format(scenes[scene], scene))
        if exit_code == 0:
            success_render.append(scene)
            print(f"Rendered {scene}")
        else:
            error_render.append(scene)
            print(f"Error rendering {scene}")

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
