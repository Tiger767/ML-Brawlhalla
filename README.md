# ML-Brawlhalla
The purpose of this repository is to publish results achieved while attempting a machine learning solution of creating a bot in Brawlhalla.

Disclaimer: This bot is not for any competitive contexts, where such a bot would be deemed cheating. This bot is solely created and published to show the potential of machine learning algorithms in a popular game. Also, no hacking of the game was performed, meaning the game's inner state was not touched (ex. reading the game's memory). All actions were performed with keypresses, and the states of the game were observed through screenshots.

The code for each training trial is published here, but the Brawhalla training environments are not published.

Trial 1
- Goal: The agent will be able to 1v1 and perform better than a random agent.
- Actions: Left, Right, Left Heavy, Right Heavy, Left Light, Right light, Nothing
- Input: Preprocessed screenshot
- Rewards: -time, dealt damage, -(recieved damage), enemey died, -(player died)
- Simplifications: Trained on only 1 character, limited number of actions, only uses fist, only one stadium used
- Algorithm: Policy Gradients (No Critic)
- Actor
  - Model: Input -> Conv(32, 5) -> Conv(64, 3) -> Conv(128, 3) -> Conv(256, 3) -> Conv(512, 3) -> Flatten() -> Dense(7, Softmax)
    - Conv(filter, kernel_size) = Conv2D(filter, kernel_size=kernel_size, strides=2) -> ReLu -> BatchNorm 
  - Optimizer: Adam(.0001)
- Agent Parameters
  - Discount Rate: .99
  - Memory: 100000
- Learning Parameters
  - Batch Size: 32
  - Mini-Batch size (Sample size from all experience): 3200
  - Epochs (Number of complete gradient steps per episode): 1
- Environment Parameters:
  - Frames stacked to make a state: 3
- Training
  - Episodes of Random Agent (exploring): 5
  - Episodes of Policy Gradient Agent (convergence episodes): 180
  - Epochs: 180
- Conclusion: The agent, on average, is better than the random agent, but not by much. However, progress was seen, suggesting that training the agent for a more extended period would achieve the goal in a much more viewable manner.

Gameplays from a random agent:
![](./gifs/random_1.gif)
![](./gifs/random_2.gif)
![](./gifs/random_3.gif)

Gameplays from a ~1 hour trained (trial 1) agent using a policy gradient reinforcement algorithm:
![](./gifs/trained_t1_1.gif)
![](./gifs/trained_t1_2.gif)
![](./gifs/trained_t1_3.gif)
