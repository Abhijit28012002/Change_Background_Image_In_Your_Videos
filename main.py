import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os


cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
segmentor = SelfiSegmentation()

fpsReader= cvzone.FPS()

#imgBG=cv2.imread("images/1.jpg")

#imgBG=cv2.resize(imgBG,(640,480))

listImg = os.listdir("images")
imgList=[]
for imgPath in listImg:
    img = cv2.imread(f'images/{imgPath}')
    img=cv2.resize(img,(640,480))
    imgList.append(img)

indexImg=0


while True:
    status,img=cap.read()
    #imgOut=segmentor.removeBG(img,(255,0,255)) # Background image is Pink
    #imgOut=segmentor.removeBG(img,(255,0,0)) # Background image is Blue
    imgOut=segmentor.removeBG(img,imgList[indexImg],threshold=0.8)
    imgStacked=cvzone.stackImages([img,imgOut],2,1)
    fps,imgStacked=fpsReader.update(imgStacked)
    cv2.imshow("Image",imgStacked)
    #cv2.imshow("Image",imgOut)
    key=cv2.waitKey(1)
    if key == ord('a'):
        if indexImg>0:
            indexImg -=1
    elif key == ord('b'):
        if indexImg < len(imgList)-1:
            indexImg +=1
    elif key == ord('q'):
        break