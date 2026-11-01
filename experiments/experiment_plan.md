# Experiment plan

## Stage 1: Baseline

Run the provided policy and training setup without changing the main algorithm. Record the configuration, number of training steps, random seed and evaluation results.

## Stage 2: Velocity curriculum

Compare fixed command sampling with a curriculum that gradually expands forward velocity and yaw rate. Check whether higher command tracking performance leads to higher sustainable speed without more falls.

## Stage 3: Observation history

Compare an MLP policy using the current observation with a GRU policy using a short history. Keep the training budget and evaluation conditions as similar as possible.

## Stage 4: Wheel and leg coordination

Inspect the action mapping and verify that the policy controls the wheel and leg actuators through the same action interface. Compare the learned behaviour on flat and uneven ground.

## Stage 5: Domain randomisation

Add friction, payload, centre of mass, motor strength and sensor noise variation. Begin with modest ranges and increase them only when training remains stable. Evaluate the required 10 kg payload separately.

## Stage 6: Disturbance and safety tests

Test the specified lateral push, uneven terrain and obstacles within the problem statement. Record falls, recovery time, body attitude and actuator saturation.

## Stage 7: Deployment check

Measure the complete control loop on Raspberry Pi equivalent hardware. Confirm that sensor handling, preprocessing, inference and command output fit within the 20 ms control period.

## Fair comparison

Change one major factor at a time. Use the same evaluation commands, terrain sets and random seeds where possible. Keep the best checkpoint and configuration for every experiment.
