import cv2
from video.source import open_video_source

def main() -> None:
    capture = open_video_source(0)  # Open the default camera (index 0)
    try:
        while True:
            success, frame = capture.read()
            if not success:
                print("Could not read frame from video source.")
                break
            cv2.imshow("Video Analysis", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()