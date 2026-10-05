import cv2
import numpy as np

def add_overlay(
    frame: np.ndarray,
    fps: float,
    frame_number: int,
) -> np.ndarray:
    cv2.putText(frame, f"FPS: {fps:.1f}", (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA,)
    cv2.putText(frame, f"Frame: {frame_number}", (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA,)
    return frame