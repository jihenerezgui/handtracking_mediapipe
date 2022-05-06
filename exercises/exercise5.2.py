import cv2
from quickHand import HandDetector

cap = cv2.VideoCapture(-1)
detector = HandDetector(detectionCon=0.8,maxHands=2)

def main():
    while True:
        success, image = cap.read()
        hands = detector.findHands(image, draw=False)#,flipType=False)

        if len(hands) == 1:
            hand = hands[0]
            detector.infoOnHand(image, hand, [detector.fingersUp(hand)])
            
        elif len(hands) == 2:
            length, info, img = detector.findDistance(hands[0]["lmList"][8][1:],
                                                      hands[1]["lmList"][8][1:], image)

            distance = f"distance: {length}"
            detector.infoOnHand(image, hands[0], [f"{detector.fingersUp(hands[0])} doigts", distance])
            detector.infoOnHand(image, hands[1], [f"{detector.fingersUp(hands[1])} doigts", distance])

        cv2.imshow("Image", image)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break




if __name__ == '__main__':
    main()
