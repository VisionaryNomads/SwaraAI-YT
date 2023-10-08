import os
import json
import configparser
import time

LOG_FILE = "rendered.log"

if not os.path.exists(LOG_FILE):
    open(LOG_FILE, "w").close()


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


def record_rendered_scene(scene_name, quality):
    with open(LOG_FILE, "r") as log_file:
        lines = log_file.readlines()

    with open(LOG_FILE, "w") as log_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{scene_name} - {quality} - {timestamp}\n")
        log_file.writelines(lines)


def get_scene_timestamp(scene_name, quality):
    with open(LOG_FILE, "r") as log_file:
        for line in log_file:
            parts = line.split(" - ")
            if len(parts) == 3 and parts[0] == scene_name and parts[1] == quality:
                return parts[2].strip()
    return None


def render_scene(scene_path, class_name, quality, manim_command, force_render):
    last_render_timestamp = get_scene_timestamp(class_name, quality)

    if (
        force_render
        or last_render_timestamp is None
        or os.path.getmtime(scene_path)
        > time.mktime(time.strptime(last_render_timestamp, "%Y-%m-%d %H:%M:%S"))
    ):
        exit_code = os.system(manim_command.format(scene_path, class_name))
        if exit_code == 0:
            print(f"Rendered {class_name} at quality {quality}")
            record_rendered_scene(class_name, quality)
            os.system("python3 export.py")
            print(f"Exported {class_name}")
        else:
            print(f"Error rendering {class_name}")
    else:
        print(
            f"No changes in {class_name} at quality {quality} since last render on {last_render_timestamp}"
        )
