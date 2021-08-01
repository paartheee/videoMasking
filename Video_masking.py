

import numpy as np
import cv2


Vid_path = "E:\Spritle\Videos\L&T Loading 1\7-June-2021\00000000320000000 L&T J7 L1.mp4"

cap = cv2.VideoCapture(Vid_path)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('E:\Spritle\MyLearning\Video Masking\output.avi', fourcc, 20.0, (3072,1728))


while(True):

    # Capture frames in the video
    ret, frame = cap.read()
    ret, frame = cap.read()
    ret, frame = cap.read()
    ft = 20
    
    #cv2.rectangle(frame, (0, 1080), (500, 150), (0, 0, 0), -1)
    
    h, w, c = frame.shape
    x1, y1, w_size, h_size = [0.127604,0.575000,0.254167,0.850000]
    x = x1 - (w_size / 2)
    y = y1 - (h_size / 2)
    wid = x + w_size
    hig = y + h_size
    cv2.rectangle(frame, (int(x * w), int(y * h)),
              (int(wid * w), int(hig * h)), (0, 0, 0), -1)

    imS = cv2.resize(frame,(3072,1728))
    out.write(imS)
    cv2.imshow('video', imS)

    # creating 'q' as the quit
    # button for the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
# close all windows

cv2.VideoWriter
cv2.destroyAllWindows()


