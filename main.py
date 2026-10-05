import cv2
from video.source import open_video_source
from video.processor import add_overlay
from video.stats import FPSCounter
import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple video analysis application.")
    parser.add_argument("--source", default=0, help="Camera index or path to a video file. Default is 0 (the first camera).")
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    source: int | str
    if args.source.isdigit():
        source = int(args.source)
    else:
        source = args.source
    capture = open_video_source(source)
    fps_counter = FPSCounter()
    frame_number = 0
    try:
        while True:
            success, frame = capture.read()
            if not success:
                print("Could not read frame from video source.")
                break
            frame_number += 1
            fps = fps_counter.update()
            frame = add_overlay(frame, fps, frame_number)
            cv2.imshow("Video Analysis", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()