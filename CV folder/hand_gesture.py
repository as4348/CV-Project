import cv2
import numpy as np

print("🎥 Starting Hand Gesture Recognition...")

# Open webcam safely
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("❌ Could not access the camera.")
    exit()

print("✅ Camera opened successfully! Place your hand inside the green box. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Failed to grab frame.")
        break

    roi = frame[100:400, 100:400]
    cv2.rectangle(frame, (100, 100), (400, 400), (0, 255, 0), 2)

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    mask = cv2.GaussianBlur(mask, (5, 5), 100)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        cnt = max(contours, key=lambda x: cv2.contourArea(x))
        hull = cv2.convexHull(cnt)
        cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)
        cv2.drawContours(roi, [hull], -1, (0, 0, 255), 2)

    cv2.putText(frame, "Hand Gesture | Press 'q' to Quit", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Hand Gesture Recognition", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("✅ Camera released and windows closed.")
