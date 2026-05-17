from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("traffic.mp4")

vehicle_classes = ["car", "motorcycle", "bus", "truck"]

count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    boxes = results[0].boxes

    for box in boxes:

        cls = int(box.cls[0])
        label = model.names[cls]

        if label in vehicle_classes:

            count += 1

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)

            cv2.putText(
                frame,
                label,
                (x1, y1-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,0),
                2
            )

    cv2.putText(
        frame,
        f"Vehicles: {count}",
        (20,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,0,0),
        2
    )

    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()