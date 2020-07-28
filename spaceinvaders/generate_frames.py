import os
import gym
from PIL import Image

stage = "test"
env = gym.make('SpaceInvadersNoFrameskip-v4')
print(env.observation_space, env.action_space)
count = 0
for e in range(100):
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
    count += step
    print(f"Done E{e}")

    if count > 3000:
        break
