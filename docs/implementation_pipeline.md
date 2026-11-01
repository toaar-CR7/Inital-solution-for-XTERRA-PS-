# Implementation pipeline

1. Read the supplied repository and identify the simulator, robot model, observation definition, action mapping and training entry point.
2. Run the unmodified baseline and save its configuration and metrics.
3. Verify the 16 action outputs and their mapping to wheel and leg actuators.
4. Add or tune the reward using the actual simulator signals and actuator limits.
5. Introduce a velocity curriculum over forward and yaw commands.
6. Compare a current observation MLP with a history based GRU policy.
7. Add domain randomisation for friction, payload, centre of mass, motor strength and sensor noise.
8. Evaluate the required payload, terrain, obstacle and disturbance conditions.
9. Run ablation tests and retain the best reproducible checkpoint.
10. Measure the complete 50 Hz control loop on the target class of onboard computer.
11. Pass simulation safety checks before any hardware test.
12. Document the final model, configuration, results and limitations.
