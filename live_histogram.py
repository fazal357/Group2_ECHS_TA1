#!/usr/bin/env python3
"""
Live Histogram from RTSP Stream
--------------------------------
Press 'q' to quit.
"""

import cv2
import numpy as np
import time

# 🔹 Replace with your actual RTSP URL
RTSP_URL = "rtsp://username:password@ip_address:554/your_stream"

# Open the RTSP stream using FFMPEG backend
cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print("❌ Unable to open RTSP stream.")
    exit()

print("✅ RTSP stream opened. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠ Frame grab failed, retrying…")
        time.sleep(0.5)
        continue

    # Resize frame for faster processing
    frame = cv2.resize(frame, (320, 240))

    # --- Compute histograms for B, G, R channels ---
    chans = cv2.split(frame)
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # BGR colors
    hist_h, hist_w = 200, 512
    bins = 256
    hist_img = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)

    for i, ch in enumerate(chans):
        hist = cv2.calcHist([ch], [0], None, [bins], [0, 256])
        cv2.normalize(hist, hist, 0, hist_h, cv2.NORM_MINMAX)
        hist = hist.flatten()
        for b in range(1, bins):
            x1 = int((b - 1) * (hist_w / bins))
            x2 = int(b * (hist_w / bins))
            y1 = int(hist_h - hist[b - 1])
            y2 = int(hist_h - hist[b])
            cv2.line(hist_img, (x1, y1), (x2, y2), colors[i], 1)

    # Display both the video feed and histogram
    cv2.imshow("RTSP Feed", frame)
    cv2.imshow("Live Histogram (BGR)", hist_img)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
