To use a webcam with a Raspberry Pi, follow these steps:  

1. **Install the `fswebcam` library**:  
   ```bash
   sudo apt install fswebcam
   ```  

2. **Create a folder to store images**:  
   ```bash
   mkdir -p /home/pi4/Images
   ```  

3. **Test the webcam** by capturing an image:  
   ```bash
   fswebcam -r 1280x720 --no-banner /home/pi4/Images/pic-name.jpg
   ```  
   - If the image is captured successfully, the webcam is working.  
   - If not, proceed with the next steps.  

4. **Install OpenCV for additional functionalities**:  
   ```bash
   pip3 install opencv-python
   ```  

5. **Update system libraries**:  
   ```bash
   sudo apt update
   sudo apt install libatlas-base-dev
   ```  

6. **Write a Python script to capture images**:  
   - Open Thonny editor.  
   - Create a new Python file and save it as `capture.py`.  
   - Write the necessary code to capture an image using OpenCV.