import gymnasium as gym
import numpy as np
from stable_baselines3 import A2C, PPO, DQN

ENVIRONMENTS = ["CartPole", "Acrobot", "FrozenLake"]
ALGORITHM = {
    "A2C": A2C,
    "PPO": PPO,
    "DQN": DQN
}

# TODO set your environment and algorithm here
environment_name = "Acrobot"
algorithm_name = "DQN"
nr_test_episodes = 10

env = gym.make(f"{environment_name}-v1", render_mode="rgb_array")
model = ALGORITHM[algorithm_name]("MlpPolicy", env, verbose=1)

# Train your agent (increase 'total_timesteps' is necessary)
model.learn(total_timesteps=10_000)

# Evaluate your trained agent
test_env = model.get_env()
returns = []
for e in range(nr_test_episodes):
    done = False
    return_value = 0.0
    obs = test_env.reset()
    while not done:
        random_noise = np.random.randn()
        # Decision on an action
        action, _ = model.predict(obs, deterministic=True)
        # Execution of the action
        obs, reward, done, info = test_env.step(action)

        test_env.render("human")
        return_value += reward
    print(f"Episode {e}: {return_value}")
    returns.append(return_value)
print(f"Average return: {np.mean(returns)}")