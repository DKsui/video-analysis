import time

class FPSCounter:
    def __init__(self) -> None:
        self._previous_time = time.perf_counter()
        self._fps = 0.0
    def update(self) -> float:
        current_time = time.perf_counter()
        elapsed = current_time - self._previous_time
        if elapsed > 0:
            self._fps = 1.0 / elapsed
        self._previous_time = current_time
        return self._fps
