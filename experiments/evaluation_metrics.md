# Evaluation metrics

## Speed

Measure average and peak forward velocity over the 100 m dash. Also record whether the robot maintains speed without falling or violating safety limits.

## Command tracking

Measure mean absolute error for forward, lateral and yaw velocity commands. Include high speed turning tests because straight line speed alone does not measure controllability.

## Stability

Record roll and pitch, fall count, time spent near safety limits and response to disturbances.

## Payload and terrain

Test the required payload mass and centre of mass variations. Evaluate flat ground, uneven terrain and obstacles within the problem statement.

## Actuator behaviour

Record joint and wheel command limits, torque or current saturation where available, and how often saturation occurs.

## Energy

Calculate cost of transport using the official energy definition and robot mass. A common dimensionless form is energy divided by weight times distance. The exact energy measurement must match the evaluation setup.

## Runtime

Measure the full control loop at 50 Hz. The complete cycle has 20 ms available, including sensing and command output. Report policy inference time separately from total loop time.
