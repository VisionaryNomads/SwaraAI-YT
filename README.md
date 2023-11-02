# SwaraAI - YouTube Video

[![SwaraAI Logo](logo.png)](https://www.youtube.com/watch?v=vvcQfcdNtH8)

YouTube video: [https://youtu.be/vvcQfcdNtH8](https://www.youtube.com/watch?v=vvcQfcdNtH8)

## Flow of the Presentation

This video is created in many scenes. All the exports are in the [`exports`](exports) folder. Order of the scenes are described in the [`flow.md`](flow.md) file.

## Installation

```bash
git clone https://github.com/VisionaryNomads/SwaraAI-YT.git
cd SwaraAI-YT
pip3 install -r requirements.txt
```

## Command to render the scenes

```bash
python3 main.py {SCENE} -r {RESOLUTION}
```

SCENE can be any of the key in the [`scenes.json`](scenes.json) file.

For RESOLUTION, see the [Quality of the Video](#quality-of-the-video) section.

To render all the scenes, execute `python3 main.py all -r {RESOLUTION}`.

To render scenes in a specific folder, execute `python3 main.py all -f {FOLDER} -r {RESOLUTION}`.

## Help

For more information, execute `python3 main.py --help`.

### Quality of the Video

720p30 is the default resolution. To change the resolution, use the `-r` flag.

Flags for resolution:

- `-rl 480p15 (854x480)`
- `-rm 720p30 (1280x720)`
- `-rh 1080p60 (1920x1080)`
- `-rp 1440p60 (2560x1440)`
- `-rk 2160p60 (3840x2160)`

## Credits

Created by [Gopal Saraf](https://gopalsaraf.com/).  
Created using [manim](https://www.manim.community/).

## License

This project is licensed under the [MIT License](LICENSE).
