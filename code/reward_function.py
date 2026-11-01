def calculate_reward(
    command,
    measured_velocity,
    roll,
    pitch,
    angular_velocity,
    energy,
    action,
    previous_action,
    collision,
    fallen,
    actuator_saturation
):
    forward_error = abs(command[0] - measured_velocity[0])
    lateral_error = abs(command[1] - measured_velocity[1])
    yaw_error = abs(command[2] - measured_velocity[2])

    tracking_reward = (
        2.5 * max(0.0, 1.0 - forward_error)
        + 1.5 * max(0.0, 1.0 - lateral_error)
        + 1.5 * max(0.0, 1.0 - yaw_error)
    )

    stability_penalty = 1.2 * (roll ** 2 + pitch ** 2)
    angular_penalty = 0.08 * sum(value ** 2 for value in angular_velocity)
    energy_penalty = 0.002 * max(0.0, energy)

    action_change = sum(
        (current - previous) ** 2
        for current, previous in zip(action, previous_action)
    )
    smoothness_penalty = 0.03 * action_change

    collision_penalty = 5.0 if collision else 0.0
    fall_penalty = 20.0 if fallen else 0.0
    saturation_penalty = 0.5 * sum(bool(value) for value in actuator_saturation)

    reward = (
        tracking_reward
        - stability_penalty
        - angular_penalty
        - energy_penalty
        - smoothness_penalty
        - collision_penalty
        - fall_penalty
        - saturation_penalty
    )

    return reward
