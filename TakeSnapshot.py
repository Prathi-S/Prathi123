import cv2

def snap():
    videoCaptureObject=cv2.VideoCapture(0)
    result=True

    while(result):
        ret,frame=videoCaptureObject.read()
        cv2.imwrite("Picture1.png",frame)
        result=False



    videoCaptureObject.release()
    cv2.destroyAllWindows()

snap()