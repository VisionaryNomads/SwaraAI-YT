import os
import shutil
import json


def load_scene_info():
    with open("scenes.json", "r") as json_file:
        return json.load(json_file)


videos_dir = "media/videos"
qualities = ["480p15", "720p30", "1080p60", "2160p60"]

scenes = load_scene_info()

for quality in qualities:
    exports_dir = f"exports/{quality}"

    if not os.path.exists(exports_dir):
        os.makedirs(exports_dir)

    for scene in os.listdir(videos_dir):
        files_dir = os.path.join(videos_dir, scene, quality)

        if os.path.exists(files_dir):
            files = os.listdir(files_dir)
            for file in files:
                if file.endswith(".mp4"):
                    file_parent = scenes[file.split(".")[0]].split("/")[0]

                    if not os.path.exists(os.path.join(exports_dir, file_parent)):
                        os.makedirs(os.path.join(exports_dir, file_parent))

                    shutil.copyfile(
                        os.path.join(videos_dir, scene, quality, file),
                        os.path.join(exports_dir, file_parent, f"{scene}_{file}"),
                    )
