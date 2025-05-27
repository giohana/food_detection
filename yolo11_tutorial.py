# -> pip install ultralytics


# import ultralytics
# ultralytics.checks()

# -> yolo predict model=yolo11n.pt source='https://ultralytics.com/images/zidane.jpg'

# import torch
# torch.hub.download_url_to_file('https://ultralytics.com/assets/coco2017val.zip', 'tmp.zip')

# -> unzip -q tmp.zip -d datasets && rm tmp.zip
# -> yolo val model=yolo11n.pt data=coco8.yaml
# -> yolo train model=yolo11n.pt data=coco8.yaml epochs=3 imgsz=640
# -> yolo export model=yolo11n.pt format=torchscript

# from ultralytics import YOLO

# # Load a model
# model = YOLO('yolo11n.yaml')  # build a new model from scratch
# model = YOLO('yolo11n.pt')  # load a pretrained model (recommended for training)

# # Use the model
# results = model.train(data='coco8.yaml', epochs=3)  # train the model
# results = model.val()  # evaluate model performance on the validation set
# results = model('https://ultralytics.com/images/bus.jpg')  # predict on an image
# results = model.export(format='onnx')  # export the model to ONNX format

# DETECTION

# # Load YOLO11n, train it on COCO128 for 3 epochs and predict an image with it
# from ultralytics import YOLO

# model = YOLO('yolo11n.pt')  # load a pretrained YOLO detection model
# model.train(data='coco8.yaml', epochs=3)  # train the model
# model('https://ultralytics.com/images/bus.jpg')  # predict on an image

# SEGMENTATION
# Load YOLO11n-seg, train it on COCO128-seg for 3 epochs and predict an image with it
# from ultralytics import YOLO

# model = YOLO('yolo11n-seg.pt')  # load a pretrained YOLO segmentation model
# model.train(data='coco8-seg.yaml', epochs=3)  # train the model
# model('https://ultralytics.com/images/bus.jpg')  # predict on an image
# DETETCTOU 1 PLACAA A MAIS Q O OUTRO

# CLASSIFICATION
# from ultralytics import YOLO

# model = YOLO('yolo11n-cls.pt')  # load a pretrained YOLO classification model
# model.train(data='mnist160', epochs=3)  # train the model
# model('https://ultralytics.com/images/bus.jpg')  # predict on an image

# POSE

# from ultralytics import YOLO

# model = YOLO('yolo11n-pose.pt')  # load a pretrained YOLO pose model
# model.train(data='coco8-pose.yaml', epochs=3)  # train the model
# model('https://ultralytics.com/images/bus.jpg')  # predict on an image


# CUSTOM DATASET

from ultralytics import YOLO
import os
from IPython.display import Image, display
from IPython import display
display.clear_output()
# -> yolo mode=checks

# -> yolo task=detect mode=train model=yolov8m.pt data=data.yaml epochs=20 imgsz=640
