from ultralytics import YOLO
model = YOLO('yolov8n-cls.pt') 
results = model.train(data='C:/Users/Sarath/Downloads/Dataset', epochs=200, imgsz=64)