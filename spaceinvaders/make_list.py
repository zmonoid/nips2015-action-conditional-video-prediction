
import glob

fs = glob.glob('train/*/*.png')

with open('img_list.txt', 'w') as f:
    for x in fs:
        f.write(x + '\n')
