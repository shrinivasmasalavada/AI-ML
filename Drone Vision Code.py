from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("drone_video.mp4")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model.track(frame, persist=True)

    annotated = results[0].plot()

    cv2.imshow("Drone AI Vision", annotated)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()