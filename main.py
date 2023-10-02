#!/usr/bin/env python3

import argparse
import os

parser = argparse.ArgumentParser(description="SwaraAI-YT Manim Render")
parser.add_argument("class_name", help="Name of the class to be rendered")

parser.add_argument(
    "-r",
    "--resolution",
    help="Resolution of the video to be rendered",
    default="m",
    choices=["l", "m", "h", "p", "k"],
)

parser.add_argument(
    "-p",
    "--preview",
    help="Preview the animation before rendering",
    action="store_true",
)


args = parser.parse_args()
class_name = args.class_name
resolution = args.resolution
preview = args.preview

FLAGS = f"-q{resolution}"
if preview:
    FLAGS += " -p"

scenes = {
    "EV": "Methodology/0_start.py",
    "EV2EA": "Methodology/1_engVid_to_engAud.py",
    "EA2ET": "Methodology/2_engAud_to_engText.py",
    "ET2RT": "Methodology/3_engText_to_regText.py",
    "RT2RA": "Methodology/4_regText_to_regAud.py",
    "RA2RVCA": "Methodology/5_regAud_to_RVCAud.py",
    "RVCA2RV": "Methodology/6_RVCAud_to_regVid.py",
    "RV2RSV": "Methodology/7_regVid_to_regSubVid.py",
    "RV": "Methodology/8_end.py",
}

if class_name in scenes:
    scene = scenes[class_name]
    os.system(f"manim {scene} {class_name} {FLAGS}")
    print(f"Rendered {class_name}")
    os.system("python3 export.py")
    print(f"Exported {class_name}")

elif class_name == "all":
    for scene in scenes:
        os.system(f"manim {scenes[scene]} {scene} {FLAGS}")
        print(f"Rendered {scene}")
    os.system("python3 export.py")
    print(f"Exported all scenes")

else:
    print(f"Scene {class_name} not found")
