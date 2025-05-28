# from ultralytics import YOLO

# # Load the YOLO11 model
# model = YOLO("runs/detect/train17/weights/best.pt")

# # Export the model to TFLite format
# model.export(format="tflite")  # creates 'yolo11n_float32.tflite'

# # Load the exported TFLite model
# tflite_model = YOLO("yolo11n_float32.tflite")

# # Run inference
# results = tflite_model("https://t3.ftcdn.net/jpg/06/27/23/56/360_F_627235669_iz0O2leKYRzjxAKdFP7odpp9eCOZREtN.jpg")

# import onnx
# from onnx_tf.backend import prepare

#onnx_model = onnx.load("runs/detect/train17/weights/best.onnx")
#tf_rep = prepare(onnx_model)
#tf_rep.export_graph("exported_tf_model")

# import tensorflow as tf

# converter = tf.lite.TFLiteConverter.from_saved_model("exported_tf_model")
# tflite_model = converter.convert()
# with open("model.tflite", "wb") as f:
#     f.write(tflite_model)


#from ultralytics import YOLO

#model = YOLO("runs/detect/train17/weights/best.pt")
#model.export(format="onnx", opset=13)

# import tensorflow as tf

# converter = tf.lite.TFLiteConverter.("runs/detect/train17/weights/best_saved_model")
# tflite_model = converter.convert()

# with open("model.tflite", "wb") as f:
#     f.write(tflite_model)

from ultralytics import YOLO

model = YOLO("runs/detect/train17/weights/best.pt")
results = model("https://ultralytics.com/images/bus.jpg")
results.show()
