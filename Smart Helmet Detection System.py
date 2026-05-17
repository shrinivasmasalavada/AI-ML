from ultralytics import YOLO
import cv2
import os
import time

# Load custom helmet model
model = YOLO("helmet.pt")

cap = cv2.VideoCapture(0)

save_path = "violations"

os.makedirs(save_path, exist_ok=True)

while True:

    ret, frame = cap.read()

    results = model(frame)

    annotated = results[0].plot()

    boxes = results[0].boxes

    for box in boxes:

        cls = int(box.cls[0])
        conf = float(box.conf[0])

        label = model.names[cls]

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        if label == "no_helmet" and conf > 0.5:

            cv2.putText(
                annotated,
                "NO HELMET ALERT",
                (x1, y1 - 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,0,255),
                2
            )

            filename = f"{save_path}/{time.time()}.jpg"
            cv2.imwrite(filename, frame)

            print("Violation Saved")

    cv2.imshow("Helmet Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()