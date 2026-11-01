# Initial solution for the DHAV-Hy wheeled quadruped

This repository contains my initial study and implementation plan for the xTerra Robotics problem statement on high speed locomotion for DHAV-Hy.

The main objective is to develop one proprioception based reinforcement learning policy that can drive the wheels and control the leg joints while maintaining stability at high forward speeds. The policy must work without cameras or LiDAR. It can use joint states and IMU measurements, including a history of observations.

## What is included

The research folder summarises five papers that are relevant to the problem.

The architecture folder describes the proposed policy inputs, outputs and training setup.

The code folder contains small standalone prototypes for a velocity curriculum, reward calculation, domain randomisation, observation history and a GRU policy.

The experiments folder describes the tests and metrics that should be used during development.

The docs folder contains the implementation sequence.

## Important project status

These files are an initial design and prototype, not a trained locomotion controller. The Python examples are not yet connected to the xTerra simulator, robot description, actuator interface or training framework. Their purpose is to make the proposed methods concrete and testable before integration.

The reward weights and randomisation ranges are starting values for experiments. They must be checked against the simulator, robot limits and the official evaluation setup before training.

## Problem constraints to keep in mind

The policy is expected to run at 50 Hz and produce 16 outputs. Leg joints are position controlled and wheels are velocity controlled. The allowed sensing is proprioceptive, based on joint states and IMU data. The task includes high speed forward motion, lateral and yaw velocity tracking, uneven ground, obstacles up to approximately 10 cm, a payload of at least 10 kg, payload centre of mass variation, and recovery from a specified lateral disturbance.

The 20 ms control period is the total time available for sensing, preprocessing, inference and command output. Neural network inference must therefore take substantially less than 20 ms.

## Suggested first milestone

Run the provided baseline in the simulator before changing the algorithm. Record its speed, tracking error, stability and energy use. Then change one part at a time so that improvements can be measured rather than assumed.
