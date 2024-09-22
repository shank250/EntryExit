import cv2
import time
import csv
import os
import json

url = 'http://192.168.137.127:8080/video' # Update this URL based on your setup
# Update this URL based on your setup

def decode_qr_codes():
    cap = cv2.VideoCapture(url)

    # Create a window with a resizable size
    cv2.namedWindow("QR Code Scanner", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("QR Code Scanner", 640, 480)  # Set window size, not frame size

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame. Check your connection.")
            break

        # Convert frame to grayscale for QR code detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # QR Code detection
        detect = cv2.QRCodeDetector()
        value, points, _ = detect.detectAndDecode(gray)

        if value:
            spliting = value.split("id=")
            global id
            id = spliting[1]
            print(f"ID: {id}")

            # Save the scanned ID to CSV file
            save_id_to_csv(id)

            # Draw bounding box around QR code
            if points is not None:
                points = points[0]
                for i in range(len(points)):
                    pt1 = (int(points[i][0]), int(points[i][1]))
                    pt2 = (int(points[(i + 1) % len(points)][0]), int(points[(i + 1) % len(points)][1]))
                    cv2.line(frame, pt1, pt2, (0, 255, 0), 3)

                # Display the scanned ID above the bounding box
                cv2.putText(frame, f"ID: {id}", (int(points[0][0]), int(points[0][1]) - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

            # Add a delay to avoid rescanning too quickly
            time.sleep(1)
            break

        # Show the frame in a resized window
        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def save_id_to_csv(scanned_id):
    file_exists = os.path.isfile("scanned_ids.csv")

    # Open the CSV file in append mode
    with open("scanned_ids.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["ID"])  # Write header if file doesn't exist
        writer.writerow([scanned_id])  # Write the scanned ID

def main():
    while True:
        decode_qr_codes()

main()
