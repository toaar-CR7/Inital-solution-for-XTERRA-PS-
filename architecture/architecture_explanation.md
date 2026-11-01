# Proposed policy architecture

## Data flow

The policy receives the current proprioceptive observation and a short history of previous observations. Depending on the supplied interface, the observation may include body angular velocity, body orientation estimate, joint positions, joint velocities and commanded forward, lateral and yaw velocities.

The observation is normalised using statistics collected during training. A history buffer stores a fixed number of recent observations. The resulting sequence is passed to a GRU policy or, for the baseline, a feed forward MLP.

The policy outputs a 16 dimensional action vector. The exact mapping from each output to a wheel or leg actuator must be taken from the supplied runner code. The outputs are scaled and sent to the existing control interface. Leg joints receive position targets and wheels receive velocity targets.

## Training setup

The policy is trained in simulation using reinforcement learning. The reward combines command tracking, body stability, energy or actuator effort, action smoothness and penalties for unsafe behaviour. Training randomises uncertain physical parameters such as friction, payload and motor strength.

A curriculum gradually expands the commanded velocity range after the policy reaches acceptable tracking and stability performance.

## Deployment constraints

The controller runs at 50 Hz, so one complete control cycle takes 20 ms. Sensor reading, preprocessing, policy inference and command output must all fit within that period. The neural network itself should use only a fraction of the available time.

The deployed policy must use only the permitted proprioceptive measurements. Privileged simulation information may be used to train a teacher, but it must not be required by the deployed student.

## Architecture sketch

Proprioceptive sensors and command
        |
        v
Observation normalisation
        |
        v
Recent observation history
        |
        v
MLP baseline or GRU policy
        |
        v
16 dimensional action vector
        |
        v
Action scaling and safety limits
        |
        v
Leg joint position targets and wheel velocity targets
