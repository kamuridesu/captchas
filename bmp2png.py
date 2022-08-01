from PIL import Image
import glob
import os
import sys

path = "."
args = sys.argv[1:]
if args:
    path = args[0]

out_dir = 'results'
try: os.makedirs(out_dir)
except FileExistsError: pass

cnt = 0
for img in glob.glob(f'{path}/*.bmp'):
    Image.open(img).save(os.path.join(out_dir, str(cnt) + '.png'))
    cnt += 1

