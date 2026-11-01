import torch
from torch import nn


class GRULocomotionPolicy(nn.Module):
    def __init__(self, observation_size, action_size=16, hidden_size=128):
        super().__init__()

        self.encoder = nn.Sequential(
            nn.Linear(observation_size, 128),
            nn.ELU()
        )

        self.gru = nn.GRU(
            input_size=128,
            hidden_size=hidden_size,
            batch_first=True
        )

        self.actor = nn.Sequential(
            nn.Linear(hidden_size, 128),
            nn.ELU(),
            nn.Linear(128, action_size)
        )

    def forward(self, observation_history):
        encoded = self.encoder(observation_history)
        sequence_output, hidden_state = self.gru(encoded)
        last_output = sequence_output[:, -1, :]
        action = self.actor(last_output)
        return action


if __name__ == "__main__":
    policy = GRULocomotionPolicy(observation_size=48)
    sample_history = torch.randn(2, 10, 48)
    sample_action = policy(sample_history)
    print("Output shape:", tuple(sample_action.shape))
