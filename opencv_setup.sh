#!/bin/bash

# Update and upgrade the system
echo "Updating and upgrading the system..."
sudo apt update && sudo apt upgrade -y

# Install dependencies for building OpenCV and handling images and video
echo "Installing necessary libraries..."
sudo apt install -y cmake build-essential pkg-config git
sudo apt install -y libjpeg-dev libtiff-dev libjasper-dev libpng-dev
sudo apt install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt install -y libxvidcore-dev libx264-dev
sudo apt install -y libfontconfig1-dev libcairo2-dev
sudo apt install -y libgdk-pixbuf2.0-dev libpango1.0-dev
sudo apt install -y libgtk2.0-dev libgtk-3-dev
sudo apt install -y libatlas-base-dev gfortran
sudo apt install -y libhdf5-dev libhdf5-103
sudo apt install -y libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5

# Install OpenCV Python library
echo "Installing OpenCV library..."
pip install opencv-python-headless numpy

# Download Haar Cascade Frontal Face XML file
echo "Downloading Haar Cascade Frontal Face XML file..."
wget -O ~/haarcascade_frontalface_default.xml https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml

echo "Setup complete. You can now use OpenCV with Haar Cascade for face detection."
