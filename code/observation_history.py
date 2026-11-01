from collections import deque
import numpy as np


class ObservationHistory:
    def __init__(self, observation_size, history_length):
        self.observation_size = observation_size
        self.history_length = history_length
        self.history = deque(maxlen=history_length)

    def reset(self, first_observation):
        self.history.clear()
        for _ in range(self.history_length):
            self.history.append(np.asarray(first_observation, dtype=np.float32))

    def add(self, observation):
        observation = np.asarray(observation, dtype=np.float32)

        if observation.shape != (self.observation_size,):
            raise ValueError("Observation has an unexpected shape")

        if not self.history:
            self.reset(observation)
        else:
            self.history.append(observation)

    def get_history(self):
        if not self.history:
            raise RuntimeError("History is empty. Call reset first.")

        return np.concatenate(list(self.history))


if __name__ == "__main__":
    history = ObservationHistory(observation_size=6, history_length=4)
    history.reset([0, 0, 0, 0, 0, 0])
    history.add([1, 0, 0, 0, 0, 0])
    history.add([2, 0, 0, 0, 0, 0])
    print(history.get_history())
