import cv2

print("🎥 Testing camera access...")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Could not access the camera.")
    exit()

print("Camera opened successfully! Press 'q' to quit.")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame.")
        break
    cv2.imshow("Camera Test", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Camera released and windows closed.")

