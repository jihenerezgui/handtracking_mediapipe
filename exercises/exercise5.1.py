import cv2
from quickHand import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8,maxHands=2)

def main():
    while True:
        success, image = cap.read()
        hands = detector.findHands(image, draw=False)#,flipType=False)
        for hand in hands:
            lmList = hand["lmList"]
            fingers = detector.fingersUp(hand)
            length, info, img = detector.findDistance(lmList[4][1:], lmList[8][1:], image)
            textsToDisplay = [f"{fingers} doigts", f"distance: {length}"]
            detector.infoOnHand(image, hand, textsToDisplay)

        cv2.imshow("Image", image)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break




if __name__ == '__main__':
    main()
