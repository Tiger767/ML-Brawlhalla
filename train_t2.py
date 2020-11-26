import numpy as np
import tensorflow as tf
from tensorflow import keras
import cv2

from paiutils import image
from paiutils.neural_network import conv2d
from paiutils.reinforcement import (
    PGAgent, Memory
)

from environment import BrawlhallaSimple2

if __name__ == '__main__':
    inputs = keras.layers.Input((64, 64, 3))
    x = conv2d(32, 5, 2)(inputs)
    x = conv2d(64, 3, 2)(x)
    x = conv2d(128, 3, 2)(x)
    x = conv2d(256, 3, 2)(x)
    x = conv2d(512, 3, 2)(x)
    x = keras.layers.Flatten()(x)
    outputs = keras.layers.Dense(7, activation='softmax')(x)
    model = keras.models.Model(inputs=inputs, outputs=outputs)
    model.compile(optimizer=keras.optimizers.Adam(.0002), loss='mse')
    model.summary()

    with image.Windows() as windows:
        env = BrawlhallaSimple2(3, windows=windows)
        agent = PGAgent(model, .99, lambda: Memory(max_len=100000))
        agent.set_playing_data(training=False, memorizing=True)
        env.play_episodes(agent, 5, 10000, random=True, render=True,
                          verbose=True, episode_verbose=True)
        #agent.load('saves/20201125_231722_659083', load_data=False)
        #agent.amodel.optimizer = keras.optimizers.Adam(.0002)
        agent.set_playing_data(training=True, memorizing=True, batch_size=64,
                               mini_batch=12800, epochs=1, repeat=1,
                               entropy_coef=0, verbose=True)
        for ndx in range(9):
            avg = env.play_episodes(agent, 10, 10000, render=True,
                                    verbose=True, episode_verbose=False)
            agent.save('saves/', note=f'PGAGENT_{ndx}_{len(agent.states)}_{avg}')
        env.close()