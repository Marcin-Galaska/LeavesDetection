import json
from pathlib import Path
from typing import Dict

import click
import cv2 as cv
from tqdm import tqdm

# Real-time object detection
from ultralytics import YOLO

# Item number array
leaves = {}


def detect(img_path: str) -> Dict[str, int]:
    global leaves

    img = cv.imread(img_path, cv.IMREAD_COLOR)

    # Load pretrained, best model
    model = YOLO('last.pt')

    # Perform prediction
    results = model.predict(img, conf=0.45, half=False)

    # Save items
    for i, j in model.names.items():
        leaves[j] = results[0].boxes.cls.tolist().count(i)
    aspen = leaves['aspen']
    birch = leaves['birch']
    hazel = leaves['hazel']
    maple = leaves['maple']
    oak = leaves['oak']

    return {'aspen': aspen, 'birch': birch, 'hazel': hazel, 'maple': maple, 'oak': oak}


@click.command()
@click.option('-p', '--data_path', help='Path to data directory',
              type=click.Path(exists=True, file_okay=False, path_type=Path), required=True)
@click.option('-o', '--output_file_path', help='Path to output file', type=click.Path(dir_okay=False, path_type=Path),
              required=True)
def main(data_path: Path, output_file_path: Path):
    img_list = data_path.glob('*.jpg')

    results = {}

    for img_path in tqdm(sorted(img_list)):
        leaves = detect(str(img_path))
        results[img_path.name] = leaves

    with open(output_file_path, 'w') as ofp:
        json.dump(results, ofp)


if __name__ == '__main__':
    main()