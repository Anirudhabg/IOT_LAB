import cv2
import time

num = 1
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    cv2.imshow("Frame", img)
    # When in keyboard 'c' is pressed the photo is taken.
    if cv2.waitKey(1) & 0xFF == ord("c"):
        cv2.imwrite("/home/pi4/Images/" + str(num) + ".jpg", img)
        print("Capture " + str(num) + " Successful!")
        num += 1

    if num == 4:
        break

cap.release()
cv2.destroyAllWindows()
