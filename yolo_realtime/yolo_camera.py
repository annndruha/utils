import torch
import cv2
from PIL import Image


class YOLO:
    def __init__(self):
        self.model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)

    def __call__(self, img):
        im = Image.fromarray(img)
        results = self.model(im)
        results.render()
        return results.imgs[0]

vid = cv2.VideoCapture(0)
yolo = YOLO()

while True:
    ret, frame = vid.read()
    img = yolo(frame)
    cv2.imshow('frame', img)
    print(frame.shape)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


vid.release()
cv2.destroyAllWindows()