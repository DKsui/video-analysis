# Video Analysis

A simple video analysis application built with Python and OpenCV.

## Features

- Webcam input
- Video file input
- Configurable video source via CLI
- FPS overlay
- Frame counter
- Keyboard exit with `q`
- Safe resource cleanup
- Test video recording utility
- Modular project structure

## Project structure

```text
video_analysis/
├── assets/
├── output/
├── video/
│   ├── __init__.py
│   ├── processor.py
│   ├── source.py
│   └── stats.py
├── .gitignore
├── main.py
├── record_video.py
├── README.md
└── requirements.txt
```

**Installation**
Create and activate a virtual environment:
```
python3.12 -m venv .venv
source .venv/bin/activate
```
Install dependencies:
```
python -m pip install -r requirements.txt
```
**Usage**
Run with the default webcam
```
python main.py
```
or explicitly
```
python main.py --source 0
```
Analyze a video file
```
python main.py --source assets/sample.mp4
```
Press `q` to stop playback
**Record a test video**
You can record a local test video from the webcam
```
python record_video.py
```
Press `q` to stop recording
**CLI help**
```
python main.py --help
```
