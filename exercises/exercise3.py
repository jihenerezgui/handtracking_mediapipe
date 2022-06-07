import cv2
from quickHand import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8,maxHands=2)

def main():
    while True:
        success, image = cap.read()
        hands = detector.findHands(image, draw=False)#,flipType=False)
        for hand in hands:
            detector.infoOnHand(image, hand)

        cv2.imshow("Image", image)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break



if __name__ == '__main__':
    main()
