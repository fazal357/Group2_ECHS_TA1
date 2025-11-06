# 📘 4. README 

Below is a professional README.md content you can include in your GitHub or presentation folder.

🧠 Live Histogram from RTSP Stream
📍 Overview

This project visualizes the real-time color distribution of a live RTSP video feed using OpenCV. It plots a dynamic BGR histogram, helping understand the brightness, contrast, and color spread in live footage — useful in camera calibration, lighting correction, and computer vision preprocessing.

# ⚙️ Requirements

Jetson Nano Orin (or any Linux device)

Python 3.8+

OpenCV 4.x

Numpy

GStreamer RTSP support

Install with:

sudo apt install python3-opencv python3-numpy gstreamer1.0-tools -y

# 📸 RTSP Setup

Use your mobile camera as RTSP stream source.
Apps like IP Webcam (Android) or RTSP Camera Server (iOS) can generate links like:

rtsp://192.168.1.101:554/stream


If authentication is enabled:

rtsp://username:password@192.168.1.101:554/stream

# ▶️ Running the Project
python3 live_histogram.py


Controls:

Press q → Quit

Histogram auto-updates as scene changes

# 🧩 Output Example

Left Window: Live camera feed

Right Window: Real-time histogram

Blue curve → Blue intensity distribution

Green curve → Green intensity distribution

Red curve → Red intensity distribution

<img width="794" height="564" alt="Screenshot 2025-11-06 120547" src="https://github.com/user-attachments/assets/467f0f38-dd1b-4d2e-8f45-7f629cc3c90d" />

<br> </br>
  
<img width="781" height="563" alt="image" src="https://github.com/user-attachments/assets/a7d1bb2e-8a99-45c7-9c16-d0c3e93eb2b3" />


# 🧮 How It Works

The program continuously captures frames from the RTSP source.

Each frame is split into its B, G, R channels.

A histogram is computed for each channel using cv2.calcHist().

The histograms are normalized and plotted in a single frame.

Both the live video and histogram are displayed simultaneously.

# 💡 Applications

Live image quality monitoring

Exposure analysis

Color correction calibration

Camera tuning on embedded devices (Jetson, Raspberry Pi)

# 👨‍💻 Author

Mohammad Fazal Faruk Attar
Project under Jetson Nano Orin Platform
For AI-based Visual Analytics Research
