import random


def sample_physics():
    return {
        "friction": random.uniform(0.5, 1.2),
        "payload_mass": random.uniform(0.0, 10.0),
        "payload_com_x": random.uniform(-0.07, 0.07),
        "payload_com_y": random.uniform(-0.07, 0.07),
        "payload_com_z": random.uniform(0.0, 0.14),
        "motor_strength": random.uniform(0.9, 1.1),
        "sensor_noise": random.uniform(0.0, 0.02)
    }


def sample_required_payload_test():
    return {
        "payload_mass": 10.0,
        "payload_com_x": random.uniform(-0.07, 0.07),
        "payload_com_y": random.uniform(-0.07, 0.07),
        "payload_com_z": random.uniform(0.0, 0.14)
    }


if __name__ == "__main__":
    print("Random training configuration:")
    print(sample_physics())
    print("Required payload test configuration:")
    print(sample_required_payload_test())
