import cv2 as cv
from cvzone.FaceMeshModule import FaceMeshDetector


cap = cv.VideoCapture(0)
mesh = FaceMeshDetector(maxFaces=2)


while 1 :
    rec, frame = cap.read()
    frame, faces = mesh.findFaceMesh(frame)

    cv.imshow('frame', frame)
    if cv.waitKey(5) & 0XFF == ord('q'):
        break

cv.destroyAllWindows()
cap.release()