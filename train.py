from ultralytics import YOLO
import torch
import torchvision

assert torch.cuda.is_available(), "cuda.is_available() returned False."
assert torch.cuda.get_device_name(), "cuda.get_device_name() returned None."

model = YOLO("yolov8x.pt")

# yolov8m, best.pt: MARPE = 10
# yolov8x, best.pt: MARPE = 8.8
# yolov8x, last.pt, conf=0.5: MARPE = 3.8
# yolov8x, last.pt, conf=0.45: MARPE = 3.27


def start():
    model.train(data="data.yaml", epochs=500, patience=1000)


if __name__ == "__main__":
    start()