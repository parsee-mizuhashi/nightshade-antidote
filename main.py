import numpy as np
import cv2
import argparse
from pathlib import Path
from cv2.ximgproc import guidedFilter

def clean(imagepath: str, save_suffix: str = '.cured'):
    img = cv2.imread(imagepath).astype(np.float32)
    y = img.copy()
    for _ in range(64):
        y = cv2.bilateralFilter(y, 5, 8, 8)
    for _ in range(4):
        y = guidedFilter(img, y, 4, 16)
    return cv2.imwrite(imagepath.replace('.png', save_suffix+'.png'), y)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, required=True)
    parser.add_argument('--suffix', '-s', type=str, required=False, default='.cured')
    args = parser.parse_args()
    if Path(args.input).is_file():
        clean(args.input, args.suffix)
    else:
        for file in Path(args.input).glob('*.png'):
            clean(file, args.suffix)
