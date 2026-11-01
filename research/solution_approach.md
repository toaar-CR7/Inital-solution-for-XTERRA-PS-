# Proposed solution approach

## Main idea

I propose to train one reinforcement learning policy that controls the wheel velocities and leg joint positions together. The policy will use only joint states, IMU data and a short history of previous observations and actions. It will not depend on cameras or LiDAR.

The aim is to reach high forward speeds without losing the ability to turn, track lateral commands, handle uneven ground and carry the required payload.

## 1. Establish a baseline

I will first run the provided training and simulation setup without major changes. This gives a reference for speed, tracking error, falls, actuator saturation and energy use. I will keep the baseline configuration so that later experiments can be compared fairly.

## 2. Train speed and turning together

I will use a velocity command curriculum. Training can begin with moderate forward speeds and small yaw commands. As the robot tracks these commands reliably, the command range can expand. Forward velocity and yaw rate should be sampled together because turning at high speed is more difficult than straight line motion.

Lateral velocity commands should also be included where supported by the task interface. The curriculum should not increase difficulty simply according to training time. It should use measured tracking and stability performance.

## 3. Learn wheel and leg coordination

The same policy will output wheel velocity commands and leg joint position targets. On smooth ground, the policy should learn to use rolling for efficient movement. When body motion and contact indicate uneven terrain or a disturbance, it should learn to use leg motion to maintain stability.

Since the policy is blind to upcoming terrain, I will not manually switch modes based on terrain labels at deployment. The coordination should emerge from training and feedback.

## 4. Use observation history

A single observation may not reveal whether the robot is slipping, whether the payload has changed, or how the ground is affecting the robot. I will compare a feed forward MLP policy with a history based policy such as a GRU. The history will contain recent proprioceptive observations and, if supported by the framework, previous actions.

A teacher student setup is another possible experiment. A teacher can use privileged simulator information during training, while the deployed student receives only the allowed proprioceptive inputs. The student must be trained to work without privileged information at run time.

## 5. Improve simulation to hardware transfer

Training should vary physical properties that are uncertain on the real robot. These include ground friction, motor strength, sensor noise, payload mass and payload location. The simulator should include the required 10 kg payload and the specified centre of mass offsets.

Randomisation ranges must be based on the PS and hardware specifications. They should not be so broad that the policy learns a poor compromise for the main 100 m sprint.

## 6. Include actuator limits

The policy must not depend on motor commands that the hardware cannot produce. I will use the actual motor torque speed and velocity limits in the simulator where available. The reward can penalise saturation, excessive effort and abrupt action changes. The simulator and actuator interface should also enforce hard safety limits.

## 7. Evaluate with separate tests

I will measure flat ground maximum sustainable speed, velocity tracking, yaw control at speed, lateral tracking, falls, response to the specified lateral push, payload performance, self collisions, energy use and policy inference time.

I will keep a record of each experiment and change one major factor at a time. The best policy should pass simulation safety checks before any hardware deployment.
