import gym
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Categorical

# Hyperparmeters
learning_rate = 0.0002
gamma = 0.98
n_rollout = 10

def main():
    env = gym.make('CartPole-v1')
    model = ActorCritic()