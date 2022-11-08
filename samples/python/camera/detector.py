import cv2
import torchvision
import numpy
import torch
import argparse
import cv2
import detect_utils
from PIL import Image

import ecal.core.core as ecal_core
from ecal.core.publisher import StringPublisher

def detect(image, model,device):
    boxes, classes, labels = detect_utils.predict(image, model, device, 0.8)
    image = detect_utils.draw_boxes(boxes, classes, labels, image)

    return image, len(boxes)
