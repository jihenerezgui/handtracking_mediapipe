import cv2
from quickHand import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8,maxHands=2)

def main():
    while True:
        success, image = cap.read()
        hands = detector.findHands(image, draw=False)#,flipType=False)
        for hand in hands:
            fingers = detector.fingersUp(hand)
            detector.infoOnHand(image, hand, [f"{fingers} doigts"])
             #compléter la fonction infoHand dans le fichier quickHand pour ajouter le nombre de doights à coté des doights vus.
        cv2.imshow("Image", image)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break




if __name__ == '__main__':
    main()
