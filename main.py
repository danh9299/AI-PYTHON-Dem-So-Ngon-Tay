import cv2 as cv 
#Thêm thư viện cv2 để xử lý hình ảnh
from cvzone.HandTrackingModule import HandDetector 
#Thêm thư viện để bắt chuyển động của bàn tay
import time 
#Thư viện thời gian để tính thời gian chờ

detector = HandDetector(detectionCon=0.8, maxHands=2) 
#Xác định tay, cho phép cả tay trái và tay phải, tối đa 2 tay

video_cap = cv.VideoCapture(0) 
#Bắt sự kiện video

while 1:
    success, image = video_cap.read()
    #Đọc các hình ảnh từ video
    hands, image = detector.findHands(image)
    #Tìm kiếm tay

    cv.rectangle(image, (0, 480), (400, 425),(0, 255, 255), -2)
    
    totalFingers = 0
    if hands:
        for hand in hands:
            fingersUp = detector.fingersUp(hand)
            totalFingers += sum(fingersUp)
    cv.putText(image, f'So Ngon Tay: {totalFingers}', (60, 460), cv.FONT_HERSHEY_TRIPLEX, 1, (0,0,0), 1, cv.LINE_AA)
    
    cv.imshow('Image:', image)

    key = cv.waitKey(1)
    if key ==ord('x'):
        break

    # Kiểm tra sự kiện nút close trên cửa sổ
    if cv.getWindowProperty('Image:', cv.WND_PROP_VISIBLE) < 1:
        break