import cv2
capture = cv2.VideoCapture(0)
if not capture.isOpened():
    raise RuntimeError("Failed to open video source: 0")
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
writer = cv2.VideoWriter("assets/sample.mp4", fourcc, 20.0, (width, height))
print("Recording video. Press 'q' to stop.")
try:
    while True:
        success, frame = capture.read()
        if not success:
            break
        writer.write(frame)
        cv2.imshow("Recording test video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    capture.release()
    writer.release()
    cv2.destroyAllWindows()