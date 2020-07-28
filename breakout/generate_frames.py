import os
import gym
from PIL import Image

stage = "test"
env = gym.make('BreakoutNoFrameskip-v4')
print(env.observation_space, env.action_space)
for e in range(3):
    try:
        os.mkdir(f'{stage}/{e:04d}')
    except:
        break
    images = [env.reset()]
    actions = []
    while True:

        action = env.action_space.sample()
        actions.append(action)
        obs_next, reward, done, info = env.step(action)
        if done:
            break
        images.append(obs_next)

    step = 0
    with open(f'{stage}/{e:04d}/act.log', 'w') as f:
        for img, act in zip(images, actions):
            img = Image.fromarray(img)
            img.save(f'{stage}/{e:04d}/{step:05d}.png')
            f.write(f'{act}\n')
            step += 1

    print(f"Done E{e}")



