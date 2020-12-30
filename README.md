# ML-Brawlhalla
The purpose of this repository is to publish results achieved while attempting a machine learning solution of creating a bot in Brawlhalla.

Disclaimer: This bot is not for any competitive contexts, where such a bot would be deemed cheating. This bot is solely created and published to show the potential of machine learning algorithms in a popular game. Also, no hacking of the game was performed, meaning the game's inner state was not touched (ex. reading the game's memory). All actions were performed with keypresses, and the states of the game were observed through screenshots.

The code for some of the trials is published here, but the Brawhalla training environments are not published.

Trial 1
- Goal: The agent will be able to 1v1 and perform better than a random agent.
- Actions: Left, Right, Left Heavy, Right Heavy, Left Light, Right light, Nothing
- Input: Preprocessed screenshot (fixed; view of stadium)
- Rewards: -time, dealt damage, -(recieved damage), enemey died, -(player died)
- Simplifications: Trained on only one character, limited number of actions, only uses fist, only one stadium used, only fights one character, fighting an easy bot
- Algorithm: Policy Gradients (No Critic)
- Actor
  - Model: Input((48, 96, 3)) -> Conv(32, 5) -> Conv(64, 3) -> Conv(128, 3) -> Conv(256, 3) -> Conv(512, 3) -> Flatten() -> Dense(7, Softmax)
    - Conv(filter, kernel_size) = Conv2D(filter, kernel_size=kernel_size, strides=2) -> ReLu -> BatchNorm 
  - Optimizer: Adam(.0001)
- Agent Parameters
  - Discount Rate: .99
  - Memory: 100000
- Learning Parameters
  - Batch Size: 32
  - Mini-Batch Size (Sample size from all experience): 3200
  - Epochs (Number of complete gradient steps per episode): 1
- Environment Parameters:
  - Frames Stacked (for a single state): 3
- Training
  - Episodes of Random Agent (exploring): 5
  - Episodes of Policy Gradient Agent (convergence episodes): 180
  - Epochs: 180
- Conclusion: The agent, on average, is better than the random agent, but not by much. However, progress was seen, suggesting that training the agent for a more extended period would achieve the goal in a much more viewable manner.

Trial 2
- Goal: The agent will be able to 1v1 and perform better than a random agent.
- Actions: Left, Right, Nothing, Left Heavy, Right Heavy, Left Light, Right light
  - Jumps are performed by heavy attacks when in the air
- Input: Preprocessed screenshot (follow; view of player with immediate surroundings)
- Rewards: -time, dealt damage, -(recieved damage), enemey died, -(player died)
- Simplifications: Trained on only one character, limited number of actions, only one stadium used, only fights one character, fighting an easy bot
- Algorithm: Policy Gradients (No Critic)
- Actor
  - Model: Input((64, 64, 3)) -> Conv(32, 5) -> Conv(64, 3) -> Conv(128, 3) -> Conv(256, 3) -> Conv(512, 3) -> Flatten() -> Dense(7, Softmax)
    - Conv(filter, kernel_size) = Conv2D(filter, kernel_size=kernel_size, strides=2) -> ReLu -> BatchNorm 
  - Optimizer: Adam(.0001)
- Agent Parameters
  - Discount Rate: .99
  - Memory: 100000
- Learning Parameters
  - Batch Size: 64
  - Mini-Batch Size (Sample size from all experience): 12800
  - Epochs (Number of complete gradient steps per episode): 1
- Environment Parameters:
  - Frames Stacked (for a single state): 3
- Training
  - Episodes of Random Agent (exploring): 5
  - Episodes of Policy Gradient Agent (convergence episodes): 80
  - Epochs: 80
- Testing:
  - Average of 20 Episodes: 5.033
  - Best Total Reward: 23.23
  - Random Agent Average of 20 Episodes: -6.249
  - Random Agent Best Total Reward: 21.561
- Conclusion: This agent averages a reward of about 5, which is much better than the random agent. The agent is noticeably smarter than the random agent as seen in the gameplay videos.

Trial 3
 - Goal: The agent will be able to 1v1 and on average perform better against a medium difficulty bot.
 - Actions: Neutral, Left, Right, Up, Down, Heavy, Light, Throw, Dodge
  - Directional actions can be combined with other actions
 - Input: Preprocessed screenshot (follow; view of player with immediate surroundings), active actions, and healths of both players
 - Rewards: -time, dealt damage, -(recieved damage), enemey killed, -(player killed), enemy suicide, -(player suicide), -(attack action)
 - Simplifications: Trained on only one character, only one stadium used, only fights one character, fighting a medium bot
 - Algorithm: Policy Gradients (No Critic)
- Agent Parameters
  - Discount Rate: .99
  - Memory: No limit (using ETDMemory)
- Learning Parameters
  - Batch Size: 32
  - Mini-Batch Size (Sample size from all experience): 64
  - Epochs (Number of complete gradient steps per episode): 1
- Environment Parameters:
  - Frames Stacked (for a single state): 3
- Training
  - Episodes of Random Agent (exploring): 50
  - Episodes of Policy Gradient Agent (convergence episodes): 50
  - Epochs: 50
- Testing:
  - Average of 20 Episodes: -0.241
  - Best Total Reward: 4.874
  - Random Agent Average of 50 Episodes: -0.09
  - Random Agent Best Total Reward: 15.226
- Conclusion: This agent, on average, is worse than the random agent. The limited number of episodes played (100 in total with the 50th having the highest convergence) for the more complex action space may explain why this agent performed poorly. Ultimately, the goal of this trial was not reached in any sense.

Gameplay from a random agent (watch at +2x speed):

[![Random Agent Gameplay](https://img.youtube.com/vi/276vlZKAxcQ/0.jpg)](https://youtu.be/276vlZKAxcQ)

Gameplay from the trial 2 agent (watch at +2x speed):

[![Trial 2 Agent Gameplay](https://img.youtube.com/vi/0AEZq08cpEo/0.jpg)](https://youtu.be/0AEZq08cpEo)

Gameplay from the trial 3 agent
[![Trial 3 Agent Gameplay](https://img.youtube.com/vi/LYZ-LCBU9aU/0.jpg)](https://youtu.be/LYZ-LCBU9aU)
