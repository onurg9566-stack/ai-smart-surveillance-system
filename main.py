import cv2
import time
from detector import HumanDetector
from tracker import Tracker
from alarm import Alarm

detector = HumanDetector()
tracker = Tracker()
alarm = Alarm()

cap = cv2.VideoCapture(0)

# FPS
prev_time = 0

# alarm kontrolü
alarm_triggered = False

# ROI (güvenli alan)
roi_x1, roi_y1 = 100, 100
roi_x2, roi_y2 = 500, 400

# video kayıt
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detections = detector.detect(frame)
    objects = tracker.update(detections)

    # ROI çiz
    cv2.rectangle(frame, (roi_x1, roi_y1), (roi_x2, roi_y2), (255,0,0), 2)

    for obj in objects:
        cx, cy, x1, y1, x2, y2 = obj

        # bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.circle(frame, (cx, cy), 5, (0,0,255), -1)

        # ROI alarm
        if roi_x1 < cx < roi_x2 and roi_y1 < cy < roi_y2:
            if not alarm_triggered:
                alarm.trigger()
                alarm_triggered = True

                # screenshot
                cv2.imwrite("intruder.jpg", frame)
        else:
            alarm_triggered = False

    # FPS hesaplama
    current_time = time.time()
    fps = 1 / (current_time - prev_time) if prev_time != 0 else 0
    prev_time = current_time

    cv2.putText(frame, f"FPS: {int(fps)}", (10,30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    # video kaydet
    out.write(frame)

    cv2.imshow("AI Surveillance System", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()