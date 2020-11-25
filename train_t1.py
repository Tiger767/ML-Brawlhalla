import numpy as np
import tensorflow as tf
from tensorflow import keras
import cv2

from paiutils import image
from paiutils.neural_network import conv2d
from paiutils.reinforcement import (
    PGAgent, Memory
)

from environment import BrawlhallaSimple

if __name__ == '__main__':
    inputs = keras.layers.Input((48, 96, 3))
    x = conv2d(32, 5, 2)(inputs)
    x = conv2d(64, 3, 2)(x)
    x = conv2d(128, 3, 2)(x)
    x = conv2d(256, 3, 2)(x)
    x = conv2d(512, 3, 2)(x)
    x = keras.layers.Flatten()(x)
    outputs = keras.layers.Dense(7, activation='softmax')(x)
    model = keras.models.Model(inputs=inputs, outputs=outputs)
    model.compile(optimizer=keras.optimizers.Adam(.0001), loss='mse')
    model.summary()

    with image.Windows() as windows:
        env = BrawlhallaSimple(3, windows=windows)
        agent = PGAgent(model, .99, lambda: Memory(max_len=100000))
        agent.set_playing_data(training=False, memorizing=True)
        env.play_episodes(agent, 5, 100000, random=True, render=True, verbose=True, episode_verbose=True)
        #agent.load('20201124_223321_211317')
        agent.set_playing_data(training=False, memorizing=True, batch_size=32, mini_batch=3200, epochs=1, repeat=1, entropy_coef=0, verbose=True)
        for _ in range(10):
            env.play_episodes(agent, 20, 100000, render=True, verbose=True, episode_verbose=False)
            agent.save('')
        env.close()