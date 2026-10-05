import cv2

def open_video_source(source: int | str) -> cv2.VideoCapture:
    capture = cv2.VideoCapture(source)
    if not capture.isOpened():
        capture.release()
        raise RuntimeError(f"Failed to open video source: {source}")
    return capture