# Design decisions and assumptions

## Decisions

The initial algorithm to investigate is PPO because it is widely used for continuous locomotion control and is suitable for parallel simulation training. I will first use the training algorithm already present in the supplied codebase if one is provided, rather than replacing working infrastructure without a reason.

The first policy comparison will be an MLP against a GRU with a short observation history. This is a manageable experiment and tests whether temporal information helps under changing friction and payload conditions.

The policy will be unified. It will produce wheel velocity targets and leg joint position targets in one action vector. I will not introduce a hand written terrain mode switch because the policy does not receive terrain perception.

The command curriculum will include forward velocity and yaw rate together. Lateral commands will be included if they are part of the command interface and evaluation setup.

## Assumptions to verify in the supplied codebase

The exact ordering and units of the 16 policy outputs must be checked in the runner and robot interface.

The exact observation vector, joint order, IMU convention, action scaling and control frequency must be checked before connecting any prototype to the simulator.

The actual motor limits, joint limits, wheel limits, robot mass and inertia must come from the robot description or hardware documentation.

The official centre of mass variations and payload definition must be interpreted exactly as written in the PS. A centre of mass offset is not necessarily the same thing as moving the payload by that distance.

The exact definition of energy used for the COT score must be confirmed. Electrical energy, mechanical work and actuator effort are not interchangeable.

## Important limitation

The blind policy cannot see an obstacle before contact. It can react to body motion, joint response and IMU changes after interacting with the terrain. This makes obstacle handling a feedback and robustness problem rather than a visual path planning problem.
