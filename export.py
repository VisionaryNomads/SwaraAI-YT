import os
import shutil

videos_dir = "media/videos"

qualities = ["480p15", "720p30", "1080p60", "2160p60"]

for quality in qualities:
    exports_dir = f"exports/{quality}"

    if not os.path.exists(exports_dir):
        os.makedirs(exports_dir)

    for scene in os.listdir(videos_dir):
        files_dir = os.path.join(videos_dir, scene, quality)

        if not os.path.exists(files_dir):
            continue

        files = os.listdir(files_dir)
        for file in files:
            if file.endswith(".mp4"):
                shutil.copyfile(
                    os.path.join(videos_dir, scene, quality, file),
                    os.path.join(exports_dir, f"{scene}_{file}"),
                )
