import cv2

print("🎥 Starting Live Edge Detection...")

# Open your webcam safely
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("❌ Could not access the camera.")
    exit()

print("✅ Camera opened successfully! Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Failed to grab frame.")
        break

    # 1️⃣ Convert to grayscale (edges work on brightness changes)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2️⃣ Blur to remove noise (reduces false edges)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 3️⃣ Detect edges
    edges = cv2.Canny(blurred, 50, 150)

    # 4️⃣ Add label text
    cv2.putText(edges, "Live Edge Detection | Press 'q' to Quit", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255), 2)

    # 5️⃣ Show both the original and edges side-by-side
    cv2.imshow("Original", frame)
    cv2.imshow("Edges", edges)

    # Exit when you press 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 6️⃣ Release everything
cap.release()
cv2.destroyAllWindows()
print("✅ Camera released and windows closed.")
