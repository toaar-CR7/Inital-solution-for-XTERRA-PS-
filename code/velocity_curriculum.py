import random


class VelocityCurriculum:
    def __init__(self, start_forward=0.5, max_forward=4.0, start_yaw=0.5, max_yaw=2.0):
        self.max_forward = start_forward
        self.max_yaw = start_yaw
        self.forward_limit = max_forward
        self.yaw_limit = max_yaw

    def update(self, success_rate):
        if success_rate > 0.85:
            self.max_forward = min(self.max_forward + 0.1, self.forward_limit)
            self.max_yaw = min(self.max_yaw + 0.05, self.yaw_limit)
        elif success_rate < 0.50:
            self.max_forward = max(0.2, self.max_forward - 0.1)
            self.max_yaw = max(0.2, self.max_yaw - 0.05)

    def sample_command(self):
        forward = random.uniform(0.0, self.max_forward)
        lateral = random.uniform(-0.5, 0.5)
        yaw = random.uniform(-self.max_yaw, self.max_yaw)
        return forward, lateral, yaw


if __name__ == "__main__":
    curriculum = VelocityCurriculum()

    for episode_group in range(10):
        measured_success_rate = 0.9
        curriculum.update(measured_success_rate)
        command = curriculum.sample_command()
        print("Forward limit:", round(curriculum.max_forward, 2))
        print("Yaw limit:", round(curriculum.max_yaw, 2))
        print("Sample command:", command)
