import cv2
import numpy as np

def load_yolo():
    # Load YOLO model
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    
    # Load COCO class labels
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    
    return net, output_layers, classes

def detect_item(image_path, item_name):
    net, output_layers, classes = load_yolo()

    # Load image
    img = cv2.imread(image_path)
    height, width, _ = img.shape

    # Prepare the image for YOLO
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layers)

    # Process the outputs
    class_ids = []
    confidences = []
    boxes = []
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # You can adjust the confidence threshold
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Use Non-Maximum Suppression to eliminate duplicate boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    # Check if the item is detected
    for i in range(len(boxes)):
        if i in indexes:
            label = str(classes[class_ids[i]])
            if label.lower() == item_name.lower():
                return True

    return False


# # Example usage
# if __name__ == "__main__":
#     image_path = "path_to_your_image.jpg"
#     item_name = "dog"  # Example item to search for
#     found = detect_item(image_path, item_name)
#     if found:
#         print(f"{item_name} is present in the image.")
#     else:
#         print(f"{item_name} is not present in the image.")