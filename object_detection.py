from ultralytics import YOLO

model = YOLO('yolov8n.pt')


def detect_objects(input_path):
    try:
        result = model.predict(source=input_path, save=True)
        return '/runs/detect/predict'
    except():
        return False


